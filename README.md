## Basic Python Web Application with MongoDB and Nginx Reverse Proxy

This is a basic Python web application that serves an HTTP endpoint that returns the client’s IP address and an indication of the last time a request was received from that client IP address. The application makes use of a MongoDB database to record the timestamp of the last HTTP request from each client IP address. The application lives behind a Nginx reverse proxy that forwards all HTTP requests starting with /api/ to the Python backend application. SSL support over TLS 1.2 is enabled in the reverse proxy.

In addition, a simple frontend application using HTML has been included to display the client IP address and last request time.

The application, database, and reverse proxy are all deployed using Docker Compose.

## Requirements

Installation and Setup
To use the application, you will need to have Python and Docker installed on your machine. You will also need to have a MongoDB instance set up with a database and collection for storing IP addresses and timestamps.

To install the Python dependencies for the application, navigate to the root directory of the project and run the following command:


    pip install -r requirements.txt

To set up the application, create a file called .env in the root directory of the project with the following contents:

    CONNECTION_LINK=<your MongoDB connection link here>

Replace <your MongoDB connection link here> with the connection link to your MongoDB instance.REMEMBER TO INCLUDE YOUR PASSWORD AND YOUR USERNAME IS ON THE CONNECTION LINK.


Once you have set up your MongoDB instance and created the .env file, you can start the application using Docker by running the following command:

- docker-compose up

This will start the application and a reverse proxy (Nginx) with SSL support over TLS 1.2 only.

You can access the application by visiting https://localhost in your web browser.


