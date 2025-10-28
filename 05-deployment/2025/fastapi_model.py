import pickle
import uvicorn

from typing import Dict, Any
from fastapi import FastAPI

app = FastAPI(title="subscription-prediction")


with open('/code/pipeline_v2.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

 
def predict_single(client):
    result = pipeline.predict_proba(client)[0, 1]
    return float(result)


@app.post("/predict")    
def predict(client: Dict[str, Any]):
    prob = predict_single(client)

    return {
        "sub_probability": prob,
        "subscription" : bool(prob >= 0.5)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)