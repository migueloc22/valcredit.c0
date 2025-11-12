# from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, controllers
from db.Config import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
# from db.Config import settings  
from dotenv import load_dotenv
load_dotenv()
import os
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

models.Base.metadata.create_all(bind=engine) # crea las tablas en la base de datos

app = FastAPI()
#cors
origins = [
    "http://localhost.tiangolo.com",
    "http://localhost:5173",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Instancia la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db # yield es como return pero para generadores
    finally:
        db.close()

# @app.get("/")
# def read_root():
#     # return {"Hello": "World"}
#     return {"Hello": os.getenv("DATABASE_URL")}
# Evento Endpoints

# tipo_documento CRUD Endpoints
@app.get("/v1/tipo_documentos/", response_model=list[schemas.TipoDocumento],tags    =['Tipo_Documento'])
def read_tipo_documentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tipo_documentos = controllers.get_tipo_documents(db, skip=skip, limit=limit)
    return tipo_documentos
# tipo_usuario CRUD Endpoints
@app.get("/v1/tipo_usuarios/", response_model=list[schemas.TipoUsuario],tags=['Tipo_Usuario'])
def read_tipo_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tipo_usuarios = controllers.get_tipo_usuarios(db, skip=skip, limit=limit)
    return tipo_usuarios
# Usuario CRUD Endpoints
@app.get("/v1/usuarios/", response_model=list[schemas.Usuario],tags=['Usuario'])
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios = controllers.get_usuarios(db, skip=skip, limit=limit)
    return usuarios
@app.post("/v1/usuarios/", response_model=schemas.UsuarioCreate,tags=['Usuario'])
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return controllers.create_usuario(db=db, usuario=usuario)
@app.post("/v1/calcular_pagos", response_model=schemas.planPagosResponse,tags=['Solicitud'])
def calcular_plan_pagos(valores: schemas.calcularPlanPagos, db: Session = Depends(get_db)):
    plan_pagos = controllers.calcular_solicitudes(valores=valores)
    return plan_pagos

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Endpoint OAuth2 password flow. El campo 'username' del form debe contener el email.
    Devuelve access_token (bearer) si las credenciales son correctas.
    """
    # form_data.username se interpreta como email
    user = controllers.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = controllers.create_access_token(user.id)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/v1/me", response_model=schemas.Usuario, tags=['Usuario'])
def read_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Ruta protegida de ejemplo. Requiere Authorization: Bearer <token>.
    """
    user_id = controllers.get_user_id_by_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    user = controllers.get_usuario_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@app.get("/v1/solicitudes/planes", tags=['Solicitud'])
def read_my_solicitud_planes(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Ruta protegida: devuelve las solicitudes del usuario autenticado y sus plan_pagos.
    Authorization: Bearer <token>
    """
    user_id = controllers.get_user_id_by_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    planes = controllers.get_plan_pagos_by_user_id(db, user_id)
    return planes