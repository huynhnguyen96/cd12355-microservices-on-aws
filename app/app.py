from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the IP Address and Health Check App!"

@app.route('/ip')
def get_ip():
    ip_address = request.remote_addr
    return jsonify({'ip_address': ip_address})

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

