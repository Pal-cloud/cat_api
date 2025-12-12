"""
como funciona api rest en python:

Una API REST en Python funciona 
mediante la comunicación del servidor y el cliente a través de peticiones HTTP. 
Para crearla, se usan frameworks como Flask o FastAPI, que permiten definir "endpoints" (rutas) y 
asociarles funciones que manejan verbos HTTP como GET (para leer), POST (para crear), PUT (para actualizar) 
y DELETE (para borrar). Los datos generalmente se intercambian en formato JSON, y 
se utilizan bibliotecas como requests para que otras aplicaciones en Python puedan interactuar con la API.

3.- JSON placeholder : JSON placeholder es una API gratuita que te ofrece datos ficticios como fotos, 
publicaciones, comentarios, datos de usuarios falsos, rutas y mucho más. 
https://jsonplaceholder.typicode.com/
posts : https://jsonplaceholder.typicode.com/posts

4geeks *****
https://4geeks.com/es/how-to/como-consumir-una-api-en-python


------------------------------------------------------------
¿Cómo consumir una API?

A continuación veremos algunos ejemplos sobre cómo consumir una API en Python con la ayuda de la librería Requests de Python
y la API gratuita de jsonplaceholder que proporciona datos simulados, para esto necesitas instalar esta la librería 
de requests en tu ordenador, puedes instalarla con el siguiente comando:

pip install requests

Esta librería te permite acceder a la información obtenida desde una API de una forma muy sencilla, 
estos son algunos de los métodos y propiedades más comunes para acceder a la información que retornan las peticiones:

Propiedad	            Descripción
response.status_code	Contiene el código de status de la petición, ejemplo: 201
response.url	        Contiene la URL de la petición.
response.headers	    Proporciona los headers de la petición.
response.cookies	    Proporciona las cookies de la petición.
response.encoding	    Contiene la codificación de la petición, ejemplo: utf-8.
response.json()	        Guarda la información que viene desde la API, por ejemplo, en la API del clima, 
                        una lista de diccionarios con la información de las ciudades.

Nota importante, las peticiones a la API de jsonplaceholder sólo simulan el comportamiento de una API real, 
no todas las peticiones son funcionales, por ejemplo, si hacer una petición de tipo POST la API de jsonplaceholder 
la información NO se guardará en los servidores de la API pero la API te responde con un mensaje que simula que si.
----------------------------------------------

¿Cómo consumir una API en Python usando requests?

En el mundo del desarrollo moderno es muy común hacer uso de una API (Application Programming Interface) 
para conectarse a servicios de terceros. Por ejemplo, si estas creando una aplicación donde necesitas 
rastrear la ubicación de los usuarios, en lugar de escribir todo el código necesario para eso, 
puedes simplemente hacer uso de la API de google maps.

En este artículo veremos cómo consumir una API en Python con ayuda de la librería Requests. 
En el siguiente ejemplo veremos un caso sencillo de una petición GET a la API gratuita de jsonplaceholder.

Para poder hacer uso de la librería Requests primero debemos instalarla en nuestro ordenador, 
para eso puedes utilizar el siguiente comando:

"""

#import requests

"""
Una vez instalada, ya podemos usarla en nuestro código para hacer pedidos HTTP, en este caso, 
un pedido GET de un usuario de ejemplo.
"""

# URL = "https://jsonplaceholder.typicode.com/users/1"
# response = requests.get(URL)

# if response.status_code == 200:
#     print('Solicitud exitosa')
#     print('Data:', response.json())

#     ###########################
#     print("------------------> ", response.json()['name'])
#     print("------------------> ", response.json().get('username'))
#     print("headers -> ", response.headers)
#     print("url -> ", response.url)

#     ############################

# else:
#     print('Error en la solicitud, detalles:', response.text)


"""
En este ejemplo, hacemos uso del método get(api_url) de la librería requests para traer la información 
de un usuario falso proporcionada por la API de jsonplacehorder, este método retorna la información recibida 
desde la API y se guarda en la variable response. Si la solicitud fue exitosa la petición retorna un status_code 
de 2XX (Entre 200 y 299) y la información del usuario, pero si ocurrió algún error en la proceso retorna un 
status_code de 4XX (Entre 400 y 499) y un mensaje con el motivo del error.
"""

# CÓDIGOS DE ESTADO DE RESPUESTA HTTP
# https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status

"""
Ejemplo con la solicitud GET

Las solicitudes de tipo GET se utilizan para traer información de un servidor.
"""
# import requests

# URL = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(URL)

# if response.status_code == 200:
#     data = response.json()

#     print('Solicitud exitosa')
#     print('Data:', data)
#     print('titulo -> ', data['title'])
# else:
#     print('Error en la solicitud, detalles:', response.text)

"""
En este ejemplo, hacemos uso del método get() de la librería requests para traer 
la información de un post simulado por la API de jsonplaceholder, esta información 
será guardada en la variable response, luego con un condicional if else verificamos 
si la petición a la API se realizó de forma correcta, de ser así mostramos la información 
en la consola, de lo contrario imprimimos un mensaje con el error.
"""

# Con error en la url
# import requests

# URL = "https://jsonplaceholder.typicod.com/posts/1"
# response = requests.get(URL)

# if response.status_code == 200:
#     data = response.json()

#     print('Solicitud exitosa')
#     print('titulo -> ', data['title'])
# else:
#     print('Error en la solicitud, detalles:', response.text)

"""
Ejemplo con la solicitud POST

Las solicitudes de tipo POST se utilizan para enviar datos al servidor.
"""

# import requests

# URL = "https://jsonplaceholder.typicode.com/posts"
# DATA = {
#     "title": "Título del ejemplo",
#     "body": "Contenido de un nuevo post",
#     "userId": 1
# }

# response = requests.post(URL, json=DATA)

# if response.status_code == 201:
#     data = response.json()

#     print('Post creado de forma exitosa')
#     print('Respuesta:', data)
# else:
#     print('Error en la solicitud, detalles:', response.text)

"""
En este ejemplo, hacemos uso del método post() de la librería requests 
para crear un nuevo objeto en el servidor, el método post() recibe dos parámetros, 
el primero es la URL de la API y el segundo es la información del objeto que 
queremos crear dentro de un diccionario.
"""

"""
Los status codes para un método POST son típicamente 200 OK (si la solicitud fue exitosa y se procesó) 
o 201 Created (si la solicitud resultó en la creación de un nuevo recurso). Otros códigos 
comunes incluyen 400 Bad Request para un error en la solicitud o 404 Not Found si no se encuentra 
el recurso, aunque este último es menos común en POST.
"""

"""
Ejemplo con la solicitud PUT

Las solicitudes de tipo PUT se utilizan para actualizar datos en el servidor.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/posts/1"
DATA = {
    "title": "Título actualizado",
    "userId": 2
}

#response = requests.put(URL, json=DATA)
response = requests.patch(URL, json=DATA)

if response.status_code == 200:
    data = response.json()

    print('Post actualizado de forma exitosa')
    print('Respuesta:', data)
else:
    print('Error en la solicitud, detalles:', response.text)

"""
Para hacer una solicitud de tipo PUT debemos hacer uso del método put() de la 
librería de requests, este método también recibe dos parámetros, el primero es 
la URL que le indica a la API el objeto en particular que deseas actualizar y 
el segundo parámetro es la información con la que deseas actualizar el objeto.
"""

"""
Ejemplo con la solicitud DELETE

Las solicitudes de tipo DELETE se utilizan para eliminar datos en el servidor.
"""
# import requests

# URL = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.delete(URL)

# if response.status_code == 200:
#     print('Post eliminado de forma exitosa.')
# else:
#     print('Error en la solicitud, detalles:', response.text)

"""
Para realizar una solicitud de tipo DELETE en Python debemos hacer uso del método 
delete() de la librería requests, este método recibe como parámetro la URL que le 
indica a el servidor de la API el objeto en particular que deseas eliminar, normalmente 
las APIs retornan un mensaje que nos indica si el objeto se eliminó de forma correcta o 
no pero la API de jsonplaceholder no retorna un mensaje en particular solo retorna un status_code de 200.
"""

"""
Conclusión

Las APIs desempeñan un papel fundamental en la integración de aplicaciones y el intercambio 
de datos en el mundo del desarrollo de software. En Python la librería Requests nos permite 
interactuar con las APIs de una forma sencilla e intuitiva, en este artículo aprendimos como 
hacer uso de esta librería para hacer peticiones HTTP y así obtener, crear, actualizar o eliminar información 
en una API, ahora ya estás listo/a para consumir una API de forma correcta y hacer uso de sus funcionalidades 
en tus propias aplicaciones.

Enlaces de interés



Para profundizar en cómo consumir APIs en Python, os invito a realizar mi curso interactivo. 
Es una excelente oportunidad para aprender de manera práctica y dominar el uso de la librería requests.
(it's a joke - es una broma)

"""