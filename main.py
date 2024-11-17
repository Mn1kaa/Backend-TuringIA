from fastapi import FastAPI,Body
from fastapi.middleware.cors import CORSMiddleware
from sql_app.database import SessionLocal,engine,Base
from typing import List
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sql_app.schemas import SchemaCelular,SchemaPC,SchemaTablet
from sql_app.models import PC,Celular,Tablets

app= FastAPI(title="Turing IA - API",description="API para la Prueba técnica de Turing IA",version="1.0")
origins=["*"]
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_headers=["*"],allow_methods=["*"])
Base.metadata.create_all(bind=engine)


##====================CRUD COMPUTADORA====================
##=========================================================
##========================================================

@app.get('/computadora_get',tags=["CRUD Computadoras"],response_model=List[SchemaPC] )
def get_computadoras():
    db=SessionLocal()
    all_computers=db.query(PC).all()
    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonable_encoder(all_computers))

@app.post('/computadora_post',tags=["CRUD Computadoras"],response_model=dict )

def post_computadoras(argumento:SchemaPC=Body()):
     db=SessionLocal()
     newComputadora=PC(**argumento.model_dump())
     try: 
         db.add(newComputadora)
     except:
          return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED,content={'message':"No creado"})
     else:
        db.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED,content={'message':"Creado"}) 
     
@app.put('/computadora_put{id}',tags=['CRUD Computadoras'],response_model=SchemaPC)
def put_computadora(id:int,datos_corregidos:SchemaPC=Body()):
    db=SessionLocal()
    registro_a_modificar=db.query(PC).filter(PC.id==id).first()
    if registro_a_modificar:
        registro_a_modificar.descripcion=datos_corregidos.descripcion
        registro_a_modificar.almacenamiento=datos_corregidos.almacenamiento
        registro_a_modificar.marca=datos_corregidos.marca
        registro_a_modificar.memoria_ram=datos_corregidos.memoria_ram
        registro_a_modificar.sistema_operativo=datos_corregidos.sistema_operativo
        db.commit()
        db.refresh(registro_a_modificar)
        return JSONResponse(status_code=status.HTTP_201_CREATED,content={'message':jsonable_encoder(registro_a_modificar),'mensaje':'Modificado con exito'}) 
    
    if not registro_a_modificar:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,content={'mensaje':'El registro con el ID Proporcionado no existe'}) 

     
@app.delete('/computadora_delete',tags=["CRUD Computadoras"],response_model=dict)
def delete_computadora(id:int=Body()):
    db=SessionLocal()
    
    try:
        compute_to_delete=db.query(PC).filter(PC.id==id).first()

        db.delete(compute_to_delete)
        db.commit()
    except :
        return(JSONResponse(status_code=status.HTTP_200_OK,content={'message':f"Computadora no esxiste "}))
        
   
    return JSONResponse(status_code=status.HTTP_200_OK,content={'message':"Computadora Eliminada"}) 
     


##==================================================================
##=======================CELULAR===================================
##===================================================================
@app.get('/celular_get',tags=["CRUD Celulares"],response_model=List[SchemaCelular] )
def get_celulares():
    db=SessionLocal()
    all_computers=db.query(Celular).all()
    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonable_encoder(all_computers))

@app.post('/celular_post',tags=["CRUD Celulares"],response_model=dict )

def post_ceulares(argumento:SchemaCelular=Body()):
     db=SessionLocal()
     newcelular=Celular(**argumento.model_dump())
     try: 
         db.add(newcelular)
     except:
          return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED,content={'message':"No creado"})
     else:
        db.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED,content={'message':"Creado"}) 
     



##==================================================================
##=======================TABLETS===================================
##===================================================================


@app.get('/tablet_get',tags=["CRUD Tablets"],response_model=List[SchemaTablet] )
def get_tablets():
    db=SessionLocal()
    all_tablets=db.query(Tablets).all()
    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonable_encoder(all_tablets))

@app.post('/tablet_post',tags=["CRUD Tablets"],response_model=dict )

def post_tablets(argumento:SchemaTablet=Body()):
     db=SessionLocal()
     newtablet=Tablets(**argumento.model_dump())
     try: 
         db.add(newtablet)
     except:
          return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED,content={'message':"No creado"})
     else:
        db.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED,content={'message':"Creado"}) 
     





    
