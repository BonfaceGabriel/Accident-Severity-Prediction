import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from joblib import load
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

def preprocess_data(raw_data):
    encoder = load('API/encoder.joblib')
    imputer = load('API/imputer.joblib')
    scaler = load('API/scaler.joblib')


    # Convert raw_data to a DataFrame
    df = pd.DataFrame(raw_data, index=[0])

    # Separate numerical and categorical features
    numerical_features = ['Start_Lng', 'Start_Lat', 'Humidity', 'Distance', 'Precipitation']
    categorical_features = ['Stop', 'Give_Way', 'Amenity', 'Traffic_Calming', 'Crossing', 'Bump']

    # # Create transformers for numerical and categorical features
    # numerical_transformer = Pipeline(steps=[
    #     ('imputer', SimpleImputer(strategy='mean')),
    #     ('scaler', MinMaxScaler())
    # ])
    # categorical_transformer = OneHotEncoder()

    # # Create a ColumnTransformer to apply the transformers to the appropriate features
    # preprocessor = ColumnTransformer(
    #     transformers=[
    #         ('num', numerical_transformer, numerical_features),
    #         ('cat', categorical_transformer, categorical_features)
    #     ])

    #impute numerical features
    imputer.fit(df[numerical_features])
    df[numerical_features] = imputer.transform(df[numerical_features])

    #scale numeric features
    scaler.fit(df[numerical_features])
    df[numerical_features] = scaler.transform(df[numerical_features])


    #encode categorical variables
    encoded_data = encoder.fit_transform(df[categorical_features])
    encoded_columns = list(encoder.get_feature_names_out(df[categorical_features]))
    df_encoded = pd.DataFrame(encoded_data, columns=encoded_columns)

    
    preprocessed_data = pd.concat([df_encoded, df[numerical_features]], axis=1)
    print(preprocessed_data.info())
    

    return preprocessed_data