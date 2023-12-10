from sqlalchemy.orm import Session
from models.pedidoModel import PedidoModel
from schemas.pedidoSchema import PedidoSchema
import requests

class PedidoService:
    def __init__(self, db: Session, base_url_clientes: str, base_url_productos: str, base_url_repartidores: str) -> None:
        self.db = db
        self.base_url_clientes = base_url_clientes
        self.base_url_productos = base_url_productos
        self.base_url_repartidores = base_url_repartidores

    # Métodos de validación de existencia
    def validar_cliente_existente(self, cliente_id: int) -> bool:
        response = requests.get(f"{self.base_url_clientes}/clientes/{cliente_id}")
        return response.status_code == 200

    def validar_producto_existente(self, producto_id: int) -> bool:
        response = requests.get(f"{self.base_url_productos}/productos/{producto_id}")
        return response.status_code == 200

    def validar_repartidor_existente(self, repartidor_id: int) -> bool:
        response = requests.get(f"{self.base_url_repartidores}/repartidores/{repartidor_id}")
        return response.status_code == 200

    # Resto de los métodos del servicio
    def obtener_pedidos(self):
        return self.db.query(PedidoModel).all()

    def obtener_pedido_por_id(self, id_pedido: int):
        return self.db.query(PedidoModel).filter_by(idPedido=id_pedido).first()

    def crear_pedido(self, pedido: PedidoSchema):
        # Validación de existencia antes de crear el pedido
        if not self.validar_cliente_existente(pedido.idCliente):
            raise ValueError("Cliente no encontrado.")
        if not self.validar_producto_existente(pedido.idProducto):
            raise ValueError("Producto no encontrado.")
        if not self.validar_repartidor_existente(pedido.idRepartidor):
            raise ValueError("Repartidor no encontrado.")

        nuevo_pedido = PedidoModel(**pedido.dict())
        self.db.add(nuevo_pedido)
        self.db.commit()
        self.db.refresh(nuevo_pedido)
        return nuevo_pedido

    def actualizar_pedido(self, id_pedido: int, pedido_actualizado: PedidoSchema):
        pedido_existente = self.obtener_pedido_por_id(id_pedido)
        if pedido_existente:
            for key, value in pedido_actualizado.dict(exclude_unset=True).items():
                setattr(pedido_existente, key, value)
            self.db.commit()
            self.db.refresh(pedido_existente)
            return pedido_existente
        return None

    def eliminar_pedido(self, id_pedido: int):
        pedido_existente = self.obtener_pedido_por_id(id_pedido)
        if pedido_existente:
            self.db.delete(pedido_existente)
            self.db.commit()
            return True
        return False


# class PedidoService:
#     def __init__(self, db: Session) -> None:
#         self.db = db

#     def obtener_pedidos(self):
#         return self.db.query(PedidoModel).all()

#     def obtener_pedido_por_id(self, id_pedido: int):
#         return self.db.query(PedidoModel).filter_by(idPedido=id_pedido).first()

#     def crear_pedido(self, pedido: PedidoSchema):
#         nuevo_pedido = PedidoModel(**pedido.dict())
#         self.db.add(nuevo_pedido)
#         self.db.commit()
#         self.db.refresh(nuevo_pedido)  # Para cargar completamente los datos desde la base de datos
#         return nuevo_pedido

#     def actualizar_pedido(self, id_pedido: int, pedido_actualizado: PedidoSchema):
#         pedido_existente = self.obtener_pedido_por_id(id_pedido)
#         if pedido_existente:
#             for key, value in pedido_actualizado.dict(exclude_unset=True).items():
#                 setattr(pedido_existente, key, value)
#             self.db.commit()
#             self.db.refresh(pedido_existente)
#             return pedido_existente
#         return None

#     def eliminar_pedido(self, id_pedido: int):
#         pedido_existente = self.obtener_pedido_por_id(id_pedido)
#         if pedido_existente:
#             self.db.delete(pedido_existente)
#             self.db.commit()
#             return True
#         return False