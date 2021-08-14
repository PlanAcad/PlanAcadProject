# PlanAcad

## Instrucciones para Windows para ejecutar

1. Descomprimir **env.zip**
2. En la ventana de comandos ejecutar
    ```
    env\Scripts\activate.bat
    ```
    ```
    cd planacad
    ```
    ```
    python manage.py runserver
    ```
3. La aplicación estará corriendo en **http://127.0.0.1:8000/**


## Instrucciones para Windows para crear un modelo nuevo
1- En planificaciones.model.py creo la clase model
2- En planificaciones.views.py creo los request and post
3-En la ventana de comandos ejecutar (para crear la nueva migración)
  ```
  py manage.py makemigrations planificaciones
  ```
  ```
  py manage.py migrate
  ```

## Instrucciones para Linux
