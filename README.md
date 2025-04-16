# Simple Flask Blog Portfolio
This is a simple blog application built with Flask, SQLAlchemy, and Jinja2. It allows users to create, view, and delete posts. The project demonstrates the use of Flask for web development and SQLAlchemy for managing a simple SQLite database.

# Features:
Create Posts: Add blog posts with a title and content.

View Posts: Display all posts with their titles, content, and publication date in a clean and minimalistic layout.

Delete Posts: Securely delete posts after confirming the action by typing "DELETE".

Formatted Dates: Display dates in the Brazilian timezone (UTC-3), formatted for better readability.

Minimalistic Design: Clean, modern, and simple design using custom CSS.

# Installation Instructions:
Clone the repository:

bash
Copy
Edit
git clone https://github.com/sh4wty1/flask-blog-portfolio.git
Navigate into the project directory:

bash
Copy
Edit
cd flask-blog-portfolio
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy
Edit
venv\Scripts\activate
On Mac/Linux:

bash
Copy
Edit
source venv/bin/activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python app.py
Open your browser and visit http://127.0.0.1:5000/ to view the blog.

# Technologies Used:
Flask: Web framework for building the app.

SQLAlchemy: ORM for database management.

Jinja2: Template engine for rendering HTML pages.

SQLite: Lightweight relational database for storing posts.

# Status:
This project is currently under development. Features and improvements are still being added.
