# 🏡 Bangalore House Price Prediction

A simple machine learning web application built with **Flask** to predict house prices in Bangalore. The model takes inputs like location, square footage, number of bathrooms, and BHKs to estimate the price of a house. This app runs locally in your browser.

## 🚀 Features

- Predict house prices in Bangalore based on input parameters
- Clean and simple UI built using HTML/CSS (and optionally Bootstrap)
- Local Flask server for running predictions
- Trained ML model (e.g., Linear Regression)
- Location filtering and user-friendly dropdowns

## 🖥️ Tech Stack

- Python
- Flask
- scikit-learn, Matplotlib
- Pandas, NumPy
- HTML/CSS (optionally with Bootstrap)
- JavaScript (optional for interactivity)


## ⚙️ How to Run the Project Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/rajmachawal-py/Bangalore-House-Price-Prediction.git
   cd Bangalore-House-Price-Prediction

   
2. **Run the Flask Application**
   ```bash
   python server.py

3. <pre> BHP/ ├── client/ │ ├── app.css # Styling for the front-end │ ├── app.html # HTML structure of the front-end │ └── app.js # JavaScript logic for the front-end │ ├── model/ │ ├── Banglore_home_prices_model.pickle # Trained ML model │ ├── Bengaluru_House_Data.csv # Dataset used for training │ ├── Machine Learning Project 1.ipynb # Jupyter notebook for EDA and model building │ └── columns.json # JSON file containing model input features │ ├── server/ │ ├── __pycache__/ # Python cache directory │ ├── artifacts/ # Folder to store model artifacts │ ├── server.py # Backend API using Flask │ └── util.py # Utility functions for preprocessing/prediction │ └── README.md # Project documentation </pre>

