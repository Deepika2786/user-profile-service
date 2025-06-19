from flask import Flask, request, jsonify

app = Flask(__name__)

# In a real app, this would be a database
users_db = {
    "user1": {"name": "Alice", "email": "alice@example.com", "profile_pic": "http://example.com/alice.jpg"},
    "user2": {"name": "Bob", "email": "bob@example.com", "profile_pic": "http://example.com/bob.jpg"}
}

@app.route('/')
def home():
    return "User Profile Service is running!"

@app.route('/users/<user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = users_db.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user_profile():
    data = request.json
    if not data or 'user_id' not in data or 'name' not in data:
        return jsonify({"error": "Missing user_id or name"}), 400

    user_id = data['user_id']
    if user_id in users_db:
        return jsonify({"error": "User already exists"}), 409

    users_db[user_id] = {
        "name": data['name'],
        "email": data.get('email', ''),
        "profile_pic": data.get('profile_pic', '')
    }
    return jsonify({"message": "User created", "user_id": user_id}), 201

# --- Intentional Vulnerability for DAST Demo (XSS) ---
@app.route('/greet', methods=['GET'])
def greet_user():
    name = request.args.get('name', 'Guest')
    # This is vulnerable to XSS! DAST will find this.
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)