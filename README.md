# Flask Contact-Manager-API



## Description

The Flask Portfolio API is a project that implements a Flask API for a portfolio management system. It provides functionality for managing a contact list, allowing users to perform CRUD (Create, Read, Update, Delete) operations on contacts. The contact information includes fields such as username, name, lastname, phone number, email, and address.

The API is built using the Flask framework, a popular Python web framework known for its simplicity and flexibility. It utilizes the Flask_SQLAlchemy extension to interact with a SQLite database for storing contact data. SQLite is a lightweight, serverless database that requires no additional setup, making it ideal for small-scale applications.

Following RESTful architecture principles, the API exposes several endpoints for different operations:

- `GET /`: Displays the homepage, which is a basic HTML template.
- `POST /main`: Creates a new contact with the provided information.
- `GET /main`: Retrieves contacts based on query parameters such as username, name, lastname, phone, email, and address.
- `PUT /main/<contact_id>`: Updates an existing contact identified by the provided contact ID.
- `DELETE /main/<contact_id>`: Deletes an existing contact identified by the provided contact ID.

These endpoints handle incoming requests, validate input data, interact with the SQLite database using SQLAlchemy, and return appropriate responses in JSON format.

## Deployment

The Flask Portfolio API is deployed on PythonAnywhere and can be accessed using the following URL:

[https://nikaalaverdashvili.pythonanywhere.com/](https://nikaalaverdashvili.pythonanywhere.com/)

Feel free to visit the deployed API and interact with it using API testing tools like Postman. However, please note that this API is for demonstration purposes only and does not implement authentication or authorization mechanisms.

## Project Structure

The project structure includes the following files:

- `app.py`: The main Flask application file containing the API endpoints and database configuration.
- `templates/index.html`: A simple HTML template for the API homepage.

## Manipulation_Result_Screens



In the `Manipulation_Result_Screens` directory, you can find screenshots showcasing the results of various operations performed on the Flask Portfolio API. These screenshots provide visual representations of how the API handles different CRUD operations on the contact list.

Please refer to the images in the `Manipulation_Result_Screens` directory to see the expected results when interacting with the API.

