import os

from web3 import Web3
import json, hashlib

from dotenv import load_dotenv

load_dotenv()
# ✅ Use Sepolia endpoint (replace YOUR_INFURA_KEY)

infura_url = os.getenv("INFURA_URL")
sender_address = os.getenv("PUBLIC_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")

w3 = Web3(Web3.HTTPProvider(infura_url))

print("Connected:", w3.is_connected())
if not w3.is_connected():
    quit()
power_data = {
    "latitude": 22.9734,
    "longitude": 78.6569,
    "currently_powered": True,
    "power_availability": 90,
    "number_of_power_cuts": 3,
    "number_of_complaints": 1,
    "avg_time_of_daily_power": 18
}
transaction_hex = "0x42238ee6577ffe50475ff44420775498f869ce9d0dc23c435958d586b042174c"
data_str = json.dumps(power_data, sort_keys=True)
data_hash = hashlib.sha256(data_str.encode()).hexdigest()

# Replace with your Sepolia wallet private key and address
tx = w3.eth.get_transaction(transaction_hex)
on_chain_data = tx["input"]
print(on_chain_data, data_hash, transaction_hex)
# # Create transaction
# tx = {
#     "to": None,  # None means it's a data-only transaction
#     "value": 0,
#     "gas": 54028 + len(data_hash) * 10,  # small buffer for data
#     "gasPrice": w3.to_wei("5", "gwei"),
#     "nonce": w3.eth.get_transaction_count(sender_address),
#     "data": w3.to_hex(text=data_hash)
# }
#
# # Sign and send
# signed_tx = w3.eth.account.sign_transaction(tx, private_key)
# tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
#
# print("Transaction sent!")
# print("Tx Hash:", w3.to_hex(tx_hash))
