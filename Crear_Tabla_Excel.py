import os
from Exportador import Exportador

direccion = str(input('Escribir dirección de la carpeta: '))

print(direccion)
df = Exportador(direccion)
print(df.datos)

nombre = str(input('Nombre del archivo a crear: '))
df.exportar_excel(nombre)

print('El archivo está en la dirección')
print((os.path.expanduser('~/Desktop')+f'/{nombre}.xlsx').replace('\\', '/'))
