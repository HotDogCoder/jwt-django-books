AMBIENTE LOCAL

1. solicitar a la srta Andrea el .env de la applicacion
2. correr pip install -r requirements.txt
3. python manage.py runserver


LOGIN APP

1. User el endpoint de dj-rest-auth/registration

extraer el access para usarlo en el Authorization Bearer

2. (opcional) logearte y hacer lo mismo

*** La proteccion de las rutas falla en produccion por una imcompatibilidad de djongo 
*** debe probar la seguridad en local
*** para todos los endpoint se uso pymongo no djongo solo que se instalo para usar el ORM y las migraciones


BOOKS APP

1. Correr el QUERY BOOKS

esto hara que puedas ver los datos de prueba

2. Correr los demas endpoint usando Authorization Bearer

3. Revisar los archivos en el postman, tambien puede usar el swagger que esta en la ruta principal localhost:8000

4. puede ver cierta documentacoin en localhost:8000/redoc tambien