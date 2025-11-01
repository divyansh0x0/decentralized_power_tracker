import hashlib
import json
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from pymongo import MongoClient
from bson import ObjectId
import os
from web3 import Web3
from dotenv import load_dotenv
from urllib.parse import quote_plus
load_dotenv()

MONGODB_URL = quote_plus(os.getenv("MONGODB_URL"))
client = MongoClient()
db = client["power_grid"]
collection = db["IOTs"]
api = FastAPI()
INFURA_URL = os.getenv("INFURA_URL")  # e.g. https://sepolia.infura.io/v3/YOUR_PROJECT_ID
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Your wallet private key
SENDER_ADDRESS = os.getenv("PUBLIC_ADDRESS")  # Your wallet address
# Allow specific origins (your frontend URL)
origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not w3.is_connected():
    raise RuntimeError("Could not connect to Web3")
else:
    print("connected to WEB3")

class PowerData(BaseModel):
    iot_id: str
    recorded_at: datetime
    latitude: float
    longitude: float
    pincode: int
    power_availability: int = Field(..., ge=0, le=1)
    number_power_cuts: int = 0
    number_complaints: int = 0


class TransactionData(BaseModel):
    power_data: PowerData
    transaction_id: str
    blockchain_hash: str
    verified_on_chain_at:datetime


def makeTransaction(power_data: PowerData) -> TransactionData:
    # 1️⃣ Create SHA-256 hash of the power data
    data_str = json.dumps(power_data.model_dump(), sort_keys=True)
    data_hash = hashlib.sha256(data_str.encode()).hexdigest()
    data_hex = "0x" + data_hash

    # 2️⃣ Create transaction
    nonce = w3.eth.get_transaction_count(SENDER_ADDRESS)
    tx = {
        "to": None,  # No recipient — data-only tx
        "value": 0,
        "gas": 54028 + len(data_hash) * 10,
        "gasPrice": w3.to_wei("5", "gwei"),
        "nonce": nonce,
        "data": w3.to_hex(text=data_hash),
        "chainId": 11155111  # Sepolia Chain ID
    }

    # 3️⃣ Sign and send transaction
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    print(f"✅ Transaction sent: {w3.to_hex(tx_hash)}")

    # 4️⃣ Return TransactionData object
    return TransactionData(
        power_data=power_data,
        transaction_id=w3.to_hex(tx_hash),
        blockchain_hash=data_hex,
        verified_on_chain_at=datetime.now()
    )


@api.post("/power-data/")
def add_power_data(data: PowerData):
    transaction_data = makeTransaction(data)
    result = collection.insert_one(transaction_data.model_dump())
    return {"id": str(result.inserted_id), "message": "Data inserted successfully"}


@api.get("/")
def hello_msg():
    return {"data": "Welcome to decentralized power tracking"}


@api.get("/power-data/")
def get_power_data(
    txid: str | None = Query(None),
    iotid: str | None = Query(None),
    pincode: str | None = Query(None),
):
    query = {}
    if txid:
        query["transaction_id"] = txid
    if iotid:
        query["power_data.iot_id"] = iotid
    if pincode:
        query["power_data.pincode"] = int(pincode)

    docs = list(collection.find(query, {"_id": 0}))
    if not docs:
        raise HTTPException(status_code=404, detail="No matching data found")

    return {"count": len(docs), "data": docs}
