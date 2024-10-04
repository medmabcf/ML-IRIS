import joblib
import pandas as pd
from fastapi import HTTPException

def load_model(model_path: str) -> object:
    """Load the machine learning model from the specified path.
    
    Args:
        model_path (str): The path to the model.
        
    Returns:
        object: The loaded ML  model.
        
    Raises:
        HTTPException: If the model file is not found or an error occurs during loading.
    """
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Model file not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while loading the model: {str(e)}")

