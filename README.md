Online Library Project

Introduction:

The Online Library Project is a web application that aims to provide users with a user-friendly interface for exploring books, viewing books by category, creating user accounts, and downloading books. It is built using the Django framework, incorporating models, serializer structures, views, and URL structures. Additionally, Django's admin interface is utilized for efficient database management.

Project Structure:

The project follows the basic structure outlined below:

models.py: Database models and relationships
serializers.py: Serializer classes converting model data to JSON format
views.py: View functions responding to HTTP requests
urls.py: URL redirections and connections to view functions
admin.py: Model registrations for the Django admin interface
api.py: Router and view sets defining the REST API
Django Models and Serializer Structure:

Book Model: A model containing basic information about books.
Category Model: A model representing book categories.
User Model: A model representing registered users.
AuthToken Model: A model representing user authentication tokens.
Serializer Classes: Serializer classes for each model, used to convert model data to JSON format.
Django Views and URLs Structure:

Book List and Details: Views for listing all books and displaying details for a specific book.
Books by Category: A view for listing books belonging to a specific category.
User Operations: Views managing user registration, login, logout, and password change operations.
Book Download: A view managing the book download operation.
API Operations: Views managing operations related to REST API endpoints.
Django Admin Interface:

Admin Panel: Database management and user account control through the Django admin interface.
Django REST Framework Token Authentication:

Token Authentication: Token authentication is implemented using 'rest_framework.authtoken' to create and use user authentication tokens.
PostgreSQL Database:

Database: A PostgreSQL database is used to securely and efficiently store data.
API Testing and Postman:

Postman: Postman is used for API testing to ensure each URL endpoint produces the expected results.
Front-End API Connections:

API Links: Front-end API connections are established for each function, ensuring a user-friendly interface with integrated APIs.
Router and Register Method:

Router: A router is used for the automatic creation of APIs based on book genres. A unique algorithm is integrated to assign unique IDs for each category and book.
Conclusion:

Success Evaluation: The project successfully delivers an online library experience using the Django framework and REST API.

Lessons Learned: In-depth understanding is gained in using Django models, serializer structures, views, and REST API usage.

Future Developments: Future enhancements may include features such as favorite book lists, user comments, aiming to increase user interaction with the project.
