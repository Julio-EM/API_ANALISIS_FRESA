from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

class SensorData(BaseModel):
    valor_humedad: str


@app.post("/REGISTRO_SENSORES")
def AnalizarJsonEndpoint(data: SensorData):


    return "hola desde post python"