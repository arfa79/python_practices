#writing a program for getting data from user like name email and password for regidteration
from flask import Flask, jsonify, request
import json

app = Flask(__name__)
@app.route('/register', methods=['POST'])
def register():
    # Get user registration data from the request
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']

    # Load existing user data from the JSON file
    with open('users.json', 'r') as file:
        users = json.load(file)

    # Add new user to the list
    new_user = {'name': name, 'email': email, 'password': password}
    users.append(new_user)

    # Save the updated user data to the JSON file
    with open('users.json', 'w') as file:
        json.dump(users, file)

    return jsonify({'message': 'User registered successfully'})

@app.route('/users', methods=['GET'])
def get_users():
    # Load user data from the JSON file
    with open('users.json', 'r') as file:
        users = json.load(file)

    return jsonify({'users': users})
if __name__ == '__main__':
    app.run(debug=True)