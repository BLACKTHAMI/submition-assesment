
from flask import Flask, request,jsonify
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
import datetime

app = Flask(__name__)

# connect to MongoDB database with password and username included on the connection link
url_link = os.environ.get("CONNETION_LINK")
client = MongoClient('url_link')
db = client['mydb']
ip_collection = db['ip']

# Define endpoint for /api/myip/ S0gc5RzjFsnN3uG6

@app.route('/api/myip/')
def myip():
    # Get client IP address
    client_ip = request.remote_addr
    # Check if IP is already in database
    last_request = ip_collection.find_one({'ip': client_ip})
    print(client_ip)
    if not last_request:
            timestamp = datetime.datetime.now()
            print(timestamp)
            ip_collection.insert_one({'ip': client_ip, 'timestamp': timestamp})

            message = f"Your client's IP address is: {client_ip}. Your previous/last request was on {timestamp}."

    else:
            message = f"Your client's IP address is: {client_ip}. This is the first message received from your client."
            ip_collection.insert_one({'ip_address': client_ip, 'timestamp': datetime.utcnow()})

    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True)
