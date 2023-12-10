from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class PedidoSchema(BaseModel):
    idPedido: Optional[int] = Field(None, description="ID del pedido (opcional)")
    idCliente: int = Field(..., description="ID del cliente")
    idRepartidor: int = Field(..., description="ID del repartidor")
    idProducto: int = Field(..., description="ID del producto")
    telefono: str = Field(..., pattern=r'^\d{9}$', description="Número de teléfono para el pedido")
    direccionEntrega: Optional[str] = Field(None, max_length=100, description="Dirección de entrega (opcional, hasta 100 caracteres)")
    fechaHoraEntrega: Optional[datetime] = Field(None, description="Fecha y hora de entrega del pedido (sin segundos)")
    created_at: Optional[datetime] = Field(None, description="Fecha de creación del pedido")

    class Config:
        title = "Esquema de Pedido"
        description = "Modelo para representar un pedido"
        json_schema_extra = {
            "examples": [
                {
                    "idCliente": 1,
                    "idRepartidor": 1,
                    "idProducto": 1,
                    "telefono": "987654321",
                    "direccionEntrega": "Calle Principal 123",
                    "fechaHoraEntrega": "2023-12-15T12:00:00",
                    "created_at": "2023-12-15T10:30:00"
                }
            ]
        }
