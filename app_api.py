from fastapi import FastAPI , Request, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

request_count = 0


class SexEnum(int, Enum):
    female = 0
    male = 1


class PclassEnum(int,Enum):
    first = 1
    second = 2
    third = 3


class PrectionInput(BaseModel):
    Pclass: PclassEnum
    Age: float = Field(..., ge=0)   
    Fare: float = Field(..., ge=0)
    Sex: SexEnum


@app.get("/stats")
def stats():
    return {"request_count": request_count}


@app.get("/health")
def health():
    return {'status': "OK"}


@app.post("/predict_model")
def predict_model(input_data: PrectionInput):
    global request_count
    request_count+=1

    new_data = pd.DataFrame([{
    'Sex': input_data.Sex,        
    'Pclass': input_data.Pclass,     
    'Fare': input_data.Fare,    
    'Age': input_data.Age     
    }])

    pred = model.predict(new_data)
    res = "Survived" if pred[0] == 1 else 'Not Survived'
    
    return {
        'prediction': res
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=4000)