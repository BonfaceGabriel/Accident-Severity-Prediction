import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from joblib import load

from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

def preprocess_data(raw_data):

    scaler = MinMaxScaler()
    # Convert raw_data to a DataFrame
    df = pd.DataFrame(raw_data, index=[0])

    numerical_features = ['Start_Lng', 'Start_Lat', 'Humidity(%)', 'Distance(mi)', 'Precipitation(in)']
    categorical_features = ['Stop', 'Give_Way', 'Amenity', 'Traffic_Calming', 'Crossing', 'Bump']

    #scale numeric features
    scaler.fit(df[numerical_features])
    df[numerical_features] = scaler.transform(df[numerical_features])

    encoder = OneHotEncoder()
    #encode categorical variables
    encoded_data = encoder.fit_transform(df[categorical_features])

    encoded_columns = encoder.get_feature_names_out(categorical_features)

    df_encoded = pd.DataFrame(encoded_data.toarray(), columns=encoded_columns)

    all_columns = ['Stop_False' ,'Stop_True','Give_Way_False' ,'Give_Way_True','Amenity_False',
                   'Amenity_True','Traffic_Calming_False','Traffic_Calming_True',
                    'Crossing_False' ,'Crossing_True', 'Bump_False','Bump_True']
    
    for col in all_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0


    preprocessed_data = pd.concat([df[numerical_features],df_encoded[all_columns], ], axis=1)

    

    return preprocessed_data