#!/bin/bash

# Start Nginx
nginx

# Start the Flask app using gunicorn
gunicorn --bind 0.0.0.0:5000 wsgi:app
