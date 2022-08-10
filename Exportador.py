import os.path

import pandas as pd
from Organizador import Organizador
from Explorador import Explorador

class Exportador():

    def __init__(self, direccion):
        titulos = ['Nombre', 'Tipo de Archivo', 'Tamaño', 'Unidad', 'Dirección']
        self._direccion = direccion
        self._datos = pd.DataFrame(Organizador(Explorador(direccion)).lista_archivos,
                                   columns=titulos)

    @property
    def datos(self):
        return self._datos

    @property
    def direccion(self):
        return self._direccion

    def exportar_excel(self, nombre):
        df = self.datos
        direccion_salida = (os.path.expanduser('~/Desktop')+f'/{nombre}.xlsx').\
                            replace('\\', '/')
        df.to_excel(direccion_salida,
                    engine='openpyxl',
                    index=False)


if __name__ == '__main__':
    direccion_1 = 'C:/'
    df = Exportador(direccion_1)
    print(df.datos)
    df.exportar_excel


