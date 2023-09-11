
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import os
from fastapi import FastAPI
import uvicorn
from fastapi.responses import Response, RedirectResponse
from src.pipeline.prediction import PredictionPipeline


app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train", tags=["training"])
async def training():
    try:
        os.system("python main.py")
        return Response(content="Training completed successfully", status_code=200)
    except Exception as e:
        return Response(content=str(e), status_code=500)

@app.post("/predict", tags=["prediction"])
async def prediction(text):
    try:
        prediction_pipeline = PredictionPipeline()
        summary = prediction_pipeline.predict(text)
        return Response(content=summary, status_code=200)
    except Exception as e:
        return Response(content=str(e), status_code=500)

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8080)