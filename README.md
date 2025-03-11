# Generador de Imágenes 360

Este proyecto genera imágenes panorámicas de 360 grados a partir de una serie de imágenes de entrada.

## Instalación

1.  Clona el repositorio: `git clone https://github.com/OsmelGerardoMena/generator360.git`
2.  Crea un entorno virtual (recomendado): `python3 -m venv venv`
3.  Activa el entorno virtual:
    * En macOS/Linux: `source venv/bin/activate`
    * En Windows: `venv\Scripts\activate`
4.  Instala las dependencias: `pip install -r requirements.txt`

## Uso

1.  Coloca tus imágenes de entrada en la carpeta `imagenes_360/`.
2.  Ejecuta el script: `python3 generador_360/generador.py`
3.  La imagen panorámica resultante se guardará como `panoramica_360.jpg` en el directorio raíz.

## Dependencias

* OpenCV
* NumPy

## Autor

Osmel Mena