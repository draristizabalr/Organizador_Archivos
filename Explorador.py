# -*- coding: utf-8 -*-

import os

class Explorador():
    def __init__(self, direccion):
        self._direccion = direccion
    
    @property
    def direccion(self):
        return self._direccion
    
    
    @direccion.setter
    def direccion(self, direccion):
        self.direccion = direccion
    
    def archivos(self):
        archivos = []
        for arch in os.scandir(self.direccion):
            if arch.is_file():
                posicion = 0
                while posicion != len(arch.name):
                    if arch.name[-posicion] == '.' and\
                        arch.name[-posicion:] != '.ini' and\
                        arch.name[-posicion:] != '.sys':
                        archivos.append([arch.name[:-posicion],
                                         arch.name[-posicion:]])
                        break
                    else:
                        posicion += 1
            
        return archivos
    
    def carpetas(self):
        carpetas = []
        for arch in os.scandir(self.direccion):
            if not arch.is_file():
                carpetas.append(arch.name)
            
        return carpetas

    def directorios(self):
        directorios = []
        for arch in os.scandir(self.direccion):
            directorios.append(arch.path)

        return directorios

    def tamaños(self):
        tamaños_b = []
        for arch in os.scandir(self.direccion):
            if arch.is_file():
                tamaños_b.append(os.path.getsize((arch.path)))

        unidades = ['bytes', 'Kb', 'Mb', 'Gb']
        tamaños = []

        for tamaño in tamaños_b:
            unidad = 0
            while True:
                if tamaño == 0:
                    tamaños.append(f'{tamaño} {unidades[unidad]}')
                    unidad = 0
                    break
                elif tamaño >= (2**(10*unidad)) and tamaño <= (2**(10*(unidad+1))):
                    tamaños.append([round(tamaño*2**(-10*unidad),2),
                                    unidades[unidad]])
                    unidad = 0
                    break
                else:
                    unidad += 1

        return tamaños
    
    def __str__(self):
        return f'La dirección dada es {self.direccion}'
    
if __name__ == '__main__':
    direccion_1 = Explorador('C:/')
    print(direccion_1)
    print(len(direccion_1.archivos()))
    print(direccion_1.archivos())
    print(direccion_1.tamaños())
    print(direccion_1.carpetas())
    print(direccion_1.directorios())
    # direccion_2 = Explorador('C:/David/Trabajos/Documentos/')
    # print(direccion_2)
    # print(direccion_2.archivos())
    # print(direccion_2.tamaños())
    # print(direccion_2.carpetas())
    # print(direccion_2.directorios())
    # direccion_3 = Explorador('C:/Users/zulac/Videos')
    # print(direccion_3)
    # print(direccion_3.archivos())
    # print(direccion_3.tamaños())
    # print(direccion_3.carpetas())
    # print(direccion_3.directorios())
    #
    #
    #
    #
