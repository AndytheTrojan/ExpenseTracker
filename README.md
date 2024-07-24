# Expense Tracker

## Overview

This is a simple expense tracker application built with Python and Flask. It allows users to add and view their expenses in a web-based interface. Expenses are stored in a CSV file.

## Features

- Add new expenses with details such as date, category, amount, and description.
- View a list of all added expenses.

## Project Structure

- `app.py`: The main Flask application script.
- `static/`: Contains CSS files for styling the application.
- `templates/`: Contains HTML templates.
- `data/expenses.csv`: CSV file with expense records.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd ExpenseTracker
    ```

2. Install Flask:

    ```bash
    pip install Flask
    ```

### Running the Application

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the Expense Tracker.

### Usage

- Use the form on the homepage to add new expenses.
- The expenses will be displayed in a table below the form.

### CSV File

The `data/expenses.csv` file contains sample expense records. You can add new records using the web interface, and they will be saved to this file.

