# Arquitectura de Microservicios para Empresa de Delivery

Este es un proyecto de sistema de gestión de pedidos y entregas basado en una arquitectura de microservicios. A continuación, encontrarás toda la información necesaria para entender, configurar y desplegar este sistema.

## Descripción del Proyecto
Este proyecto es una plataforma diseñada para empresas de delivery que desean optimizar sus operaciones mediante la gestión eficiente de pedidos, clientes, productos y repartidores. La arquitectura de microservicios permite una escalabilidad y mantenimiento sencillo de cada componente del sistema.

- Cada microservicio esta desarrollado con el marco de trabajo FastAPI que es un framework de Python
- Cada microservicio tendrá su propia base de datos en SQLite
- Cada microservicio tendra un schema para validar los datos
- Tendra tambien un middleware para validar los errores en en el codigo o en las solicitudes realizadas al api
- Se usará la ORM SQLAchemy para comunicarse con la base de datos, y al ser un proyecto modular podrá cambiar de motor de base de datos con solo realizar el cambio en el archivo de la configuración, y no habrá necesidad de realizar el cambio en todo el codigo.

## Microservicios

1. **ProductManagmentMicroservice_FastAPI**
Gestiona la información de productos disponibles para ordenar.

2. **CustomerManagmentMicroservice_FastAPI**
Maneja la información de clientes y sus direcciones.

3. **DeliveryManManagmentMicroservice_FastAPI**
Gestiona la información de los repartidores y su disponibilidad.

4. **OrderManagmentMicroservice_FastAPI**
Responsable de crear y gestionar órdenes. Valida la existencia de productos, usuarios y repartidores antes de crear una orden.

## Configuración del Entorno de Trabajo

1. **Clonar el Repositorio:**
    ```bash
   # ProductManagmentMicroservice_FastAPI
   git clone https://github.com/gianmarco-holm/ProductManagmentMicroservice_FastAPI.git
    
   # CustomerManagmentMicroservice_FastAPI
   git clone https://github.com/gianmarco-holm/CustomerManagmentMicroservice_FastAPI.git
   
   # DeliveryManManagmentMicroservice_FastAPI
   git clone https://github.com/gianmarco-holm/DeliveryManManagmentMicroservice_FastAPI.git
    
   # OrderManagmentMicroservice_FastAPI
    git clone https://github.com/gianmarco-holm/OrderManagmentMicroservice_FastAPI.git
    ```

2. **Crear y Activar el Entorno Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para sistemas basados en Unix
    # o
    .\venv\Scripts\activate  # Para sistemas basados en Windows
    ```

3. **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## Ejecutar la API

1. **Ejecutar la Aplicación:**
    ```bash
    # Colocar el puerto es opcional
    uvicorn main:app --reload --port 8000
    ```

## Contribuir
¡Siéntete libre de contribuir al proyecto! Abre un problema o envía una solicitud de extracción.


## Tech Stack

**FastAPI:** El framework base

**Uvicorn:** Framework usado para el servidor

**Starlette:** Libreria para manejar errores en el middleware

**Pydantic:** Libreria para validar datos en esquema

**SQLalchemy:** ORM utilizado para comunicarse con la base de datos

**PyJWT:** Libreria para generar el token del API

**SqlLite:** Base de datos super ligera y rapida para soluciones rapidas de negocio
