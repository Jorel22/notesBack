# API CRUD de Notas

Este proyecto es una API RESTful construida con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una base de datos de notas.

## Endpoints

La API expone los siguientes endpoints:

-   **GET /notes**: Obtiene todas las notas almacenadas en la base de datos.
-   **POST /notes**: Crea una nueva nota.
-   **PUT /notes/{id}**: Edita una nota existente, identificada por su `id`.
-   **DELETE /notes/{id}**: Elimina una nota específica, identificada por su `id`.

## Requisitos

Asegúrate de tener instalado lo siguiente:

-   Python 3.12+
-   pip (gestor de paquetes de Python)

## Instalación

1.  Clona este repositorio:

    ```bash
    git clone <URL_del_repositorio>
    ```

2.  Navega al directorio del proyecto:

    ```bash
    cd <nombre_del_directorio>
    ```

3.  Crea un entorno virtual (opcional, pero recomendado):

    ```bash
    python -m venv venv
    ```

4.  Activa el entorno virtual:

    -   En Windows:

        ```bash
        venv\Scripts\activate
        ```

    -   En macOS y Linux:

        ```bash
        source venv/bin/activate
        ```

5.  Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1.  Ejecuta la API:

    ```bash
    uvicorn main:app --reload
    ```


2.  La API estará disponible en `http://127.0.0.1:8000`.

3.  Puedes utilizar herramientas como `curl` o Postman para interactuar con los endpoints.

## Ejemplo de uso con curl

-   **Obtener todas las notas:**

    ```bash
    curl [http://127.0.0.1:8000/notes](http://127.0.0.1:8000/notes)
    ```

-   **Crear una nueva nota:**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"title": "Mi nueva nota", "content": "Contenido de la nota"}' [http://127.0.0.1:8000/notes](http://127.0.0.1:8000/notes)
    ```

-   **Editar una nota (reemplaza {id} con el ID de la nota):**

    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"title": "Nota editada", "content": "Nuevo contenido"}' [http://127.0.0.1:8000/notes/](http://127.0.0.1:8000/notes/){id}
    ```

-   **Eliminar una nota (reemplaza {id} con el ID de la nota):**

    ```bash
    curl -X DELETE [http://127.0.0.1:8000/notes/](http://127.0.0.1:8000/notes/){id}
    ```