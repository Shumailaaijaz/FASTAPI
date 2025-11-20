from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = {
    "shumaila": {"pin":1122, "balance":5000},
    "ali": {"pin":3333, "balance":3000},
    "anas": {"pin":2222, "balance":50000}
}

class AuthRequest(BaseModel):
    name: str
    pin_number: int

class DepositRequest(BaseModel):
    name: str
    amount: float

class TransferRequest(BaseModel):
    sender_name: str
    sender_pin: int
    recipient_name: str
    amount: float

@app.post("/authenticate")
def authenticate_user(auth_request: AuthRequest):
    user = users.get(auth_request.name)
    if not user or user["pin"] != auth_request.pin_number:
        raise HTTPException(status_code=401, detail={"error": "Invalid Credentials"})
    return {"name": auth_request.name, "bank_balance": user["balance"]}

@app.post("/deposit")
def deposit_funds(deposit_request: DepositRequest):
    if deposit_request.amount <= 0:
        raise HTTPException(status_code=400, detail={"error": "Deposit amount must be positive"})
    
    user = users.get(deposit_request.name)
    if not user:
        raise HTTPException(status_code=404, detail={"error": "User not found"})
    
    user["balance"] += deposit_request.amount
    return {"name": deposit_request.name, "bank_balance": user["balance"]}

@app.post("/bank-transfer")
def bank_transfer(transfer_request: TransferRequest):
    # Authenticate sender
    sender = users.get(transfer_request.sender_name)
    if not sender or sender["pin"] != transfer_request.sender_pin:
        raise HTTPException(status_code=401, detail={"error": "Invalid Credentials"})

    # Check for positive amount
    if transfer_request.amount <= 0:
        raise HTTPException(status_code=400, detail={"error": "Transfer amount must be positive"})
        
    # Check if sender has enough balance
    if sender["balance"] < transfer_request.amount:
        raise HTTPException(status_code=400, detail={"error": "Insufficient balance"})
        
    # Check if recipient exists
    recipient = users.get(transfer_request.recipient_name)
    if not recipient:
        raise HTTPException(status_code=404, detail={"error": "Recipient not found"})
        
    # Perform transfer
    sender["balance"] -= transfer_request.amount
    recipient["balance"] += transfer_request.amount
    
    return {
        "message": "Transfer successful",
        "sender": {"name": transfer_request.sender_name, "updated_balance": sender["balance"]},
        "recipient": {"name": transfer_request.recipient_name, "updated_balance": recipient["balance"]}
    }

@app.get("/")
def read_root():
    return {"message": "Bank API running"}