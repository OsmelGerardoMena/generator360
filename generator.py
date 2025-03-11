import cv2
import numpy as np
import os

def generar_360(carpeta_imagenes, nombre_salida="panoramica_360.jpg"):
    """
    Genera una imagen 360 a partir de una serie de imágenes en una carpeta.

    Args:
        carpeta_imagenes (str): Ruta a la carpeta que contiene las imágenes.
        nombre_salida (str): Nombre del archivo de salida para la imagen panorámica.
    """

    imagenes = []
    for archivo in sorted(os.listdir(carpeta_imagenes)):
        if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            ruta_archivo = os.path.join(carpeta_imagenes, archivo)
            img = cv2.imread(ruta_archivo)
            if img is not None:
                imagenes.append(img)
            else:
                print(f"Error al leer la imagen: {archivo}")

    if len(imagenes) < 2:
        print("Se necesitan al menos dos imágenes para la costura.")
        return

    stitcher = cv2.Stitcher.create()
    estado, panoramica = stitcher.stitch(imagenes)

    print(f"Estado de la costura: {estado}") # Imprime el estado de la costura

    if estado == cv2.Stitcher_OK:
        cv2.imwrite(nombre_salida, panoramica)
        print(f"Imagen panorámica 360 generada: {nombre_salida}")
    else:
        print("Error al realizar la costura de imágenes.")

if __name__ == "__main__":
    carpeta_imagenes = "imagenes_360"
    if os.path.exists(carpeta_imagenes):
        generar_360(carpeta_imagenes)
    else:
        print(f"Error: La carpeta '{carpeta_imagenes}' no se encontró.")