import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_data.csv")
df = load_data()

st.title("🚗 Car Resale Data Visualizer & Insights Dashboard")
st.divider()
st.header("📊 Visual Exploration of Car Resale Dataset",divider="rainbow")
st.markdown("Explore trends in car brands, pricing, safety ratings, and engine power using interactive visuals.")
theme = st.radio("🎨 Choose Display Theme", ["Light", "Dark"], horizontal=True)
sns.set_theme(style="darkgrid" if theme == "Dark" else "whitegrid")
sec_1,sec_2=st.columns([2,1])
sec_3,sec_4=st.columns([2,1])
with sec_1:
    figure_1=plt.figure(figsize=(9,5))
    sns.histplot(data=df,x="Brand",kde=True)
    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.xlabel("Brand Names")
    plt.ylabel("No. Of Cars Sold")
    st.pyplot(figure_1)
with sec_2:
    figure_2=plt.figure(figsize=(5,5.65))
    sns.countplot(data=df,y="symboling",hue="No. of doors")
    plt.ylabel("Symboling")
    st.pyplot(figure_2)
with sec_3:
    figure_3=plt.figure(figsize=(9,5))
    sns.barplot(data=df,x="Brand",y="price")
    plt.xlabel("Brand Names")
    plt.ylabel("Price")
    plt.xticks(rotation=60)
    st.pyplot(figure_3)
with sec_4:
    figure_4=plt.figure(figsize=(5,6.9))
    sns.lineplot(data=df,x="horsepower",y="price")
    plt.xlabel("Horse Power of Car")
    plt.ylabel("Price Of Car")
    st.pyplot(figure_4)

st.divider()
# st.header("Analytical Observations On Graphs",divider="rainbow")

#st.info("- Most Cars Which came for resale are from Toyota Brand\n- Jaguar has highset mean resale price followed up by Buick and then porsche\n- Buick had shown the maximum Resale Price\n- Four Door Cars Are common and most cars are rate as symboling 0 showing that they have minmal damages but totally safe to use\n- Linear Relation between horsepower and their price with many outliers ")
st.subheader("🔍 Key Insights from the Visuals")

st.markdown("""
- 🚗 **Toyota dominates the automobile market**, likely due to its affordability, reliability, and brand popularity.
- 💰 **Jaguar, Porsche, and Buick** command significantly higher average prices — indicating luxury status or higher feature sets.
- 🚪 **Four-door cars** are more common, hinting at consumer preference for family or practical vehicles.
- ⚠️ Most vehicles are rated **symboling 0**, suggesting they are **structurally safe** .
- 📈 There's a **clear upward trend** between **horsepower and price**, although **many outliers** exist — likely due to brand or condition.
""")

with st.expander("See Detailed Analysis"):
    st.markdown("""
The data visualizations above help us uncover important patterns in the car resale market:

1. **Brand Popularity**  
- The histogram shows that **Toyota** is by far the most commonly resold brand.  
- This indicates strong customer trust and high resale turnover.  
- Brands like **Jaguar** or **Porsche**, while less frequent, command a much higher price.

2. **Symboling vs. No. of Doors**  
- Most cars have **four doors**, showing a buyer preference for family or practical cars.  
- Cars rated with a **symboling of 0** are the most frequent — suggesting these cars are perceived as **safe and low-risk**.

3. **Average Price by Brand**  
- **Luxury brands** like Jaguar, Buick, and Porsche show a much higher **mean price**.  
- This reflects their premium features, brand value, and possibly better maintenance.

4. **Horsepower vs. Price Relationship**  
- A **strong linear trend** is visible between **horsepower and price**.  
- Cars with more power are generally more expensive, but some **outliers** exist — possibly due to old models or brand reputation.

5. **Outliers and Variations**  
- While the trends are clear, some brands/models break the pattern.  
- These may be rare cases like vintage cars, poorly maintained vehicles, or high-performance models with niche appeal.

### 🧠 Business Takeaway:
- **Sellers** may want to focus on reliable, popular brands like Toyota for fast turnover.
- **Luxury brands**, though fewer in number, offer **higher profit margins**.
- Buyers concerned with safety and family needs tend to prefer four-door, low-symboling cars.
""")
    
st.divider()
st.success("✅ End of Visual Analysis — Now Head Over to the Prediction Tab to Try the Model!")
