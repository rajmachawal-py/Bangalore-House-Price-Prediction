import pickle
import json
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    try:
        columns_path = "./artifacts/columns.json"
        model_path = './artifacts/Banglore_home_prices_model.pickle'
        
        print(f"Current working directory: {os.getcwd()}")
        print(f"Looking for columns file at: {os.path.abspath(columns_path)}")
        print(f"Looking for model file at: {os.path.abspath(model_path)}")
        
        # Check if files exist
        print(f"Columns file exists: {os.path.exists(columns_path)}")
        print(f"Model file exists: {os.path.exists(model_path)}")
        
        if not os.path.exists(columns_path):
            print(f"ERROR: columns.json file not found")
            __locations = []
            return
            
        if not os.path.exists(model_path):
            print(f"ERROR: model pickle file not found")
            __locations = []
            return

        # Load columns
        with open(columns_path, "r") as f:
            data = json.load(f)
            print(f"JSON data keys: {data.keys()}")
            __data_columns = data['data_columns']
            __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
            print(f"Total data columns: {len(__data_columns)}")
            print(f"First 3 columns (features): {__data_columns[:3]}")
            print(f"Total locations: {len(__locations)}")
            print(f"First 5 locations: {__locations[:5] if len(__locations) >= 5 else __locations}")

        # Load model
        if __model is None:
            with open(model_path, 'rb') as f:
                __model = pickle.load(f)
                print(f"Model loaded successfully: {type(__model)}")
        
        print("loading saved artifacts...done")
        
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        __locations = []
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        __locations = []
    except KeyError as e:
        print(f"KeyError - missing key in JSON: {e}")
        __locations = []
    except Exception as e:
        print(f"Unexpected error loading artifacts: {e}")
        import traceback
        traceback.print_exc()
        __locations = []

def get_location_names():
    if __locations is None:
        print("WARNING: __locations is None, returning empty list")
        return []
    return __locations

def get_data_columns():
    return __data_columns