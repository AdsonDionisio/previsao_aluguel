from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
import uvicorn
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


class AlugelRequest(BaseModel):
    bairro: str
    tipo_imovel: str
    area_util: float
    banheiros: int
    suites: int
    quartos: int
    vagas_garagem: int
    taxa_condominio: float
    iptu_ano: float

app = FastAPI()

# arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")


modelo = joblib.load("modelo_aluguel.pkl")

@app.get("/")
async def root():
     return FileResponse("templates/index.html")



@app.post("/prever_alugel/")
async def prever_alugel(dados: AlugelRequest):
    entrada = pd.DataFrame([dados.model_dump()])
    try:
        rental_value = modelo.predict(entrada)
    except Exception as e:
        return {"error": str(e)}    

    preco_aluguel = np.expm1(rental_value)[0]
    
    return {"rental_value": preco_aluguel}


# Este bloco roda o uvicorn quando você executa o arquivo diretamente
#if __name__ == "__main__":
#    uvicorn.run("app:app", host="0.0.0.0", port=80, reload=True)