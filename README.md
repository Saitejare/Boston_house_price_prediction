# 🏠 Boston House Price Prediction using Machine Learning

A web-based Machine Learning application that predicts Boston house prices using a trained **Gradient Boosting Regressor** model. The application features a modern and responsive user interface built with **HTML, CSS, JavaScript**, and a **Flask** backend for real-time price prediction.

---

## 📖 Project Overview

The objective of this project is to estimate the median value of owner-occupied homes in Boston based on various housing attributes. Users can enter property details through an intuitive web interface, and the trained machine learning model predicts the estimated house price instantly.

This project demonstrates the complete Machine Learning workflow, including:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Model training
- Model evaluation
- Model serialization using Pickle
- Flask web deployment
- Interactive frontend development

---

## 🚀 Features

- 🏡 Predict Boston house prices instantly
- 📊 Gradient Boosting Regressor model
- 🎨 Modern responsive user interface
- ⚡ Fast predictions using Flask
- 📱 Mobile-friendly design
- 🔄 Real-time prediction without page reload
- 💻 Clean and professional project structure

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- NumPy
- Pandas

### Data Visualization
- Matplotlib
- Seaborn

### Backend
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### Model Serialization
- Pickle

---

## 📂 Project Structure

```
Boston-House-Price-Prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── boston_house_prices_prediction.ipynb
│
├── data_set/
│   └── boston_housing_prices.csv
│
├── src/
│   └── final_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
└── .gitignore
```

---

## 📊 Input Features

The prediction model uses the following 13 housing attributes:

| Feature | Description |
|----------|-------------|
| CRIM | Crime rate by town |
| ZN | Residential land zoned for lots |
| INDUS | Non-retail business acres |
| CHAS | Charles River dummy variable |
| NOX | Nitric oxide concentration |
| RM | Average number of rooms |
| AGE | Proportion of owner-occupied units built before 1940 |
| DIS | Distance to employment centres |
| RAD | Accessibility to radial highways |
| TAX | Property tax rate |
| PTRATIO | Pupil-teacher ratio |
| B | Black population index |
| LSTAT | Percentage of lower status population |

---

## 🤖 Machine Learning Workflow

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Selection
      │
      ▼
Train-Test Split
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Serialization (.pkl)
      │
      ▼
Flask Deployment
      │
      ▼
Prediction
```

---

## 📈 Model Information

**Algorithm Used**

- Gradient Boosting Regressor

The trained model is saved as:

```
src/final_model.pkl
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Boston-House-Price-Prediction.git
```

### Move into the project directory

```bash
cd Boston-House-Price-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 💻 User Interface

The application includes:

- Professional landing page
- Interactive input form
- Responsive layout
- Beautiful prediction result card
- Instant machine learning predictions

---

## 📷 Screenshots

### Home Page

> Add a screenshot of your application's home page here.

### Prediction Result

> Add a screenshot showing the prediction result.

---

## 📌 Future Enhancements

- Deploy on Render or Railway
- House price visualization charts
- Prediction history
- User authentication
- PDF report generation
- Dark mode
- REST API support
- Interactive dashboard

---

## 📚 Learning Outcomes

This project helped in understanding:

- Data preprocessing techniques
- Machine Learning model training
- Model evaluation metrics
- Model deployment using Flask
- Frontend-backend integration
- Web application development
- RESTful request handling

---

## 👨‍💻 Author

**Kurapati Sai Teja**

B.Tech – Artificial Intelligence and Machine Learning

Lendi Institute of Engineering and Technology

---

## ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates future improvements.

---

## 📄 License

This project is intended for educational and learning purposes.
