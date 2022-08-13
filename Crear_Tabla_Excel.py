from Exportador import Exportador


def Crear_Tabla_Excel(direccion_analisis, direccion_entrega, nombre_archivo):
    direccion_analisis = direccion_analisis.replace('\\', '/')
    direccion_entrega = direccion_entrega.replace('\\', '/')
    df = Exportador(direccion_analisis)
    df.exportar_excel(f'{direccion_entrega}/{nombre_archivo}.xlsx')
    print('El archivo está en la dirección')
    print(direccion_entrega)

if __name__ == '__main__':
    Crear_Tabla_Excel('C:/', 'C:/David/Programas/Programa Santiago/', 'Archivo')
