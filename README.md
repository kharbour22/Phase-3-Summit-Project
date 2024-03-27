# Summit Reviews

This project is a simple Python application for managing mountain and review data. It provides functionalities to create, retrieve, update, and delete both mountains and reviews, as well as retrieve reviews associated with a specific mountain.

## Features

-Mountain Management: Users can create, retrieve, update, and delete mountains.

-Review Management: Users can create, retrieve, update, and delete reviews.

-Association: Reviews are associated with specific mountains, allowing users to retrieve reviews for a particular mountain.

-SQLite Database: Data is stored persistently using SQLite, allowing for easy data management.

---

## Installation

Clone the repository:

-git clone https://github.com/kharbour22/python-p3-v2-final-project-templategit

Navigate to the project directory:

-cd mountain-reviews-project

Install dependencies:

pipenv install
pipenv shell

---

## Structure

The project is structured as follows:

models/: Contains Python modules defining the Mountain and Review classes for object-relational mapping (ORM) with the SQLite database.

helpers.py: Provides helper functions for initializing the database, interacting with mountain data, and interacting with review data.

main.py: Main script to run the application and interact with user inputs.

lib/debug.py: Debug script for debugging database interactions using ipdb.

The main entry point of the project is the main.py script. This script provides a command-line interface (CLI) for users to interact with the mountain and review data. Upon running the script, users are presented with a main menu where they can choose to interact with mountain data, review data, or quit the program. The script utilizes helper functions defined in other files to perform CRUD (Create, Read, Update, Delete) operations on mountains and reviews, as well as retrieve reviews associated with specific mountains.

