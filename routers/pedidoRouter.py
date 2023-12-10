from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.pedidoSchema import PedidoSchema
from services.pedidoService import PedidoService
from utils.dependencies import get_db

# Proporciona las URL base de los otros servicios
base_url_clientes = "http://127.0.0.1:8001"
base_url_productos = "http://127.0.0.1:8002"
base_url_repartidores = "http://127.0.0.1:8003"

pedido_router = APIRouter()

@pedido_router.get('/pedidos', tags=['Pedidos'], response_model=List[PedidoSchema])
def obtener_pedidos(db: Session = Depends(get_db)) -> List[PedidoSchema]:
    # Instancia el servicio de pedidos con las URL base de los otros servicios
    servicio_pedidos = PedidoService(db, base_url_clientes, base_url_productos, base_url_repartidores)

    try:
        resultado = servicio_pedidos.obtener_pedidos()
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener pedidos: {str(e)}")

@pedido_router.get('/pedidos/{id_pedido}', tags=['Pedidos'], response_model=PedidoSchema)
def obtener_pedido_por_id(id_pedido: int, db: Session = Depends(get_db)) -> PedidoSchema:
    servicio_pedidos = PedidoService(db, base_url_clientes, base_url_productos, base_url_repartidores)

    try:
        resultado = servicio_pedidos.obtener_pedido_por_id(id_pedido)
        if resultado:
            return resultado
        else:
            raise HTTPException(status_code=404, detail=f"No se encontró un pedido con el ID {id_pedido}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener pedido por ID: {str(e)}")

@pedido_router.post('/pedidos', tags=['Pedidos'], response_model=PedidoSchema, status_code=201)
def crear_pedido(pedido: PedidoSchema, db: Session = Depends(get_db)) -> PedidoSchema:
    servicio_pedidos = PedidoService(db, base_url_clientes, base_url_productos, base_url_repartidores)

    try:
        nuevo_pedido = servicio_pedidos.crear_pedido(pedido)
        return nuevo_pedido
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear pedido: {str(e)}")

@pedido_router.put('/pedidos/{id_pedido}', tags=['Pedidos'], response_model=PedidoSchema)
def actualizar_pedido(id_pedido: int, pedido_actualizado: PedidoSchema, db: Session = Depends(get_db)) -> PedidoSchema:
    servicio_pedidos = PedidoService(db, base_url_clientes, base_url_productos, base_url_repartidores)

    try:
        resultado = servicio_pedidos.actualizar_pedido(id_pedido, pedido_actualizado)
        if resultado:
            return resultado
        else:
            raise HTTPException(status_code=404, detail=f"No se encontró un pedido con el ID {id_pedido}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar pedido: {str(e)}")

@pedido_router.delete('/pedidos/{id_pedido}', tags=['Pedidos'], status_code=204)
def eliminar_pedido(id_pedido: int, db: Session = Depends(get_db)):
    servicio_pedidos = PedidoService(db, base_url_clientes, base_url_productos, base_url_repartidores)

    try:
        eliminado_exitosamente = servicio_pedidos.eliminar_pedido(id_pedido)
        if not eliminado_exitosamente:
            raise HTTPException(status_code=404, detail=f"No se encontró un pedido con el ID {id_pedido}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar pedido: {str(e)}")


# pedido_router = APIRouter()

# @pedido_router.get('/pedidos', tags=['Pedidos'], response_model=List[PedidoSchema])
# def obtener_pedidos(db: Session = Depends(get_db)) -> List[PedidoSchema]:
#     try:
#         resultado = PedidoService(db).obtener_pedidos()
#         return resultado
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error al obtener pedidos: {str(e)}")

# @pedido_router.get('/pedidos/{id_pedido}', tags=['Pedidos'], response_model=PedidoSchema)
# def obtener_pedido_por_id(id_pedido: int, db: Session = Depends(get_db)) -> PedidoSchema:
#     try:
#         resultado = PedidoService(db).obtener_pedido_por_id(id_pedido)
#         if resultado:
#             return resultado
#         else:
#             raise HTTPException(status_code=404, detail=f"No se encontró un pedido con el ID {id_pedido}.")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error al obtener pedido por ID: {str(e)}")

# @pedido_router.post('/pedidos', tags=['Pedidos'], response_model=PedidoSchema, status_code=201)
# def crear_pedido(pedido: PedidoSchema, db: Session = Depends(get_db)) -> PedidoSchema:
#     try:
#         nuevo_pedido = PedidoService(db).crear_pedido(pedido)
#         return nuevo_pedido
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error al crear pedido: {str(e)}")

# @pedido_router.put('/pedidos/{id_pedido}', tags=['Pedidos'], response_model=PedidoSchema)
# def actualizar_pedido(id_pedido: int, pedido_actualizado: PedidoSchema, db: Session = Depends(get_db)) -> PedidoSchema:
#     try:
#         resultado = PedidoService(db).actualizar_pedido(id_pedido, pedido_actualizado)
#         if resultado:
#             return resultado
#         else:
#             raise HTTPException(status_code=404, detail=f"No se encontró un pedido con el ID {id_pedido}.")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error al actualizar pedido: {str(e)}")

# @pedido_router.delete('/pedidos/{id_pedido}', tags=['Pedidos'], status_code=204)
# def eliminar_pedido(id_pedido: int, db: Session = Depends(get_db)):
#     try:
#         eliminado_exitosamente = PedidoService(db).eliminar_pedido(id_pedido)
#         if not eliminado_exitosamente:
#             raise HTTPException(status_code=404, detail=f"No se encontró un pedido con el ID {id_pedido}.")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error al eliminar pedido: {str(e)}")

