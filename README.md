# Pildora API Rest y CRUD

## Presentación
enlace a la presentación https://gamma.app/docs/Introduccion-a-API-REST-y-CRUD-Fundamentos-Esenciales-4ofewad9ssvi17b

## ¿Qué es una API?

✔ Definición

Una API (Application Programming Interface) es un conjunto de reglas que permite que dos aplicaciones se comuniquen entre sí.

Ejemplos:

    • Una app del clima consultando un servidor de meteorología.

    • Un frontend web pidiéndole datos a un backend.

## ¿Qué es una API REST?

✔ Definición API Web / API REST

Cuando hablamos de API REST generalmente nos referimos a APIs que funcionan sobre HTTP siguiendo ciertos principios:

📌 Principios REST

    • Cliente - Servidor: Frontend y backend separados.

    • Sin estado (stateless): Cada petición contiene toda la información necesaria.

    • Recursos: Todo se modela como recursos (usuarios, productos, posts…).

    • Uso de métodos HTTP: GET, POST, PUT, DELETE.

    • Respuestas en JSON.

## CRUD y su relación con REST
📚 CRUD es un acrónimo que describe las 4 operaciones básicas sobre datos:
| Operación | Acción  | Método HTTP |
|-----------|---------|-------------|
| Create | Crear | POST |
| Read | Leer | GET |
| Update | Actualizar | PUT/PATCH |
| Delete | Eliminar | DELETE |

En una API REST, cada uno de estos métodos se aplica a un recurso.
Ejemplo con recurso usuarios:

    • GET /usuarios → obtener usuarios

    • POST /usuarios → crear usuario

    • PUT /usuarios/1 → actualizar usuario con id=1

    • DELETE /usuarios/1 → borrar usuario con id=1


## Taller práctico

### Cómo funciona api rest en python:

Una API REST en Python funciona mediante la comunicación del servidor y el cliente a través de peticiones HTTP. 
Para crearla, se pueden usar frameworks como Flask o FastAPI, que permiten crear "endpoints" (rutas) y 
asociarles funciones que manejan verbos HTTP como GET (para leer), POST (para crear), PUT (para actualizar) 
y DELETE (para borrar). 

Los datos generalmente se intercambian en formato JSON, y se utilizan bibliotecas como **requests** 
para que otras aplicaciones en Python puedan interactuar con la API.

**En este taller vamos a usar el sitio JSON placeholder**

jsonplaceholder es una API gratuita que ofrece datos ficticios como fotos, 
publicaciones, comentarios, datos de usuarios falsos y rutas para poder practicar.

sitio web : https://jsonplaceholder.typicode.com/

Por ejemplo para trabajar con los posts la URL es la siguiente : https://jsonplaceholder.typicode.com/posts

## Para realizar las pruebas podemos preparar un entorno virtual de python en la carpeta donde queramos hacer las pruebas o instalar request de manera global.

Podemos crear la carpeta de nombre **api_rest**

Nos metemos en dicha carpeta y ejecutamos los siguientes comandos para crear elentorno virtual en python y activarlo.

    python -m venv venv
    source venv/Scripts/activate

<u>**¿Cómo consumir una API?**</u>

Durante este taller vamos a ver algunos ejemplos sobre cómo consumir una API en Python con la ayuda de la librería **requests** de Python y la API gratuita de jsonplaceholder que proporciona datos simulados; para hacer las pruebas necesitamos instalar la librería 
de requests en el ordenador, podemos instalarla con el siguiente comando:

    pip install requests

Esta librería nos permite acceder a la información obtenida desde una API de una forma muy sencilla, 
estos son algunos de los métodos y propiedades más comunes para acceder a la información que retornan las peticiones:

| Propiedad            | Descripción                                               |
|----------------------|-----------------------------------------------------------|
| response.status_code | Contiene el código de status de la petición, ejemplo: 201 |
| response.url         | Contiene la URL de la petición.                           |
| response.headers	   | Proporciona los headers de la petición.                   |
| response.cookies	   | Proporciona las cookies de la petición.                   |
| response.encoding	   | Contiene la codificación de la petición, ejemplo: utf-8.  |
| response.json()	   | Guarda la información que viene desde la API, por ejemplo, en la API de los posts, devuelve una lista de diccionarios con la información de los posts. |

# Vamos a hacer algún ejemplo

> Nota importante : las peticiones a la API de jsonplaceholder sólo simulan el comportamiento de una API real, 
no todas las peticiones son funcionales; por ejemplo, si hacemos una petición de tipo POST a la API de jsonplaceholder 
la información NO se guardará en los servidores de la API pero la API te responde con un mensaje que simula que si.

<u>**¿Preparados para consumir una API en Python usando requests?**</u>

En la programación actual es muy común hacer uso de una API para conectarse a servicios de terceros. 
Por ejemplo, si estas creando una aplicación donde necesitas 
mostrar el tiempo que hace, en vez de escribir todo el código necesario para eso, 
puedes simplemente hacer uso de la API que muestre el tiempo.

En este taller vamos a ver cómo consumir una API en Python con ayuda de la librería **requests**.

En el siguiente ejemplo veremos un caso sencillo de una petición GET a la API gratuita de jsonplaceholder.

Debemos crear un fichero de python con la extensión **py**, por ejemplo jsonplaceholder.py

Para poder hacer uso de la librería **requests** primero tenemos que importarla en nuestro archivo, 
para eso debemos usar el siguiente comando:

    import requests
 
Con el código de abajo vamos a hacer una petición GET de un usuario de ejemplo, en este caso el usuario 1.

    URL = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(URL)

    if response.status_code == 200:
        print('Solicitud exitosa')
        print('Data:', response.json())

        print("------------------> ", response.json()['name'])
        print("------------------> ", response.json().get('username'))
        print("headers -> ", response.headers)
        print("url -> ", response.url)

    else:
        print('Error en la solicitud, detalles:', response.text)

En este ejemplo, hemos usado el método get(api_url) de la librería requests para traer la información 
de un usuario falso de id=1 proporcionada por la API de jsonplacehorder, este método devuelve la información recibida 
desde la API y se guarda en la variable response. Si la solicitud fue exitosa la petición retorna un status_code 
de 2XX (Entre 200 y 299) y la información del usuario, pero si ocurrió algún error en el proceso retorna un 
status_code de 4XX (Entre 400 y 499) y un mensaje con el motivo del error.

En este ejemplo también se devuelve el name y el username de 2 maneras diferentes de obtener los datos de un json.

Y finalmente se imprimen los headers y la url.

> *CÓDIGOS DE ESTADO DE RESPUESTA HTTP*  
enlace a los códigos de estado https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status

# Vamos a hacer varios ejemplos con JSON para ver su forma en array y en objeto

**PokeApi**

Página web general con información de la API : https://pokeapi.co/

Ejemplo de API con datos del pokemon ditto (devuelve diccionario) -> https://pokeapi.co/api/v2/pokemon/ditto

**COVID**

Página web general con información de la API : https://api.covidtracking.com

Ejemplo de API con datos del covid (devuelve array) -> https://api.covidtracking.com/v1/us/daily.json


## A continuación haremos unos ejemplos de GET, POST, PUT y DELETE

**Ejemplo con la solicitud GET**

Las solicitudes de tipo GET se utilizan para traer información de un servidor.

    import requests

    URL = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        print('Solicitud exitosa')
        print('Data:', data)
        print('titulo -> ', data['title'])
    else:
        print('Error en la solicitud, detalles:', response.text)

En este ejemplo, hacemos uso del método get(URL) de la librería requests para traer 
la información de un post con id=1 simulado por la API de jsonplaceholder, esta información 
será guardada en la variable response, luego con un condicional if else verificamos 
si la petición a la API se realizó de forma correcta, de ser así mostramos la información 
en la consola, de lo contrario imprimimos un mensaje con el error.

**Ejemplo con error en la url de la petición GET**

    import requests

    URL = "https://jsonplaceholder.typicod.com/posts/1"
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        print('Solicitud exitosa')
        print('Data:', data)
        print('titulo -> ', data['title'])
    else:
        print('Error en la solicitud, detalles:', response.text)

En este ejemplo ponemos un URL incorrecta para que de error.

**Ejemplo con la solicitud POST**

Las solicitudes de tipo POST se utilizan para enviar datos al servidor.

    import requests

    URL = "https://jsonplaceholder.typicode.com/posts"
    DATA = {
        "title": "Título del ejemplo",
        "body": "Contenido de un nuevo post",
        "userId": 1
    }

    response = requests.post(URL, json=DATA)

    if response.status_code == 201:
        data = response.json()

        print('Post creado de forma exitosa')
        print('Respuesta:', data)
    else:
        print('Error en la solicitud, detalles:', response.text)

En este ejemplo, hacemos uso del método post(URL, DATA) de la librería requests 
para crear un nuevo objeto en el servidor, el método post(URL, DATA) recibe dos parámetros, 
el primero es la URL de la API y el segundo es la información del objeto que 
queremos crear dentro de un diccionario.

> Nota : Los status codes para un método POST son típicamente 200 OK (si la solicitud fue exitosa y se procesó) 
o 201 Created (si la solicitud resultó en la creación de un nuevo recurso). Otros códigos 
comunes incluyen 400 Bad Request para un error en la solicitud o 404 Not Found si no se encuentra 
el recurso, aunque este último es menos común en POST.

**Ejemplo con la solicitud PUT (PATCH)**

Las solicitudes de tipo PUT se utilizan para actualizar datos en el servidor.

    import requests

    URL = "https://jsonplaceholder.typicode.com/posts/1"
    DATA = {
        "title": "Título actualizado",
        "userId": 2
    }

    response = requests.put(URL, json=DATA)

    if response.status_code == 200:
        data = response.json()

        print('Post actualizado de forma exitosa')
        print('Respuesta:', data)
    else:
        print('Error en la solicitud, detalles:', response.text)

Para hacer una solicitud de tipo PUT debemos hacer uso del método put(URL, DATA) de la 
librería de requests, este método también recibe dos parámetros, el primero es 
la URL que le indica a la API el objeto en particular que deseas actualizar y 
el segundo parámetro es la información con la que deseas actualizar el objeto.

En este ejemplo accedemos al post con **id=1** y estamos modificando el **title** y el **userId**.

> Nota : La diferencia principal entre PUT y PATCH es que
PUT reemplaza completamente un recurso (debes enviar el objeto entero, aunque solo cambies un campo), mientras que PATCH aplica modificaciones parciales (solo envías los campos que quieres cambiar), lo cual es más eficiente para actualizaciones menores. PUT es una actualización "todo o nada", mientras que PATCH es una actualización selectiva o "parche".

> Nota : Pero PATCH a veces da problemas con algunos navegadores y frameworks.

**Ejemplo con la solicitud DELETE**

Las solicitudes de tipo DELETE se utilizan para eliminar datos en el servidor.

    import requests

    URL = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(URL)

    if response.status_code == 200:
        print('Post eliminado de forma exitosa.')
    else:
        print('Error en la solicitud, detalles:', response.text)

Para realizar una solicitud de tipo DELETE en Python debemos hacer uso del método 
delete(url) de la librería requests, este método recibe como parámetro la URL que le 
indica a el servidor de la API el objeto en particular que deseas eliminar, normalmente 
las APIs retornan un mensaje que nos indica si el objeto se eliminó de forma correcta o 
no pero la API de jsonplaceholder no retorna un mensaje en particular solo retorna un status_code de 200.

En este ejemplo estamos borrando el post de **id=1**.

### Conclusión

Las APIs desempeñan un papel fundamental en la integración de aplicaciones y el intercambio 
de datos en el mundo del desarrollo de software. En Python la librería **requests** nos permite 
interactuar con las APIs de una forma sencilla e intuitiva, en este taller aprendimos como 
hacer uso de esta librería para hacer peticiones HTTP y así obtener, crear, actualizar o eliminar información 
en una API, ahora ya estás listo/a para consumir una API de forma correcta y hacer uso de sus funcionalidades 
en tus propias aplicaciones.

### Enlaces de interés

1.- Artículo de 4geeks en el cual me he basado.

https://4geeks.com/es/how-to/como-consumir-una-api-en-python

2.- Este video te enseña a consumir una API usando la librería requests en Python. Video de 2:26 minutos de Juan Esquivel Méndez

https://www.youtube.com/watch?v=AYaVr6Z-VoI

3.- Este video te introduce a como usar FastApi.

https://www.youtube.com/watch?v=J0y2tjBz2Ao

4.- request para humanos

https://requests.readthedocs.io/projects/es/es/latest/user/quickstart.html


