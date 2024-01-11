# CasoPracticoZEPO-4

## Proposito y alcance del proyecto

Haciendo uso de Python o de algún framework de desarrollo basado en Python (como por ejemplo DRF) realice un programa en que simule un ataque de fuerza bruta a una contraseña probando todas las combinaciones de caracteres posibles. La contraseña a descifrar deberá ser enviada por parámetro (ej. def bruteforce_attack(password)) y deberá mostrar como resultado final el número de intentos realizados hasta descifrar la clave:
Input the password: mipassword
Password cracked in 21695135 attempts. The password is mipassword

## Herramientas y tecnologías utilizadas

- Python
- DRF (Django REST Framework)

## Implementacion

- attack/urls.py (proyecto): Se configura como se deben manejar las URLs del proyecto. 
- burteforce_attack/views.py: Se implementa una vista que contiene una clase para realizar el ataque de fuerza bruta en una contraseña objetivo
- bruteforce_attack/urls.py (aplicacion): Se configuran las URL de la aplicación. 

- attack.py: archivo en python sin uso de DRF que realiza el ataque de fuerza bruta. 

## Manual de usuario

## Iniciar

Antes de iniciarla hay que hacer la migracion, 'python3 manage.py migrate'. Para iniciar la aplicación, hay que ejecutar el comando 'python3 manage.py runserver'. Una vez iniciado el programa ya podemos acceder a la URL para realizar el ataque de diccionario, la URL es la siguiente: http://localhost:8000/brute_force/attack/mipassword/. Dentro de la URL una vez encontrada la contraseña nos aparecera en formato json la información. 