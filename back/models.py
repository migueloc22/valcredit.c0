from sqlalchemy  import Column, Integer, String ,ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.Config import Base
class Tipo_Documento(Base):
    __tablename__ = "tipo_documento"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    alias = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    usuario = relationship("Usuario", back_populates="tipo_documento") # Relacion uno a muchos con Venta
class Tipo_Usuario(Base):
    __tablename__ = "tipo_usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    usuario = relationship("Usuario", back_populates="tipo_usuario") # Relacion uno a muchos con Venta
# class Evento(Base):
#     __tablename__ = "evento"

#     id = Column(Integer, primary_key=True, index=True)
#     nombre = Column(String(255), nullable=False)
#     ubicacion = Column(String(255), nullable=False)
#     boletos_totales = Column(Integer, nullable=False)
#     boletos_disponibles = Column(Integer, nullable=False)
#     precio_boleto = Column(Float, nullable=False)
#     is_active = Column(Boolean, default=True)
#     fecha_hora = Column(DateTime(timezone=True))
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), onupdate=func.now())
#     ventas = relationship("Venta", back_populates="evento") # Relacion uno a muchos con Venta


# class Venta(Base):
#     __tablename__ = "venta"

#     id = Column(Integer, primary_key=True, index=True)
#     description = Column(String(255), nullable=True)
#     numero_documento = Column(String(100), nullable=False)
#     nombre_comprador = Column(String(255), nullable=False)
#     email_comprador = Column(String(255), nullable=False)
#     precio_boleto = Column(Float, nullable=False)
#     cantidad_boleto = Column(Integer )
#     fk_id_evento = Column(Integer, ForeignKey("evento.id"))
#     fk_id_tipo_documento = Column(Integer, ForeignKey("tipo_documento.id"))
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), onupdate=func.now())

#     evento = relationship("Evento", back_populates="ventas") # Relacion muchos a uno con Evento
#     tipo_documento = relationship("Tipo_Documento", back_populates="ventas") # Relacion muchos a uno con Tipo_Documento

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    celular = Column(String(20), nullable=True)
    numero_documento = Column(String(50), unique=True, nullable=False)
    genero = Column(String(10), nullable=True)
    fk_id_tipo_documento = Column(Integer, ForeignKey("tipo_documento.id"))
    fk_id_tipo_usuario = Column(Integer, ForeignKey("tipo_usuario.id"))
    hashed_password = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    solicitud = relationship("Solicitud", back_populates="usuario") # Relacion uno a muchos con  usuario
    tipo_documento = relationship("Tipo_Documento", back_populates="usuario") # Relacion muchos a uno con Tipo_Documento
    tipo_usuario = relationship("Tipo_Usuario", back_populates="usuario") # Relacion muchos a uno con Tipo_Usuario
class Estado(Base):
    __tablename__ = "estado"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    solicitud = relationship("Solicitud", back_populates="estado") # Relacion uno a muchos con Venta
class Solicitud(Base):
    __tablename__ = "solicitud"

    id = Column(Integer, primary_key=True, index=True)
    valor_solicitado = Column(Float, nullable=False)
    numero_cuotas = Column(Integer, nullable=False)
    fk_id_estado = Column(Integer, ForeignKey("estado.id"))
    fk_id_usuario = Column(Integer, ForeignKey("usuario.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    usuario = relationship("Usuario", back_populates="solicitud") # Relacion uno a muchos con  usuario
    estado = relationship("Estado", back_populates="solicitud") # Relacion uno a muchos con Estado
    plan_pagos = relationship("Plan_pagos", back_populates="solicitud") # Relacion uno a muchos con     Plan_pagos

class Plan_pagos(Base):
    __tablename__ = "plan_pagos"

    id = Column(Integer, primary_key=True, index=True)
    numero_cuota = Column(Integer, nullable=False)
    valor_cuota = Column(Float, nullable=False)
    saldo_pendiente = Column(Float, nullable=False)
    fk_id_solicitud = Column(Integer, ForeignKey("solicitud.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    solicitud = relationship("Solicitud", back_populates="plan_pagos") # Relacion uno a muchos con     Plan_pagos