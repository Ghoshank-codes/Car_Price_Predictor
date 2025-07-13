'''
In this .py file , We will make pipeline/column transformer for preprocessing,
prediction of car price and define custom transformer if required and
Save Them to .pkl file 
'''
# Libraies to load the file as dataframe and To do operations on them
import pandas as pd 
import numpy as np
pd.set_option("display.max_columns", None)

# Library to avoid warnings
import warnings
warnings.filterwarnings('ignore')

# For Preprocessing Of Data 
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder,StandardScaler
from sklearn.model_selection import train_test_split

# SElected Model For Regression problem
from sklearn.ensemble import RandomForestRegressor

# For creating a final pipeline 
from sklearn.base import BaseEstimator,TransformerMixin  # Parent classes to define custom transformers
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# For Saving Pipeline In .pkl file 
import joblib

# First we would make custom class for mapping the categories of a feature

class LabelMapper(BaseEstimator,TransformerMixin):
    def __init__(self,mapper):
        self.mapper=mapper
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        return X.replace(self.mapper)
    
# This class will be used to encode Brand name and Model Name , For this we requires a map 

df=pd.read_csv("E:/Projects_ML/Cohort/Car_Price_Predictor/data/cleaned_data.csv")

X=df.drop("price",axis=1)
y=df["price"]

categorical=[col for col in X.columns if X[col].dtype=='O']
numerical=[col for col in X.columns if X[col].dtype!='O']

Binary_encode = [x for x in categorical if X[x].nunique()==2]                         # Categories That Can Be Encoded in Binary (0 or 1)
one_hot = [x for x in categorical if X[x].nunique()>2 and X[x].nunique()<10]          # Features for One Hot Encoding
label_encode=[x for x in categorical if x not in Binary_encode and x not in one_hot ] # Custom Encoding Through Mapping 

# Encoding The Brand Names on The Basis of Their Popularity
brand_counts = X["Brand"].value_counts().sort_values(ascending=True)
brand_encoder={brand:rank for rank,brand in enumerate(brand_counts.index[::])}

model_encoder={}
for brand in X["Brand"].unique():
    model_brand= X[X["Brand"]==brand]["Model"]
    model_counts=model_brand.value_counts().sort_values(ascending=True)

    model_encoder.update({model:rank for rank,model in enumerate(model_counts.index)})

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42,test_size=0.2)

preprocessor=ColumnTransformer([
    ("Brand_Encoder",Pipeline([("Brand_map",LabelMapper(mapper=brand_encoder)),("Scaler",StandardScaler())]),["Brand"]),
    ("Model_Encoder",Pipeline([("Model_map",LabelMapper(mapper=model_encoder)),("Scaler",StandardScaler())]),["Model"]),
    ("One Hot Encoder",OneHotEncoder(),one_hot),
    ("Binary Encoder",OrdinalEncoder(),Binary_encode),
    ("Standardizer",StandardScaler(),numerical)
])

# Preprocessor is Ready
 
RandomForestPredictor=Pipeline([
    ("Preprocessor",preprocessor),
    ("Predictor",RandomForestRegressor(bootstrap= False,max_depth= 15,max_features= 'log2'
                                       ,min_samples_leaf= 1,min_samples_split= 2, n_estimators= 100, random_state= 42))
])

RandomForestPredictor.fit(X_train,y_train)

# Both Preprocessor and Prediction Model is ready to use

# Last Step is now just to save this model in .pkl file

joblib.dump(RandomForestPredictor,"models/prediction_model.pkl")