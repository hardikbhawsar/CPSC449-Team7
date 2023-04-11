# **CPSC 449 Web Backend Project (Team 7) README**

## **Group Member Details:**
- Member 1: Hardik Bhwsar (885191064) (hardik_bhawsar@csu.fullerton.edu)
- Member 2: Yathartha Patankar (885189803) (yatharthapatankar@csu.fullerton.edu)

## **Introduction:**
Building a robust API is an essential component of modern software development. RESTful APIs have become the industry standard for enabling communication between applications, and the ability to create reliable APIs is a highly sought-after skill in today's tech industry. This project aims to provide developers with hands-on experience in building a RESTful API using Flask, a powerful Python web framework. By building an API that covers error handling, authentication, and file handling, developers will gain a deeper understanding of the complexities involved in creating a reliable and secure API. This project also includes creating a virtual environment and connecting the Flask application to a database, adding to the developer's toolkit of essential skills. Upon completion of this project, developers will have a foundational understanding of building RESTful APIs using Flask, which they can further expand upon to meet their future API development needs.

## **Objective:**
The objective of this project is to build a RESTful API using Flask that covers error handling, authentication, and file handling. The API will have both public and protected admin routes, where the former can be accessed without authentication, and the latter will require authentication. The API will allow users to upload files, validate them for file types and sizes, and store them in a secure location. The project aims to help users understand how to build a robust API that can handle errors, authenticate users, and handle file uploads.

## **Prerequisites:**
- Python 3.x installed on the system.

- Virtual environment package installed (can be installed using "pip install virtualenv"). 

- From src.database import db 

- To initialise database, we have to enter into the interactive shell of flask. 
Command flask shell 
db.create_all()

- MySQL installed and running

- Flask package installed (can be installed using "pip install flask")

- Flask-JWT-Extended package installed (can be installed using "pip install flask-jwt-extended")

- Flask-MySQLdb package installed (can be installed using "pip install flask-mysqldb")

- Postman or a similar tool to test the API endpoints

The requirements for the project are listed in the requirements.txt file, which can be used to install the necessary packages. It is recommended to use a virtual environment to manage the packages and dependencies of the application. The README file included in the Git repository provides more detailed instructions on how to set up the environment and install the required packages.



## **Installation:**
To install the project, follow these steps:

### **Using CMD:**
**Step 1:** Clone the Git repository to your local machine.

**Step 2:** Create a virtual environment for the application using the command "python -m venv env". Activate the virtual environment using the command "source env/bin/activate" (for Linux/Mac) or "env\Scripts\activate" (for Windows).

**Step 3:** Install the necessary packages using the command "pip install -r requirements.txt".

**Step 4:** Create a MySQL database and configure the Flask application to connect to it by updating the database URL in the configuration file.

**Step 5:** Run the Flask application using the command "flask run".



## **Additional Information:**
The team members who worked on this project are listed in the README file.
The API uses JWT authentication to ensure that protected endpoints can only be accessed with a valid token.
File uploads are validated for file types and sizes and are stored in a secure location.
Error handling is implemented throughout the API to ensure proper error messages and status codes are returned.
A public route is also included that allows users to view public information without authentication.
The endpoints and their functionality are documented in the README file and can be tested using Postman or a similar tool.
The code is written in Python and uses the Flask web framework to create the API.