from sqlalchemy import Column, Integer, String, DateTime, func
from config.database import Base

class PedidoModel(Base):
    __tablename__ = 'pedidos'

    idPedido = Column(Integer, primary_key=True, autoincrement=True)
    idCliente = Column(Integer, nullable=False)
    idRepartidor = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    telefono = Column(String(9), nullable=False)
    direccionEntrega = Column(String(100), nullable=True)
    fechaHoraEntrega = Column(DateTime, nullable=True, name='fecha_hora_entrega')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
