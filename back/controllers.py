from sqlalchemy.orm import Session, aliased
from fastapi import Depends, FastAPI, HTTPException
import models, schemas
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uuid
import hashlib
from typing import Optional

# tipo_documento CRUD Operations
def get_tipo_documents(db: Session, skip: int = 0, limit: int = 100):
    tipo_documents = db.query(models.Tipo_Documento).offset(skip).limit(limit).all()
    if not tipo_documents:
        raise HTTPException(status_code=404, detail="No Tipo_Documento found")
    return tipo_documents
# tipo_usuario CRUD Operations
def get_tipo_usuarios(db: Session, skip: int = 0, limit: int = 100):
    tipo_usuarios = db.query(models.Tipo_Usuario).offset(skip).limit(limit).all()
    if not tipo_usuarios:
        raise HTTPException(status_code=404, detail="No Tipo_Usuario found")
    return tipo_usuarios 
# Usuario CRUD Operations
def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    usuarios = db.query(models.Usuario).offset(skip).limit(limit).all()
    if not usuarios:
        raise HTTPException(status_code=404, detail="No Usuario found")
    return usuarios
def create_usuario(db: Session, usuario: schemas.UsuarioBase):
    db_usuario = models.Usuario(**usuario.model_dump())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
# Solicitud CRUD Operations
def get_solicitudes(db: Session, skip: int = 0, limit: int = 100):
    solicitudes = db.query(models.Solicitud).offset(skip).limit(limit).all()
    if not solicitudes:
        raise HTTPException(status_code=404, detail="No Solicitud found")
    return solicitudes
def create_solicitud(db: Session, solicitud: schemas.SolicitudCreate):
    db_solicitud = models.Solicitud(**solicitud.model_dump())
    db.add(db_solicitud)
    db.commit()
    db.refresh(db_solicitud)
    return db_solicitud
def calcular_solicitudes(valores = schemas.calcularPlanPagos):
    try:
        if valores.numero_cuota is None:
            raise HTTPException(status_code=400, detail="numero_cuotas es requerido.")
        if valores.valor_solicitado is None:
            raise HTTPException(status_code=400, detail="valor_solicitado es requerido.")
        if valores.numero_cuota < 2 and valores.numero_cuota > 24:
            raise HTTPException(status_code=400, detail="El número de cuotas debe ser mayor a 2 y menores igual a 24 ")
        if valores.valor_solicitado < 100000 and valores.valor_solicitado > 100000000:
            raise HTTPException(status_code=400, detail="El saldo pendiente debe ser menor a 100,000 y el valor solicitado mayor a 100,000,000 ")
        plan_pagos = []
        numero_cuota = valores.numero_cuota
        valor_solicitado = valores.valor_solicitado
        cuota_basica = valor_solicitado / numero_cuota
        for i in range(1, numero_cuota + 1):
            saldo_pendiente = valor_solicitado - (cuota_basica * i)
            plan_pagos.append({
                "numero_cuota": i,
                "valor_solicitado": round(cuota_basica, 2),
                "saldo_pendiente": round(saldo_pendiente, 2)
            })
        responde = {
                    "PlanPagos": plan_pagos,
                    "total_pago": round(valor_solicitado, 2)
                    }
        return responde
    except ZeroDivisionError: # error division por cero
        raise HTTPException(status_code=400, detail="No se puede dividir entre cero (número de cuotas inválido).")

# Simple token store (en memoria) -> para desarrollo. Reiniciar servidor borra tokens.
_tokens: dict[str, int] = {}  # token -> user_id

# NOTE: Temporalmente deshabilitado hashing. Para producción usar hashing (bcrypt / passlib) y volver a activar.
# def hash_password(password: str) -> str:
#     return hashlib.sha256(password.encode()).hexdigest()
#
# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return hash_password(plain_password) == hashed_password

def authenticate_user(db: Session, email: str, password: str):
    """
    Devuelve el objeto Usuario si las credenciales son válidas, sino None.
    TEMPORAL: no se usa hash. Si el campo hashed_password está vacío, se permite el login
    (útil para pruebas). Si existe, se compara texto plano con el valor almacenado.
    """
    user = db.query(models.Usuario).filter(models.Usuario.email == email).first()
    if not user:
        return None

    # Si no hay contraseña almacenada, permitir (temporal)
    if not user.hashed_password:
        return user

    # Si hay un valor en hashed_password lo tratamos como contraseña en texto plano (temporal)
    if user.hashed_password != password:
        return None

    return user

def create_access_token(user_id: int) -> str:
    token = uuid.uuid4().hex
    _tokens[token] = user_id
    return token

def get_user_id_by_token(token: str) -> Optional[int]:
    return _tokens.get(token)

def get_usuario_by_id(db: Session, user_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == user_id).first()

def get_plan_pagos_by_user_id(db: Session, user_id: int):
    """
    Devuelve las solicitudes del usuario (por id) con sus plan_pagos.
    """
    user = get_usuario_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    solicitudes = db.query(models.Solicitud).filter(models.Solicitud.fk_id_usuario == user.id).all()
    result = []
    for s in solicitudes:
        planos = []
        for p in s.plan_pagos:
            planos.append({
                "id": p.id,
                "numero_cuota": p.numero_cuota,
                "valor_cuota": p.valor_cuota,
                "saldo_pendiente": p.saldo_pendiente
            })
        result.append({
            "solicitud_id": s.id,
            "valor_solicitado": s.valor_solicitado,
            "numero_cuotas": s.numero_cuotas,
            "plan_pagos": planos
        })
    return result


