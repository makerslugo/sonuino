# sonuino

La demo consiste en una página web con datos de Roll, Pitch y Yaw que se
actualizan cada segundo de manera indefinida. Está hecha usando WebSockets,
SocketIO y Flask.

## Cómo probar

Descargar el proyecto

    $ git clone https://github.com/makerslugo/sonuino.git

    # como alternativa al paso anterior, descargar el zip desde
    # https://github.com/makerslugo/sonuino/archive/master.zip

Crear un entorno de ejecución

    $ cd sonuino
    $ virtualenv venv
    $ . venv/bin/activate

Arrancar el servidor

    $ pip install -r requirements.txt
    $ python app.py

Visitar localhost:5000 con un navegador
