# Sistema de Proyectos

Sistema de Proyectos es una aplicación web desarrollada en Python con el framework Django que te permite gestionar y hacer un seguimiento de tus proyectos de manera eficiente.

## Características

- Registro y autenticación de usuarios.
- Creación, edición y eliminación de proyectos.
- Asignación de tareas a proyectos.
- Seguimiento del progreso de las tareas.
- ...

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.x
- Django (ver el archivo `requirements.txt` para las dependencias específicas)

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto:

1. Clona el repositorio: git clone https://github.com/Danield05/SistemaDeProyectos.git
cd SistemaDeProyectos

2. Crea un entorno virtual (opcional pero recomendado): python -m venv venv
source venv/bin/activate # En sistemas Unix/Linux
venv\Scripts\activate # En Windows

3. Instala las dependencias: pip install -r requirements.txt
   
4. Realiza las migraciones de la base de datos:
python manage.py makemigrations
python manage.py migrate


5. Inicia el servidor de desarrollo: python manage.py runserver

6. Accede a la aplicación en tu navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Uso

1. Regístrate o inicia sesión en la aplicación.
2. Crea un proyecto.
3. Agrega tareas al proyecto.
4. Realiza un seguimiento del progreso de las tareas.

Si deseas contribuir al desarrollo de este proyecto, por favor sigue estas pautas:

- Haz un fork del repositorio.
- Crea una nueva rama para tu contribución.
- Realiza tus cambios y asegúrate de seguir las guías de estilo.
- Envía una solicitud de extracción (Pull Request) describiendo tus cambios.

## Licencia

Este proyecto se distribuye bajo la licencia [Tu Licencia]. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

## Contacto

Si tienes preguntas, sugerencias o comentarios, no dudes en ponerte en contacto con el equipo de desarrollo a través de [joseaquino971@gmail.com].





