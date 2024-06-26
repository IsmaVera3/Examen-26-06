import requests
import json
import os
import sys
#os modulo de python para manejar archivos y carpetas mas faciles
os.mkdir("Descargas")
os.mkdir("Imagenes")

response = requests.get("https://fakestoreapi.com/products")#IMPORTANTE colocar enlace fake store api
productos = response.json()


categorias = ["electronics","jewelery","men's clothing"]

CantidadProductos = int(input("ingrese cuantos productos desea obtener => "))
#programacion defensiva
if CantidadProductos == str:
    print("debes ingresar un numero, error")
    sys.exit()

tipoCategoria = input(f"ingrese exactamente el tipo de producto que desea filtrar ({categorias})=> ")
#programacion defensiva
if tipoCategoria == int:
    print("no puedes ingresar un numero, error") 
    sys.exit()


productosfiltrados = []
productosnofiltrados = []

for i in productos:
    if i['category'] == tipoCategoria:
        productosfiltrados.append(i)
        print(productosfiltrados)
    else:
        productosnofiltrados.append(i)
        print(productosnofiltrados)
    if len(productosfiltrados) >= CantidadProductos:
        break

with open("Descargas/productos_filtrados.json", "wb") as file:
    json.dump(productosfiltrados, file)

with open("Descargas/productos_no_filtrados.json", "wb") as file:
    json.dump(productosnofiltrados, file)

for i in productosfiltrados:
    imagen_url = i['image']
    imagen_respuesta = requests.get(imagen_url)#obtengo el url de la imagen
    nombre_imagen = os.path.join("Imagenes", f"{i['id']}.jpg")#nombre archivo imagen
    #guardamos las img en un archivo
    with open(nombre_imagen, "wb") as file:
        file.write(imagen_respuesta.content)

print("listo! el codigo guardo un archivo json llamado descargas y las imagenes en un archivo llamado imagenes")
print(f'los productos filtrados son: {productosfiltrados} y los productos no filtrados son: {productosnofiltrados}')
