```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/YOUR_INFURA_ID"))

private_key = "YOUR_PRIVATE_KEY"
wallet_address = "0xYourWalletAddress"
contract_address = "0xYourContractAddress"

abi = [
    {
        "inputs": [{"name": "_value", "type": "uint256"}],
        "name": "set",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract = w3.eth.contract(address=contract_address, abi=abi)

tx = contract.functions.set(123).build_transaction({
    "from": wallet_address,
    "nonce": w3.eth.get_transaction_count(wallet_address),
    "gas": 100000,
    "gasPrice": w3.eth.gas_price
})

signed_tx = w3.eth.account.sign_transaction(tx, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

print("Transaction Hash:", tx_hash.hex())
```
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Block Number:", receipt.blockNumber)
chain_id = w3.eth.chain_id
latest_block = w3.eth.block_number
balance = w3.eth.get_balance(wallet_address)
print("Wallet:", wallet_address)
print("Chain ID:", chain_id)
print("Latest Block:", latest_block)
print("Balance:", balance)
tx_count = w3.eth.get_transaction_count(wallet_address)
