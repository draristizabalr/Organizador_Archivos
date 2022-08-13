from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedLayout, QWidget, \
    QLabel, QGridLayout, QLineEdit, QTreeView, QFileSystemModel

from Exportador import Exportador


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Agregamos las características a nuestra ventana
        self.setWindowTitle('Crear índice de archivos')
        self.showFullScreen()

        # Creamos nuestros layouts
        layout = QGridLayout()

        # Creamos objeto lector de archivos
        self.modelo = QFileSystemModel()
        self.modelo.setRootPath('')

        # Creamos los árboles de directorios
        self.explorador_analizar = QTreeView()
        self.explorador_analizar.setModel(self.modelo)
        self.explorador_analizar.setIndentation(20)
        self.explorador_analizar.setAnimated(False)
        self.explorador_analizar.setStyleSheet('QTreeView{font-size: 13pt;}')
        self.explorador_analizar.setSortingEnabled(False)
        self.explorador_analizar.setColumnWidth(0, 500)
        self.explorador_entrega = QTreeView()
        self.explorador_entrega.setModel(self.modelo)
        self.explorador_entrega.setIndentation(20)
        self.explorador_entrega.setAnimated(False)
        self.explorador_entrega.setStyleSheet('QTreeView{font-size: 13pt;}')
        self.explorador_entrega.setSortingEnabled(False)
        self.explorador_entrega.setColumnWidth(0, 500)

        self.nombre_archivo = QLineEdit()

        # Creamos los botones
        boton_carpeta_analizar = QPushButton('Seleccionar carpeta')
        boton_carpeta_entrega = QPushButton('Seleccionar carpeta')
        boton_una_carpeta = QPushButton('Carpeta principal')
        boton_una_carpeta.clicked.connect(self.analisis_una_carpeta)
        boton_todas_carpetas = QPushButton('Carpeta principal y subcarpetas')


        # Creamos las etiquetas
        etiqueta_analizar = QLabel('Buscar en:')
        etiqueta_analizar.setStyleSheet('QLabel{font-size: 20pt;}')
        etiqueta_destino = QLabel('Guardar en:')
        etiqueta_destino.setStyleSheet('QLabel{font-size: 20pt;}')
        etiqueta_nombre_archivo = QLabel('Nombre del archivo que se va a generar:')

        # Agregamos los botones al layout
        layout.addWidget(boton_carpeta_analizar, 2, 2)
        layout.addWidget(boton_carpeta_entrega, 4, 2)
        layout.addWidget(boton_una_carpeta, 5, 2)
        layout.addWidget(boton_todas_carpetas, 6, 2)

        # Agregamos los otros objetos al layout
        layout.addWidget(etiqueta_analizar, 1, 1)
        layout.addWidget(self.explorador_analizar, 2, 1)
        layout.addWidget(etiqueta_destino, 3, 1)
        layout.addWidget(self.explorador_entrega, 4, 1)
        layout.addWidget(etiqueta_nombre_archivo, 5, 1)
        layout.addWidget(self.nombre_archivo, 6, 1)

        # Creamos un componente genérico para publicar
        componente = QWidget()
        componente.setLayout(layout)

        # Publicamos el componente
        self.setCentralWidget(componente)

    def analisis_una_carpeta(self):
        direccion_analisis = self.direccion_analizar.text()
        direccion_entrega = self.direccion_entrega.text()
        nombre_archivo = self.nombre_archivo.text()
        direccion_analisis = direccion_analisis.replace('\\', '/')
        direccion_entrega = direccion_entrega.replace('\\', '/')
        df = Exportador(direccion_analisis)
        df.exportar_excel(f'{direccion_entrega}/{nombre_archivo}.xlsx')


if __name__ == '__main__':
    app = QApplication([])
    ventana = Window()
    ventana.show()
    app.exec()
