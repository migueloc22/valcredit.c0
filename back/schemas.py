from pydantic import BaseModel, EmailStr, computed_field
from typing import Optional
from datetime import datetime

# # Evento Schemas
#  Tipo_Documento Schemas
class TipoDocumentoBase(BaseModel):
    nombre: str
    alias: str
class TipoDocumentoCreate(TipoDocumentoBase):
    pass
class TipoDocumento(TipoDocumentoBase):
    id: int
    nombre: str
    alias: str
    class Config:
        from_attributes = True
# # Venta Schemas
# Usuario Schemas
class UsuarioBase(BaseModel):
    nombres: str
    apellidos: str
    email: EmailStr
    celular: Optional[str] = None
    numero_documento: str
    genero: Optional[str] = None
    fk_id_tipo_documento: Optional[int] = 1
    fk_id_tipo_usuario: Optional[int] = 1
    hashed_password : Optional[str] = None
class UsuarioCreate(UsuarioBase):
    pass
class UsuarioResponse(UsuarioBase):
    id: int
    pass
class UsarioUpdatePass(BaseModel):
    password: str
class Usuario(UsuarioBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True
# Tipo_Usuario Schemas
class TipoUsuarioBase(BaseModel):
    nombre: str
class TipoUsuarioCreate(TipoUsuarioBase):
    pass
class TipoUsuario(TipoUsuarioBase):
    id: int
    class Config:
        from_attributes = True
# Solicitud
class SolicitudBase(BaseModel):
    valor_solicitado: float
    numero_cuotas: int
    fk_id_estado: int = 1
    fk_id_usuario: int
class SolicitudCreate(SolicitudBase):
    pass
class Solicitud(SolicitudBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True
# Nueva respuesta enriquecida para Solicitud con datos del usuario y estado
class SolicitudResponse(BaseModel):
    id: int
    valor_solicitado: float
    numero_cuotas: int
    fk_id_estado: int
    fk_id_usuario: int
    usuario_nombres: Optional[str] = None
    usuario_email: Optional[EmailStr] = None
    tipo_documento_alias: Optional[str] = None
    estado_nombre: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True
# Estado Schemas
class EstadoBase(BaseModel):
    nombre: str
class EstadoCreate(EstadoBase):
    pass
class Estado(EstadoBase):
    id: int
    class Config:
        from_attributes = True
# Plan pagos
class PlanPagosBase(BaseModel):
    numero_cuotas: int
    valor_cuota: float
    saldo_pendiente: float
    fk_id_solicitud: int
class PlanPagosCreate(BaseModel):
    pass
class PlanPagos(PlanPagosBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True
class calcularPlanPagos(BaseModel):
    valor_solicitado: float
    numero_cuota: int
    saldo_pendiente: Optional[float] = None
class planPagosResponse(BaseModel):
    PlanPagos: Optional[list[calcularPlanPagos]] = None
    total_pago: Optional[float] = None
# Login Schema
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
# Actualizar Estado de Solicitud
class SolicitudUpdateEstado(BaseModel):
    fk_id_estado: int