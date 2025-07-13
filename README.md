# 🚗 Car Price Predictor

Welcome to the **Car Price Predictor Web App**!  
This interactive Streamlit app estimates the market value of a car based on key features like brand, fuel type, engine size, and more.

> **Note:** This is a personal learning project and is not suitable for real-world commercial use.

---

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ghoshank__Gupta-blue?logo=linkedin)](https://www.linkedin.com/in/ghoshank-gupta)  
[![Kaggle](https://img.shields.io/badge/Kaggle-Ghoshank__Gupta-blue?logo=kaggle)](https://www.kaggle.com/ghoshank)

---

## 📌 Problem Statement

A Chinese automobile company **Geely Auto** is planning to enter the US market and wants to understand the factors affecting car prices.  
To do so, they’ve partnered with a consulting firm that gathered data on various car models sold in the American market.

---

## 🎯 Business Objective

- Identify significant variables that influence the price of a car.
- Build a predictive model that estimates the resale value of cars using those variables.
- Help business teams understand pricing dynamics in a new market for better strategy and design decisions.

---

## 🛠️ Technologies Used

- Python (Pandas, NumPy, Scikit-learn)
- Streamlit (for building the web app)
- Matplotlib & Seaborn (for data visualization)
- GridSearchCV (for hyperparameter tuning)
- Joblib (for model serialization)

---

## 🚀 Key Features

- 📊 **EDA & Visualization** of dataset insights
- 🤖 **Random Forest Regressor** as the main model
- 🔍 **GridSearchCV** used for hyperparameter optimization
- 🧾 **Interactive Streamlit Form** for collecting car specs
- 🧠 **Prediction Output** based on selected features
- 📚 **Input Glossary** with brief definitions
- ✨ Clean UI layout using `st.columns` for better UX

---

## 📈 Dataset Info

- **Source**: [Kaggle – Car Price Prediction Dataset](https://www.kaggle.com/datasets/hellbuoy/car-price-prediction)
- The dataset contains various features such as:
  - Brand, Model, Car Body Type
  - Fuel Type, Engine Location, Drive Wheel
  - Technical specs like horsepower, mileage, compression ratio, etc.
- **Target variable**: `price` (price of the car)

---

## ▶️ Running the App Locally

1. **Clone the Repository**
   ```bash
    git clone https://github.com/Ghoshank-codes/Car_Price_Predictor.git
    cd Car_Price_Predictor
2. **Create and Activate Virtual Environment**
   ```bash
    python -m venv venv
    venv/Scripts/activate      # On Windows
    source venv/bin/activate   # On macOS/Linux
3. **Install Requirements**
   ```bash
    pip install -r requirements.txt
4. **Run the Streamlit App**
   ```bash
    streamlit run app/Home.py


## 👨‍💻 Author
**Ghoshank**
> [📎 Linkedin](https://www.linkedin.com/in/ghoshankghoshank/)  
> [📊 Kaggel](https://www.kaggle.com/Ghoshank)

## ⚠️ Disclaimer

This is a **version 1.0 prototype** made strictly for **educational purposes**.

In future versions, I plan to simplify the form and only ask for **essential features**, making it easier for users to get predictions without needing every technical car detail.

> 🚫 Do not rely on this model for real-world financial or business decisions.
