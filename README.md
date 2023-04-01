My Django App
The bands app is a Django web application designed for metal music enthusiasts to manage their favorite bands. With features like user authentication, registration, and CRUD (Create, Read, Update, Delete) functionality, users can easily add and edit bands to their personal collection. The app provides a simple and intuitive interface for users to manage their metal band preferences and display them in a comprehensive list. Whether you're a fan of classic heavy metal, death metal, or black metal, the bands app is a great tool for organizing and keeping track of your favorite metal bands.

Dependencies
To run this application, you will need Python 3.7 and pip installed on your computer. You can download Python from the official website, and pip should come pre-installed with Python 3.7.

Installation
1. Clone the repository to your local machine
2. Change into the project directory
3. Create a virtual environment and activate it. For example:
	python3.7 -m venv venv
	source venv/bin/activate
4. Install the required packages using pip install -r requirements.txt
5. Run the Django application using python manage.py runserver

Running with Docker
1. Clone the repository to your local machine
2. Change into the project directory
3. Build the Docker image using '''docker build -t my_django_app'''
4. Run the Docker container using docker run -p 8000:8000 my_django_app


