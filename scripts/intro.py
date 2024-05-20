
import os
import sqlite3
from flask import Flask, request
import subprocess

API_KEY = "your_api_key_here"

# sensitive information visibility
def display_credentials():
    username = "admin"
    password = "admin"
    print("user: " + username + " " + "pass: " + password)

# Hardcoded secret
def get_api_key():
    return API_KEY

# user input as param -> sql inj attack
def unsafe_query(user_input):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s' % user_input)
    return cursor.fetchall()


# no user input sanitizing -> XSS attack  
app = Flask(__name__)
@app.route('/search')
def search():
    query = request.args.get('q', '')
    return 'Search results for: ' + query

def write_to_file(data):
    with open('output.txt', 'w') as f:
        f.write(data)

# file permissions set to 777
def change_file_permissions():
    os.chmod('output.txt', 777)  # Insecure file permissions -> use Principle of least privilege

def execute_command(command):
    result = subprocess.run(command, shell=True, capture_output=True)
    return result.stdout


def main():
    display_credentials()

if __name__ == '__main__':
    main()
    #trigger wfkjsdf
