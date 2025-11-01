import dataclasses
import hashlib
import json
import os
from dataclasses import dataclass
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pymongo import MongoClient, collection
from pymongo.server_api import ServerApi
from web3 import Web3

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
client = MongoClient(MONGODB_URL, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["power_grid"]
collection = db["IoTs"]
api = FastAPI()
INFURA_URL = os.getenv("INFURA_URL")  # e.g. https://sepolia.infura.io/v3/YOUR_PROJECT_ID
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Your wallet private key
SENDER_ADDRESS = os.getenv("PUBLIC_ADDRESS")  # Your wallet address
# Allow specific origins (your frontend URL)
origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not w3.is_connected():
    raise RuntimeError("Could not connect to Web3")
else:
    print("Successfully Connected to WEB3!")


class PowerData(BaseModel):
    iot_id: str
    recorded_at: str
    latitude: float
    longitude: float
    pincode: int
    is_power_available: bool
    avg_power_availability: float = Field(..., ge=0, le=1)
    avg_power_cuts_count: int = 0
    complaints_count: int = 0


@dataclass
class TransactionData:
    power_data: str
    transaction_id: str
    blockchain_hash: str
    verified_on_chain_at: str


def make_transaction(power_data: PowerData) -> TransactionData:
    # 1️⃣ Create SHA-256 hash of the power data
    power_data_dict = power_data.model_dump()
    data_str = json.dumps(power_data_dict, sort_keys=True)
    data_hash = hashlib.sha256(data_str.encode()).hexdigest()
    data_hex = "0x" + data_hash
    print(data_str)

    # 2️⃣ Create transaction
    nonce = w3.eth.get_transaction_count(SENDER_ADDRESS, 'pending')
    tx = {
        "to": None,  # No recipient — data-only tx
        "value": 0,
        "gas": 54028 + len(data_hash) * 10,
        "gasPrice": int(w3.eth.gas_price * 1.2),
        "nonce": nonce,
        "data": w3.to_hex(text=data_hash),
        "chainId": 11155111  # Sepolia Chain ID
    }
    #
    # 3️⃣ Sign and send transaction
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    # hash = "0x42238ee6577ffe50475ff44420775498f869ce9d0dc23c435958d586b042174c"
    tx_hash_str = w3.to_hex(tx_hash)
    print(f"✅ Transaction sent: {tx_hash_str}")
    #
    # 4️⃣ Return TransactionData object
    return TransactionData(
        power_data=data_str,
        transaction_id=tx_hash_str,
        blockchain_hash=data_hex,
        verified_on_chain_at=str(datetime.now().isoformat())
    )


@api.post("/power-data/")
def add_power_data(data: PowerData):
    print(data)
    transaction_data = make_transaction(data)
    print(transaction_data)

    transaction_data_dict = dataclasses.asdict(transaction_data)
    result = collection.insert_one(transaction_data_dict)
    return { "message": "Data inserted successfully"}


@api.get("/")
def hello_msg():
    return {"data": "Welcome to decentralized power tracking"}


def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc


@api.get("/power-data/")
def get_power_data(
        txid: str | None = Query(None),
        iotid: str | None = Query(None),
        pincode: str | None = Query(None),
):
    if collection.count_documents({}) == 0:
        return {"count": 0, "data": []}
    query = {}
    if txid:
        query["transaction_id"] = txid
    if iotid:
        query["power_data.iot_id"] = iotid
    if pincode:
        query["power_data.pincode"] = int(pincode)

    docs = list(collection.find(query))

    if not docs:
        raise HTTPException(status_code=404, detail="No matching data found")

    return {
        "count": collection.count_documents(query),
        "data": [serialize_doc(d) for d in docs]
    }
