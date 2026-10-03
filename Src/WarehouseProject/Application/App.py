from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget
import pandas as pd
import WareListViewer as WareListViewer
import WarehouseViewer as WarehouseViewer


import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Warehouse Visualizer")
        self.resize(1400,900)

        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)


        #left side: ware list viewer
        ware_list_viewer = WareListViewer.WareList()

        #right side: placeholder for future visualizations
        warehouse_view = WarehouseViewer.WarehouseViewer()

        main_layout.addWidget(ware_list_viewer)
        main_layout.addWidget(warehouse_view,1)

        self.setCentralWidget(central_widget)

app = QApplication(sys.argv)


window = MainWindow()


window.show()
app.exec()


