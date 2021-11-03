from imgurpython import ImgurClient
from concurrent.futures import ThreadPoolExecutor
import os
import urllib.request
import timeit
 
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
 
cliente = ImgurClient(id_cliente, secreto_cliente)
 
# Metodo para la descarga url imagen
# Datos necesarios del metodo
# Nombre de la imagen => yntdWAr
# Formato de la imagen => png
 
 
def descarga_url_img(link):
   print(link)
   # Con esto ya podemos obtener el corte de la url imagen
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   print(nombre_img, formato_img)
   url_local = "C:/Users/humbe/Pictures/xd/{}.{}"
   #Guardar nne local las imagenes
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))
 
urls = [] 
def obtenerUrls():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
   

   for imagen in imagenes:
      urls.append(imagen.link)
      #  descarga_url_img(imagen.link)

def multiThread():
   with ThreadPoolExecutor(max_workers=len(urls)) as executor:
      executor.map(descarga_url_img, urls)

def normal():
   for i in range(len(urls)):
      descarga_url_img(urls[i])
 

if __name__ == "__main__":
   obtenerUrls()
   print(f"Multi hilos {timeit.Timer(multiThread).timeit(number=1)}")
   print(f"Proceso normal {timeit.Timer(normal).timeit(number=1)}")
