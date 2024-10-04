from fastapi import HTTPException
import pandas as pd 
def predict(model: object, df: pd.DataFrame) -> list:
    """Make predictions using the loaded model.
    
    Args:
        model (object): The model.
        df (pd.DataFrame): A DataFrame containing the input features for prediction.
        
    Returns:
        list: A list of predictions made by the model.
        
    Raises:
        HTTPException: If an error occurs during the prediction process.
    """
    try:
        predictions = model.predict(df)
        return predictions.tolist()  # Convert to list for better compatibility with JSON responses
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during prediction: {str(e)}")
