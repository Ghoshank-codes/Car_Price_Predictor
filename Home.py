import streamlit as st


st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="wide")
st.title("🚗 Welcome to Car Price Predictor")
st.subheader("Empowering Geely Auto to understand U.S. car market pricing dynamics")

st.markdown("""
---
### 📌 **Project Background**
Geely Auto, a prominent Chinese automobile manufacturer, plans to enter the **U.S. automotive market**.  
To succeed, they’ve partnered with a consulting firm to explore:

- 🔍 **Which car features significantly influence the price?**
- 📈 **How well can we predict a car's price using those features?**

This web app demonstrates a **machine learning-based price prediction model** trained on a wide dataset of car listings.

---
### 🎯 **Business Goal**
The goal is to **model car prices based on specifications** like body type, engine size, horsepower, mileage, and more.

With this tool, Geely aims to:
- Understand **pricing patterns**
- Strategize feature offerings for the U.S. market
- Offer **competitive pricing** with optimal configurations

> ⚠️ **Note**: This tool is for **educational and demonstration purposes only.**  
> It's not production-grade and shouldn't be used for real-world pricing decisions.

---
### 🧪 **Current Version**
You're viewing the **first working version** of this application.  
I'm actively improving it to:

- Simplify inputs — only a few **key features** will be needed in future updates
- Enhance the model's performance & robustness
- Make predictions more intuitive and transparent

---
### 📊 **Explore the App**
- 🔍 Visit **Model Overview** to learn how the model was built
- 🧮 Try the **Prediction Tool** to estimate sale prices
- 📚 Learn about each feature via tooltips and glossaries
- 💬 Feedback & feature suggestions are welcome!

---
### 🔗 **Dataset Source**
- This project is based on the open dataset from Kaggle:  
    [Car Price Prediction Dataset](https://www.kaggle.com/datasets/hellbuoy/car-price-prediction)

---
""")


st.markdown("Made with ❤️ by Ghoshank — ML Enthusiast | For academic use only.")
st.markdown("---")
st.markdown("### 🔗 Connect & Explore More")

st.markdown("Stay connected and explore my work on these platforms:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div style='text-align: center;'>💻<br><a href='https://github.com/Ghoshank-codes' target='_blank'><strong>GitHub</strong></a></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div style='text-align: center;'>📊<br><a href='https://www.kaggle.com/Ghoshank' target='_blank'><strong>Kaggle</strong></a></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div style='text-align: center;'>💼<br><a href='https://www.linkedin.com/in/ghoshankghoshank/' target='_blank'><strong>LinkedIn</strong></a></div>", unsafe_allow_html=True)


