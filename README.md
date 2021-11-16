# PlanAcad

## Instrucciones para Windows para ejecutar

ATENCION: Desinstalar todas la versiones de python que tengan y solo instalar la 3.5.

1. Descomprimir **env.zip**
2. Corregir la ruta( al proyecto) del env dentro del activate.bat
3. En la ventana de comandos ejecutar
    ```
    env\Scripts\activate.bat
    ```
    ```
    cd planacad
    ```
    ```
    python manage.py runserver
    ```
4. La aplicación estará corriendo en **http://127.0.0.1:8000/**


## Instrucciones para Windows para crear un modelo nuevo
1. En planificaciones.model.py creo la clase model
2. En planificaciones.views.py creo los request and post
3.En la ventana de comandos ejecutar (para crear la nueva migración)
  ```
  py manage.py makemigrations planificaciones
  ```
  ```
  py manage.py migrate
  ```

## Instrucciones para Linux
## Crear la BD
1. Crear una BD normal con el nombre djangodb
2. Crear un usuario sql con los datos
 
 ```
 user : django
 ```
 ```
 password: Carlos
 ```

2.1. Se pude observar estos datos y incluso modificarlos en el main/setting.py en la seccion DATABASES
3. Darle los permisos al usuario para que pueda realizar insert, update, create, etc
4. En la consola tiramos
 ```
 py manage.py migrate
 ```
5. Listo!!
