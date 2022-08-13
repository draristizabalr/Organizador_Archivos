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
        self.modelo_buscar = QFileSystemModel()
        self.modelo_buscar.setRootPath('')
        self.modelo_guardar = QFileSystemModel()
        self.modelo_guardar.setRootPath('')

        # Creamos los árboles de directorios
        self.explorador_buscar = QTreeView()
        self.explorador_buscar.setModel(self.modelo_buscar)
        self.explorador_buscar.setIndentation(20)
        self.explorador_buscar.setAnimated(False)
        self.explorador_buscar.setStyleSheet('QTreeView{font-size: 13pt;}')
        self.explorador_buscar.setSortingEnabled(False)
        self.explorador_buscar.setColumnWidth(0, 500)

        self.explorador_guardar = QTreeView()
        self.explorador_guardar.setModel(self.modelo_guardar)
        self.explorador_guardar.setIndentation(20)
        self.explorador_guardar.setAnimated(False)
        self.explorador_guardar.setStyleSheet('QTreeView{font-size: 13pt;}')
        self.explorador_guardar.setSortingEnabled(False)
        self.explorador_guardar.setColumnWidth(0, 500)

        # Agregamos una caja de texto donde agregar el nombre del archivo
        self.nombre_archivo = QLineEdit()

        # Creamos los botones
        boton_buscar = QPushButton('Seleccionar carpeta')
        boton_buscar.setStyleSheet('QPushButton{font-size: 14pt;}')
        boton_buscar.clicked.connect(self.imprimir_direccion)

        boton_guardar = QPushButton('Seleccionar carpeta')
        boton_guardar.setStyleSheet('QPushButton{font-size: 14pt;}')

        boton_una_carpeta = QPushButton('Carpeta principal')
        boton_una_carpeta.setStyleSheet('QPushButton{font-size: 16pt;}')
        boton_una_carpeta.clicked.connect(self.analisis_una_carpeta)

        boton_todas_carpetas = QPushButton('Carpeta principal y subcarpetas')
        boton_todas_carpetas.setStyleSheet('QPushButton{font-size: 16pt;}')

        # Creamos las etiquetas
        etiqueta_analizar = QLabel('Buscar en:')
        etiqueta_analizar.setStyleSheet('QLabel{font-size: 20pt;}')
        etiqueta_destino = QLabel('Guardar en:')
        etiqueta_destino.setStyleSheet('QLabel{font-size: 20pt;}')
        # etiqueta_nombre_archivo = QLabel('Nombre del archivo que se va a generar:')
        # etiqueta_nombre_archivo.setStyleSheet('QLabel{font-size: 15pt;}')

        # Agregamos los botones al layout
        layout.addWidget(boton_buscar, 2, 2)
        layout.addWidget(boton_guardar, 4, 2)
        layout.addWidget(boton_una_carpeta, 5, 1)
        layout.addWidget(boton_todas_carpetas, 5, 2)

        # Agregamos los otros objetos al layout
        layout.addWidget(etiqueta_analizar, 1, 1)
        layout.addWidget(self.explorador_buscar, 2, 1)
        layout.addWidget(etiqueta_destino, 3, 1)
        layout.addWidget(self.explorador_guardar, 4, 1)
        # layout.addWidget(etiqueta_nombre_archivo, 5, 1)
        # layout.addWidget(self.nombre_archivo, 6, 1)

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

    def imprimir_direccion(self):
        print('Está conectado')
        print(self.modelo_buscar.rootPath())


if __name__ == '__main__':
    app = QApplication([])
    ventana = Window()
    ventana.show()
    app.exec()
