## prerequisite

Note that you will need to install the pymongo library by running pip install pymongo in your terminal or command prompt

bash :

mkdir myproject
cd myproject


Create a virtual environment for the project using venv.

python3 -m venv env

Activate the virtual environment.

source env/bin/activate

Install the necessary Python packages: flask and pymongo.

pip install Flask pymongo

Finaly Create a new Python file in the project directory I  called mine app.py .


## THE  PYTHON FLASK  WEB APPLICATION USING  

This basic Python web application (app.py) that serves an HTTP endpoint that returns the client’s IP address and an indication of the last time a request was received from that client IP address, and uses MongoDB to store the timestamp of the last HTTP request from each client IP address:


## More information about the code 

We define a new route for /api/myip/. When this endpoint is accessed as instructed , we get the client's IP address using the request.remote_addr property. We then search the ip_addresses collection for a document with the same IP address.

If no document is found, we construct a response message indicating that this is the first message received from the client. We also insert a new document into the ip_addresses collection with the client's IP address and the current timestamp.


---
## MongoDB 

For password-protected database access, you can add a username and password to the MongoDB URI in the Flask app, like I have in the app.py file in and example below. 

client = MongoClient('mongodb://username:password@localhost:27017/')

---
## NGINX

For this Nginx reverse proxy I have created a configuration file running on the same machine as the web applicationn on port XXXX.

You then have to enable the site and reload the Nginx with the below commands. 


* sudo ln -s /etc/nginx/sites-available/myapp.conf /etc/nginx sites-enabled/
* sudo systemctl reload nginx

Install Nginx on your server using the appropriate package manager for your operating system. On Ubuntu(as I am running ubuntu for this prac), you can use the following command:

* sudo apt-get update
* sudo apt-get install nginx

Create a new Nginx configuration file for your Flask application in the /etc/nginx/sites-available/ directory. You can then  name the file anything you like, but it should have a .conf extension. 
For example, you can use the following command to create a file named webapp.conf:

* sudo nano /etc/nginx/sites-available/myapp.conf

In the new configuration file,you then add the code  saved an *ngxin.conf to define a server block for your Flask application:

server {
    listen 80;
    server_name webapp.example.com; # replace with your own domain name

    location /api/ {
        proxy_pass http://127.0.0.1:5000/; # my application was running on this IP feel free to change this on your local machine accordingly 
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
This configuration  tells Nginx to listen on port 80 for requests to your domain name (webapp.example.com in this example), and to forward all requests starting with /api/ to your Flask application running on port 5000. The other headers set by the proxy pass information about the original request to your Flask application
We then create a symbolic link to enable the new configuration file by running the following command:
 
 *sudo ln -s /etc/nginx/sites-available/myapp.conf /etc/nginx/sites-enabled/
You can then test the configuration by running the following command: 

sudo nginx -t

If the output says the below then the configuration is valid.

nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful

Lastly restart Nginx to apply the new configuration by running this last command 

* sudo systemctl restart nginx

Then your flask application can be accessed using

http://webapp.example.com/api/myip/ replace webapp.example.com with your own domain name).

---

## CI PIPELINE

The CI pipeline for this application, uses Jenkins automate the building, testing, and deployment of the application.SAve as **pipeline.Jenkins

##Simple front end

I have created a simple front end html file that uses JavaScript to make an HTTP request to the /api/myip/ endpoint of your Flask app using the Fetch API. It then updates the result element with the response from the Mongoserver.Then, when you visit your Flask app's root URL, it should display the My IP Address page and make a request to your Flask app's /api/myip/ endpoint to retrieve the client's IP address and the last time a request was received from that client IP address.

