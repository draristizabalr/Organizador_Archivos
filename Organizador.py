# -*- coding: utf-8 -*-

from Explorador import Explorador


class Organizador():
    def __init__(self, Explorador):
        self._archivos = Explorador.archivos()
        self._carpetas = Explorador.carpetas()
        self._tamaños = Explorador.tamaños()
        self._directorios = Explorador.directorios()

    @property
    def archivos(self):
        return self._archivos

    @property
    def carpetas(self):
        return self._carpetas

    @property
    def tamaños(self):
        return self._tamaños

    @property
    def directorios(self):
        return self._directorios

    @property
    def lista_archivos(self):
        lista = []
        posicion = 0
        while True:
            try:
                lista.append([self.archivos[posicion][0], self.archivos[posicion][1],
                              self.tamaños[posicion][0], self.tamaños[posicion][1],
                              self.directorios[posicion]])
                posicion += 1
            except IndexError:
                break

        return lista

    def __str__(self):
        lista_print = []
        for posicion in range(len(self.archivos)):
            lista_print.append([self.archivos[posicion][0], self.archivos[posicion][1],
                          self.tamaños[posicion][0], self.tamaños[posicion][1],
                          self.directorios[posicion]])
        texto = ''
        for posicion in range(len(self.archivos)):
            texto += f'Archivo #{posicion + 1}\n'\
                    f'Nombre archivo: {lista_print[posicion][0]}\n'\
                    f'Tipo de archivo: {lista_print[posicion][1]}\n'\
                    f'Tamaño archivo: {lista_print[posicion][2]} {lista_print[posicion][3]}\n' \
                    f'Dirección archivo: {lista_print[posicion][4]}\n\n'

        for posicion in range(len(self.carpetas)):
            texto += f'Carpeta #{posicion + 1}\n'\
                    f'Nombre carpeta: {self.carpetas[posicion]}\n\n'

        return texto


if __name__ == '__main__':
    df_1 = Organizador(Explorador('C:/David/Trabajos/'))
    print(df_1.lista_archivos)
    print(df_1)

