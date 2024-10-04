from pydantic import BaseModel

class Item(BaseModel):
    """Schema for the input data used for prediction in the machine learning model.
    
    Attributes:
        sepal_length (float): The length of the sepal in centimeters.
        sepal_width (float): The width of the sepal in centimeters.
        petal_length (float): The length of the petal in centimeters.
        petal_width (float): The width of the petal in centimeters.
    """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisPrediction(BaseModel):
    """Schema for the output data from the prediction model.
    
    Attributes:
        species (str): The predicted species of the Iris flower.
    """
    species: str


