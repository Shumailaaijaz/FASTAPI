# 🏦 SecureBank - Modern Banking Application

A beautiful, modern banking application built with Streamlit and FastAPI.

## ✨ Features

- 🔐 Secure user authentication
- 💰 Real-time balance tracking
- 💵 Deposit funds
- 🔄 Bank transfers between accounts
- 📊 Transaction history
- 🎨 Beautiful glass-morphism UI design
- 📱 Responsive layout

## 🚀 Quick Start

### 1. Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 2. Start the FastAPI Backend

\`\`\`bash
uvicorn main:app --reload
\`\`\`

The API will run on `http://localhost:8000`

### 3. Start the Streamlit App (in a new terminal)

\`\`\`bash
streamlit run streamlit_app.py
\`\`\`

The app will open in your browser at `http://localhost:8501`

## 👤 Demo Accounts

- **User 1:** Username: `shumaila`, PIN: `1122`, Balance: $5,000
- **User 2:** Username: `ali`, PIN: `3333`, Balance: $3,000
- **User 3:** Username: `anas`, PIN: `2222`, Balance: $50,000

## 🎯 How to Use

1. **Login:** Use one of the demo accounts to sign in
2. **Deposit:** Add funds to your account
3. **Transfer:** Send money to other users
4. **Track:** View your transaction history

## 🎨 Design Features

- Modern gradient backgrounds
- Glass-morphism effect containers
- Smooth animations and transitions
- Interactive hover effects
- Responsive design
- Real-time balance updates

## 🔧 Configuration

If your FastAPI server is running on a different URL, update the `API_URL` variable in `streamlit_app.py`:

\`\`\`python
API_URL = "http://localhost:8000"  # Change this to your server URL
\`\`\`

## 📝 Notes

- This is a demo application for educational purposes
- In production, use proper security measures like password hashing
- Consider using a real database instead of in-memory storage
- Implement proper authentication tokens for security

## 🛠️ Technologies Used

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Styling:** Custom CSS with animations
- **HTTP Client:** Requests

Enjoy your modern banking experience! 🎉
"# FASTAPI" 
