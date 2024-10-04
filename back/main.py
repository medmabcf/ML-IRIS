from fastapi import FastAPI
from back.helpers.dto import Item   ,IrisPrediction
import pandas as pd
from back.predict import predict
from back.load import load_model

app = FastAPI()


# Load your model here
model = load_model("./ml/iris_classifier_model.pkl")

# Define a mapping for the predicted species
species_mapping = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

@app.post("/items/", response_model=IrisPrediction)
async def create_item(item: Item):
    if all([item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]):
        df_input = pd.DataFrame([[item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]])
        prediction = predict(model, df_input)

        # Assuming prediction is a list, take the first element
        predicted_species = species_mapping[prediction[0]]  # Convert the integer to the corresponding species

        return IrisPrediction(species=predicted_species)  # Use the schema for the response

    return {"error": "All fields are required."}
