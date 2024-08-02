# Project Name

**Brief Description:** This project is an electronic shop management system built using Flask as the backend framework. It provides functionalities for managing users, staff, products, categories, orders, and payments. The application is designed to facilitate the management of an electronic shop, allowing for seamless operations and efficient customer management.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project aims to provide a robust electronic shop management system. The backend is built using Flask, and it includes various endpoints for managing users, staff, products, categories, orders, and payments. The system is designed to be scalable and easy to extend, allowing for the integration of additional features as needed.

## Features

- **User Management:** 
  - Register and login functionality for customers and staff.
  - Role-based access control for admin and customer roles.

- **Staff Management:**
  - CRUD operations for managing staff members.

- **Product Management:**
  - CRUD operations for managing products and categories.
  - Search and filter products by category.

- **Order Management:**
  - Create, update, and delete orders.
  - Manage order items and track order status.

- **Payment Processing:**
  - Handle payments with different methods.
  - Track payment status and transaction details.

## Installation

Follow these steps to install and set up the project locally.

### Prerequisites

- **Python 3.8+**
- **PostgreSQL**
- **pipenv** (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/Moringa-SDF-PTO5/phase-5-project-group-2
cd phase-5-project-group-2

### Backend (Flask API)

- Instructions for setting up the Flask backend, including using pipenv.

```bash
cd server
pipenv install
pipenv shell
```

### Frontend (React with Vite)

- Instructions for setting up the React frontend, including using npm or yarn.

```bash
cd client
npm install
```

## Usage

Provide examples or instructions on how to use your project. Include any configuration settings or environment variables that need to be set.

### Running Tests

Explain how to run tests for both backend and frontend.

```bash
# Backend tests
cd server
pipenv run pytest

# Frontend tests
cd client
npm test
```

## Contributing

Contributions are welcome! To contribute:

Fork the repository.
Create a new branch.
Make your changes.
Submit a pull request with a detailed description of your changes

## License

This project is licensed under the MIT License.

Copyright 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE

