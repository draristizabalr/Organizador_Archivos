from openpyxl import load_workbook
import pandas as pd
from PySide6.QtCore import Qt, QDir
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedLayout, QWidget, \
    QLabel, QGridLayout, QLineEdit, QTreeView, QFileSystemModel, QMessageBox

from Exportador import Exportador


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.direccion_buscar = ''

        # Agregamos las características a nuestra ventana
        self.setWindowTitle('Crear índice de archivos')
        self.setMinimumSize(1200, 900)

        # Creamos nuestros layouts
        layout_principal = QGridLayout()
        primer_layout = QGridLayout()
        segundo_layout = QGridLayout()

        # Damos las propiedades a los layouts

        # Creamos objeto lector de archivos
        self.modelo_buscar = QFileSystemModel()
        self.modelo_buscar.setRootPath('')
        self.modelo_buscar.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)

        self.modelo_guardar = QFileSystemModel()
        self.modelo_guardar.setRootPath('')
        self.modelo_guardar.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)

        # Creamos los árboles de directorios
        self.explorador_buscar = QTreeView()
        self.explorador_buscar.setModel(self.modelo_buscar)
        self.explorador_buscar.setIndentation(20)
        self.explorador_buscar.setAnimated(False)
        self.explorador_buscar.setStyleSheet('QTreeView{font-size: 13pt;'
                                             '          font-family: "Calibri", sans-serif;}')
        self.explorador_buscar.setSortingEnabled(True)
        self.explorador_buscar.sortByColumn(0, Qt.AscendingOrder)
        self.explorador_buscar.setColumnWidth(0, 500)

        self.explorador_guardar = QTreeView()
        self.explorador_guardar.setModel(self.modelo_guardar)
        self.explorador_guardar.setIndentation(20)
        self.explorador_guardar.setAnimated(False)
        self.explorador_guardar.setStyleSheet('QTreeView{font-size: 13pt;'
                                              '          font-family: "Calibri", sans-serif;}')
        self.explorador_guardar.setSortingEnabled(True)
        self.explorador_guardar.sortByColumn(0, Qt.AscendingOrder)
        self.explorador_guardar.setColumnWidth(0, 500)

        # Agregamos una caja de texto donde agregar el nombre del archivo
        self.nombre_archivo = QLineEdit()
        self.nombre_archivo.setStyleSheet('QLineEdit{font-size: 14pt;'
                                          '          font-family: "Calibri", sans-serif;}')

        # Creamos los botones
        self.boton_una_carpeta = QPushButton('Carpeta principal')
        self.boton_una_carpeta.setStyleSheet('QPushButton{font-size: 16pt;'
                                             '          font-family: "Times New Roman", Times, serif;}')
        self.boton_una_carpeta.clicked.connect(self.buscar_carpeta)

        self.boton_todas_carpetas = QPushButton('Carpeta principal y subcarpetas')
        self.boton_todas_carpetas.setStyleSheet('QPushButton{font-size: 16pt;'
                                                '            font-family: "Times New Roman", Times, serif;}')
        self.boton_todas_carpetas.clicked.connect(lambda: self.buscar_carpeta(True))

        # Creamos las etiquetas
        etiqueta_buscar = QLabel('Buscar en:')
        etiqueta_buscar.setStyleSheet('QLabel{font-size: 20pt;'
                                      '       font-family: "Times New Roman", Times, serif;}')

        etiqueta_guardar = QLabel('Guardar en:')
        etiqueta_guardar.setStyleSheet('QLabel{font-size: 20pt;'
                                       '       font-family: "Times New Roman", Times, serif;}')

        etiqueta_nombre_archivo = QLabel('Nombre del archivo que se va a generar:')
        etiqueta_nombre_archivo.setStyleSheet('QLabel{font-size: 15pt;'
                                              '       font-family: "Times New Roman", Times, serif;}')

        # Agregamos los otros objetos al primer_layout
        primer_layout.addWidget(etiqueta_buscar, 1, 1)
        primer_layout.addWidget(self.explorador_buscar, 2, 1)
        primer_layout.addWidget(etiqueta_guardar, 3, 1)
        primer_layout.addWidget(self.explorador_guardar, 4, 1)
        primer_layout.addWidget(etiqueta_nombre_archivo, 5, 1)

        # Agregamos los objetos al segundo_layout
        segundo_layout.addWidget(self.nombre_archivo, 1, 1, 1, 2)
        segundo_layout.addWidget(self.boton_una_carpeta, 2, 1)
        segundo_layout.addWidget(self.boton_todas_carpetas, 2, 2)

        # Agregamos los dos layouts al layout_principal
        layout_principal.addLayout(primer_layout, 1, 1)
        layout_principal.addLayout(segundo_layout, 2, 1)

        # Creamos un componente genérico para publicar
        componente = QWidget()
        componente.setLayout(layout_principal)

        # Publicamos el componente
        self.setCentralWidget(componente)

    def buscar_carpeta(self, todos=False):
        direccion_buscar = self.conseguir_direccion(self.explorador_buscar, self.modelo_buscar)
        direccion_guardar = self.conseguir_direccion(self.explorador_guardar, self.modelo_guardar)

        while True:
            if self.nombre_archivo.text():
                nombre_archivo = self.nombre_archivo.text()
                break
            else:
                return QMessageBox.about(self, 'ERROR', 'Agregar nombre al archivo')

        direccion_buscar = direccion_buscar.replace('\\', '/')
        direccion_guardar = direccion_guardar.replace('\\', '/')
        direccion_guardar = f'{direccion_guardar}/{nombre_archivo}.xlsx'
        df = Exportador(direccion_buscar)
        df.exportar_excel(direccion_guardar)
        if todos:
            libro_excel = load_workbook(direccion_guardar)
            writer = pd.ExcelWriter(direccion_guardar, engine='openpyxl')
            writer.book = libro_excel
            carpetas = df.carpetas()
            for carpeta in carpetas:
                df_n = Exportador(f'{direccion_buscar}/{carpeta}/')
                df_n.datos.to_excel(writer, sheet_name=f'{carpeta}', index=False)

            writer.close()

        return QMessageBox.about(self, '¡Archivo Creado!',
                                 f'El archivo "{nombre_archivo}.xlsx" fue creado exitosamente en:\n\n'
                                 f'{direccion_guardar}')

    def conseguir_direccion(self, explorador: QTreeView, modelo: QFileSystemModel):
        index = explorador.currentIndex()
        return modelo.filePath(index)





if __name__ == '__main__':
    app = QApplication([])
    ventana = Window()
    ventana.show()
    app.exec()
