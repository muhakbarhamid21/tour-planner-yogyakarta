# Tour Planner Yogyakarta

<div align="center">
  <img src="https://github.com/user-attachments/assets/78d0e55e-45ad-4fc6-9b4b-938ffdda24db" alt="logo-text-bottom" width="300"/>
</div>

Tour Planner Yogyakarta is a web-based decision support system (DSS) that helps tourists find the best tourist destinations in Yogyakarta based on user preferences using the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) method. The system allows users to rank destinations based on criteria like distance, entrance fee, rating, and available facilities.

## Features

1. User Authentication:
   - Secure login and logout system using JSON Web Tokens (JWT).
2. Tourist Spot Recommendations:
   - Use the TOPSIS method to recommend destinations based on user preferences for distance, entrance fee, rating, and facilities.
   - Categories of tourist spots include Culture & History, Education & Learning, Nature & Recreation, and Adventure.
3. Preference Weighting:
   - Users can input their preferences and assign weights to different criteria (distance, price, rating, facilities).
   - Criteria are marked as either cost (lower is better) or benefit (higher is better).
   - Input validation ensures that the sum of all weights does not exceed 100.
4. Tourist Spot Management (CRUD):
   - User can add, edit, and delete tourist destinations.
5. Distance Estimation:
   - The system estimates the user's distance from various tourist spots to assist in decision-making.
6. Interactive User Interface:
   - Built using Flask (Python) for backend processing and Bootstrap for frontend design.

## System Architecture

- Frontend: HTML, CSS, JavaScript, Bootstrap.
- Backend: Python (Flask).
- Database: PostgreSQL.
- Authentication: JWT (JSON Web Tokens).

## Architecture System

```plaintext
.
├── README.md
├── api
│   ├── __init__.py
│   ├── auth
│   │   ├── forgot-password.py
│   │   ├── login.py
│   │   └── regis.py
│   └── services
│       └── analyst.py
├── app
│   ├── __init__.py
│   ├── _admin
│   │   ├── routes.py
│   │   └── services.py
│   ├── _guest
│   │   ├── routes.py
│   │   └── services.py
│   ├── _user
│   │   ├── routes.py
│   │   └── service.py
│   ├── dss
│   │   ├── routes.py
│   │   └── services.py
│   └── models.py
├── config.py
├── core
│   └── database.py
├── middleware
│   ├── auth.py
│   └── exception.py
├── migrations
│   └── versions
│       ├── migration_files.py
├── static
│   ├── assets
│   │   ├── css
│   │   ├── fonts
│   │   └── images
│   ├── js
│   └── scss
├── templates
│   ├── _admin
│   ├── _guest
│   ├── _user
│   ├── accounts
│   └── layouts
├── tourist-destination.csv
├── utils
│   ├── jwt.py
│   └── topsis.py
└── run.py
```

## Installation

Follow these steps to install and run the application locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tour-planner-yogyakarta.git
cd tour-planner-yogyakarta
```

### 2. Create and Activate a Virtual Environment (Optional)

It is recommended to create a virtual environment to isolate the project dependencies.

```bash
python -m venv env
```

Activate the virtual environment:

- On macOS/Linux:

  ```bash
  source env/bin/activate
  ```

- On Windows:

  ```bash
  .\env\Scripts\activate
  ```

### 3. Install the Dependencies

Make sure you have the required libraries installed by running:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install Flask:

```bash
pip install Flask
```

### 4. Set Environment Variables (Optional)

For development purposes, set the Flask app environment variables:

- On macOS/Linux:

  ```bash
  export FLASK_APP=run.py
  export FLASK_ENV=development
  ```

- On Windows:

  ```bash
  set FLASK_APP=run.py
  set FLASK_ENV=development
  ```

### 5. Run the Application

Once everything is set up, you can run the application using the following command:

```bash
flask run
```

By default, the app will be available at: `<http://127.0.0.1:5000/>`

### 6. Deactivating the Virtual Environment (Optional)

To deactivate the virtual environment after you're done:

```bash
deactivate
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://pages.github.com/) file for details.
