# Tour Planner Yogyakarta

## A

## B

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
