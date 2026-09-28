\# Portal Fútbol - EVA2



Portal Fútbol es una aplicación web desarrollada con Django para la asignatura Programación Back End.



El proyecto permite visualizar información de jugadores y equipos de fútbol, utilizando una base de datos relacional MySQL y el ORM de Django.



\## Funcionalidades



\- Página de inicio.

\- Listado de jugadores.

\- Listado de equipos.

\- Relación entre jugadores y equipos.

\- Administración de jugadores y equipos mediante Django Admin.

\- Búsqueda y filtros desde el panel de administración.

\- Información obtenida desde MySQL mediante el ORM de Django.

\- Interfaz desarrollada utilizando Bootstrap.



\## Tecnologías utilizadas



\- Python

\- Django

\- MySQL

\- HTML

\- CSS

\- Bootstrap

\- Git

\- GitHub



\## Base de datos



El proyecto utiliza MySQL como sistema de base de datos.



Las credenciales de conexión se administran mediante variables de entorno utilizando un archivo `.env`, el cual no se encuentra incluido en el repositorio por motivos de seguridad.



\## Modelos principales



\### Equipo

\- Nombre

\- País



\### Jugador

\- Nombre

\- Posición

\- Nacionalidad

\- Equipo

\- Imagen



Cada jugador se encuentra relacionado con un equipo mediante una relación `ForeignKey`.



\## Aplicaciones Django



El proyecto contiene las aplicaciones:



\- `futbol`

\- `equipos`



Estas permiten organizar las distintas funcionalidades del sitio.



\## Ejecución del proyecto



Crear y activar un entorno virtual e instalar las dependencias:



```powershell

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

python -m pip install -r requirements.txt



Luego configurar las variables de entorno necesarias para la conexión a MySQL y ejecutar:



python manage.py migrate

python manage.py runserver



El sitio estará disponible localmente en:

http://127.0.0.1:8000/

Autor

Vicente Salazar Araya

INACAP Sede La Serena

