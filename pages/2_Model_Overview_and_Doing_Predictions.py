import streamlit as st
import pandas as pd
import joblib
import sys
import os
from sklearn import set_config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.preprocessor_and_predictor_ import LabelMapper
st.set_page_config(layout="wide")
@st.cache_data
def load_data():
    try:
        return pd.read_csv("data/cleaned_data.csv")
    except FileNotFoundError:
        st.error("❌ Data file not found. Make sure 'data/cleaned_data.csv' exists.")
        return pd.DataFrame()
    
df = load_data()

@st.cache_resource
def load_model():
    return joblib.load("models/prediction_model.pkl")

model = load_model()    
brand_model_map = df.groupby("Brand")["Model"].unique().to_dict()

st.title("Model Overview 🤖 and Doing Predictions")
st.header("Model Overview 👨‍🏫",divider="red")
st.subheader("Model Selected ")
st.markdown("""
For this regression task, I experimented with various models such as **Linear Regression**, **Ridge**, **Lasso**, **ElasticNet**, **K-Nearest Neighbors**, and **Decision Tree Regressor**.

Among all, **Random Forest Regressor** stood out — delivering strong performance, especially in the presence of **outliers**. It handled the complexity of the dataset well and offered superior accuracy compared to others.

Although **Decision Tree** also showed promising results, **Random Forest** consistently performed better due to its ensemble nature and reduced variance.

Once I selected Random Forest, I fine-tuned it using **GridSearchCV**, a technique that exhaustively searches for the best hyperparameters. 

You might ask:  
💭 *"If the default Random Forest was already performing well (with R² ≈ 0.96), why bother with tuning?"*

That’s a valid question. Interestingly, the model trained with the **best parameters from GridSearchCV** gave an R² of ~0.94 — slightly lower.

Does that mean the default model is better?  
Not necessarily.

- **Higher R² doesn’t always guarantee generalizability.**
- The tuned model might be more **robust** on unseen data.
- GridSearchCV helped me find a **more stable** solution by considering a broader hyperparameter space.

So, tuning wasn’t just about increasing scores — it was about building a **more reliable and generalized model**.
""")

st.divider()
st.subheader("Why I Used GridSearchCV 🔍")

st.markdown("""
I used GridSearchCV to find the **optimal combination of hyperparameters** that would help my model generalize well.

Even though my default Random Forest performed very well, tuning it with GridSearchCV allowed me to:

- 🧪 **Cross-validate performance** across multiple folds  
- ⚙️ **Control overfitting** by testing different tree depths, number of estimators, etc.  
- 🔍 **Ensure robustness**, especially for future or unseen data  
- 📊 Make **data-driven decisions** instead of relying on defaults

It was a trade-off between **accuracy** and **generalization** — and GridSearchCV helped me strike the right balance.
""")

with st.expander("🔍 See Full Pipeline CodeFlow"):
    set_config(display='diagram')
    st.write(model)

st.divider()
st.header("So now , lets start predicting some prices with Our Blast Model")

Brand = st.selectbox("Select Brand", sorted(brand_model_map.keys()))
available_models = list(brand_model_map[Brand])
Model=st.selectbox("Model Of Car",sorted(available_models))

with st.form("car_prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"**Selected Brand:** `{Brand}`")
        st.markdown(f"**Selected Model:** `{Model}`")
        Carbody=st.selectbox("Car Body Type",df["carbody"].unique())
        FuelType=st.selectbox("Fuel Type Of Car",df["fueltype"].unique())
        Aspiration=st.selectbox("Aspiration Of Car",df["aspiration"].unique())
        DriveWheel=st.selectbox("Drive Wheel",df["drivewheel"].unique())
        EngineLocation=st.selectbox("Location Of Engine",df["enginelocation"].unique())
        EngineType=st.selectbox("Engine Type of Car",df["enginetype"].unique())
        FuelSys=st.selectbox("Fuel System in Car",df["fuelsystem"].unique())
    with col2:
        Symboling=st.number_input("Symboling (-3 means safe to 3 unsafe)",min_value=-3,max_value=3,value=0,step=1)
        WheelBase=st.slider("Wheel Base measurement",min_value=86.60,max_value=120.00,value=96.5,step=0.1)
        CarLength=st.slider("Length of Car ",min_value=140.00,max_value=205.00,value=173.1,step=0.1)
        CarWidth=st.slider("Width Of Car",min_value=61.00,max_value=73.00,value=65.5,step=0.1)
        CarHeight=st.slider("Hieght Of Car :",min_value=47.00,max_value=60.00,step=0.1,value=54.00)
        CurbWieght=st.slider("Curb Wieght",min_value=1815.0,max_value=4200.0,step=0.1,value=2400.00)
        EngSize=st.slider("Size Of Engine",max_value=340.0,min_value=70.0,step=0.1,value=120.0)
        BorRatio=st.slider("Bor Ratio ",min_value=2.00,max_value=4.00,step=0.03,value=3.3)
    with col3:
        DoorNo=st.radio("No. Of Doors",[4,2])
        CylNo=st.selectbox("No. Of Cylinders",[ 4,  6,  5,  2, 12,  8])
        Stroke=st.slider("Stroke",min_value=2.0,max_value=4.3,value=3.0,step=0.01)
        CompressionRt=st.slider("Compression Rate",min_value=7.0,max_value=24.0,step=0.1,value=9.0)
        HP=st.slider("Horse Power",min_value=50,max_value=300,value=90,step=1)
        PeakRPM=st.slider("Peak RPM",min_value=4100,max_value=6700,step=10,value=5200)
        CityMPG=st.slider("City MPG",min_value=13,max_value=50,value=25,step=1)
        HighwayMPG=st.slider("HighWay MPG",min_value=13,max_value=50,value=25,step=1)
    
    button = st.form_submit_button("Predict The Car Price")

with st.expander("ℹ Feature Descriptions"):
    st.markdown("""
### 🔍 Input Feature Glossary

**Symboling**  
*Its assigned insurance risk rating. A value of +3 indicates the car is risky, -3 that it's probably safe.* 

**carCompany**  
*Name of the car company.* 

**fueltype**  
*Fuel type used in car (gas/diesel).* 

**aspiration**  
*Type of air intake used in the engine.* 

**doornumber**  
*Number of doors in the car.*

**carbody**  
*Type of car body (e.g., sedan, hatchback).*

**drivewheel**  
*Drive configuration: front, rear, or 4-wheel.*

**enginelocation**  
*Placement of engine: front or rear.*

**wheelbase**  
*Distance between front and rear wheels.*

**carlength**  
*Length of the car from bumper to bumper.*

**carwidth**  
*Width of the car.*

**carheight**  
*Height of the car.*

**curbweight**  
*Weight of the car without passengers or luggage.*

**enginetype**  
*Configuration or layout of the engine.*

**cylindernumber**  
*Number of cylinders in the engine.*

**enginesize**  
*Displacement or volume of the engine.*

**fuelsystem**  
*Type of fuel delivery system (e.g., MPFI, 2bbl).*

**boreratio**  
*Diameter of the cylinder bore relative to the stroke.*

**stroke**  
*Distance traveled by piston in the cylinder.*

**compressionratio**  
*Ratio of the maximum to minimum cylinder volume.*

**horsepower**  
*Power output of the engine.*

**peakrpm**  
*Maximum revolutions per minute (RPM) of the engine.*

**citympg**  
*Mileage (MPG) in city conditions.*

**highwaympg**  
*Mileage (MPG) on highways.*

**price**  
*(Target) The price of the car.*
""")
if button:
    input_data = {
        "Brand": [Brand],
        "Model": [Model],
        "fueltype": [FuelType],
        "aspiration": [Aspiration],
        "No. of doors": [DoorNo],
        "carbody": [Carbody],
        "drivewheel": [DriveWheel],
        "enginelocation": [EngineLocation],
        "wheelbase": [WheelBase],
        "carlength": [CarLength],
        "carwidth": [CarWidth],
        "carheight": [CarHeight],
        "curbweight": [CurbWieght],
        "enginetype": [EngineType],
        "No. of Cylinders": [CylNo],
        "enginesize": [EngSize],
        "fuelsystem": [FuelSys],
        "boreratio": [BorRatio],
        "stroke": [Stroke],
        "compressionratio": [CompressionRt],
        "horsepower": [HP],
        "peakrpm": [PeakRPM],
        "citympg": [CityMPG],
        "highwaympg": [HighwayMPG],
        "symboling": [Symboling]
    }

    input_df = pd.DataFrame(input_data)
    predicted_price = model.predict(input_df)[0]
    st.success(f"💸 Predicted Price: ${predicted_price:,.2f}")
else:
    st.info("Press the Predict Button to start prediction ")