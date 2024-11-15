from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sql_app.database import SessionLocal,engine,Base
app= FastAPI()
origins=["*"]
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_headers=["*"],allow_methods=["*"])
Base.metadata.create_all(bind=engine)
@app.get('/',tags=["RespuestaPruebaInicial"] )
def prueba():
    return {'message':'api arriba'}
