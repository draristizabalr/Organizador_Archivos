import pandas as pd
from Organizador import Organizador

class Exportador(Organizador):

    titulos = ['Nombre', 'Tipo de Archivo', 'Tamaño', 'Unidad', 'Dirección']

    def __init__(self, direccion):
        super().__init__(direccion)
        self._datos = pd.DataFrame(self.lista_archivos,
                                   columns=Exportador.titulos)

    @property
    def datos(self):
        return self._datos

    def exportar_excel(self, direccion):
        df = self.datos
        df.to_excel(direccion, engine='openpyxl', index=False, sheet_name='Carpeta Principal')


if __name__ == '__main__':
    direccion_1 = 'C:/'
    df = Exportador(direccion_1)
    print(df.datos)
    print(df.carpetas())
    df.exportar_excel('C:/David/Programas/Index.xlsx')
    df.escribir_excel('C:/David/Programas/Index.xlsx')


