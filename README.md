## Basic Python Web Application with MongoDB and Nginx Reverse Proxy

This is a basic Python web application that serves an HTTP endpoint that returns the client’s IP address and an indication of the last time a request was received from that client IP address. The application makes use of a MongoDB database to record the timestamp of the last HTTP request from each client IP address. The application lives behind a Nginx reverse proxy that forwards all HTTP requests starting with /api/ to the Python backend application. SSL support over TLS 1.2 is enabled in the reverse proxy.

In addition, a simple frontend application using React has been included to display the client IP address and last request time.

The application, database, and reverse proxy are all deployed using Docker Compose.

## Requirements

Docker
Docker Compose

## *Getting Started

Clone this repository to your local machine.

git clone https://github.com/your-username/basic-python-web-application.git

Navigate to the root directory of the project.


cd basic-python-web-application

Build and start the Docker containers.

docker-compose up --build

Once the containers are up and running, you can access the application at https://localhost/api/myip/ in your web browser. You should see the client IP address and the timestamp of the last request, or a message indicating that this is the first request from the client.

To stop the Docker containers, use Ctrl-C to stop the running process.

## Configuration

# Environment Variables

The following environment variables can be set in the .env file:

* MONGO_INITDB_ROOT_USERNAME: The username for the MongoDB database.

* MONGO_INITDB_ROOT_PASSWORD: The password for the MongoDB database.

* MONGO_DB: The name of the MongoDB database to use.

* MONGO_COLLECTION: The name of the MongoDB collection to use.

## Nginx Configuration

The Nginx configuration can be found in the nginx directory. The nginx.conf file contains the SSL configuration for the reverse proxy.

# MongoDB Configuration

The MongoDB configuration can be found in the mongo directory. The mongo-init.js file contains the initialization script for the MongoDB database.

# Testing
To test the application, you can use the following curl command:

[ curl -k https://localhost/api/myip/ ]

This will return the client IP address and the timestamp of the last request, or a message indicating that this is the first request from the client.

# Credits

This application was created by *[THAMISANQA]



