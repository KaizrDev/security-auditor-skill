"""
WARNING: THIS CODE IS FOR TESTING PURPOSES ONLY.
It contains intentional security vulnerabilities designed to be detected 
by the Claude Security Auditor tool. DO NOT use this code in a production environment.
"""

import sqlite3
import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

# VULNERABILITY: Hardcoded Secret
SECRET_KEY = "super_secret_unprotected_key_123"

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    
    # VULNERABILITY: SQL Injection
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    query = f"SELECT username FROM users WHERE id = {user_id}"
    cursor.execute(query)
    user = cursor.fetchone()
    
    # VULNERABILITY: Cross-Site Scripting (XSS)
    return render_template_string(f"<h1>Hello, {user[0]}</h1>")

@app.route("/execute")
def run_command():
    cmd = request.args.get("cmd")
    
    # VULNERABILITY: Remote Code Execution (RCE) / Command Injection
    os.system(cmd)
    return "Command executed"

if __name__ == "__main__":
    app.run(debug=True)
