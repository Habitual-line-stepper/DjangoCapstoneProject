## Welcome to my Django app!
- [Description](#description)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Running with Docker](#running-with-docker)
- [Usage](#usage)
- [Configuration](#configuration)

# Description: 
The bands app is a Django web application designed for metal music enthusiasts to manage their favorite bands. With features like user authentication, registration, and CRUD (Create, Read, Update, Delete) functionality, users can easily add and edit bands to their personal collection. The app provides a simple and intuitive interface for users to manage their metal band preferences and display them in a comprehensive list. Whether you're a fan of classic heavy metal, death metal, or black metal, the bands app is a great tool for organizing and keeping track of your favorite metal bands.

# Getting Started
- Prerequisites:  
	- ```Python 3.7 or higher``` 
	- ```pip``` 
	- ```virtualenv``` 
	- ```Docker```
# Dependencies:
To run this application, you will need ```Python 3.7``` and pip installed on your computer. You can download Python from the official website, and pip should come pre-installed with ```Python 3.7```.

# Installation:
1. Clone the repository to your local machine
2. Change into the project directory
3. Create a virtual environment and activate it. For example:
	- ```python3.7 -m venv venv```
	- ```source venv/bin/activate```
4. Install the required packages using: 
	- ```pip install -r requirements.txt```
5. Run the Django application using:
	- ```python manage.py runserver```	

# Running with Docker
1. Clone the repository to your local machine
2. Change into the project directory
3. Build the Docker image using: 
	- ```docker build -t my_django_app```
4. Run the Docker container using 
	- ```docker run -p 8000:8000 my_django_app .```
	
# Usage:
- Using venv:
	1. Navigate to the mysite directory  
	2. Start the Django development server by running the following command:  
		- ```python manage.py runserver```  
	3. Open a web browser and navigate to:  
		- ```http://localhost:8000```  
- Using Docker
	1. Navigate to the root directory of the project  
	2. Build the Docker image by running the following command:  
		- ```docker build -t my_django_app . ```   
	3. Start a container by running the following command:  
		- ```docker run -p 8000:8000 my_django_app```  
	4. Open a web browser and navigate to:  
		- ```http://localhost:8000```  

# Configuration:
The following environment variables need to be set for the application to run:  
- SECRET_KEY: the secret key used by Django. You can generate a new key with the following command:    
	- ```python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' ```  
- DATABASE_URL: Database URL 

You can either set these environment variables manually or use a tool like direnv to automatically load them from a .envrc file.  


