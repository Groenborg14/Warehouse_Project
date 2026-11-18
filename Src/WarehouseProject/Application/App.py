from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel
import pandas as pd
import WareListViewer as WareListViewer
import WarehouseViewer as WarehouseViewer


import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Warehouse Optimizer")
        self.resize(1400,900)

        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        #Setup page container
        self.pages = QStackedWidget()

        #Create Pages

        main_menu = QLabel("Main Menu")
        warehouse_viewer = QLabel("Warehouse Viewer")
        settings = QLabel("Settings")
        optimizer = QLabel("Optimizer")

        # add pages to the stacked widget
        self.pages.addWidget(main_menu)
        self.pages.addWidget(warehouse_viewer)
        self.pages.addWidget(settings)
        self.pages.addWidget(optimizer)

        # Nav bar buttons
        page_names = ["Main Menu", 
                      "Warehouse Viewer", 
                      "Settings", 
                      "Optimizer"]


        # Setup top navigation bar
        nav_bar = QWidget()
        nav_bar_layout = QHBoxLayout(nav_bar)
        nav_bar_layout.setSpacing(5)
        nav_bar_layout.addStretch() 
        nav_bar_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        
        for i, name in enumerate(page_names):
            button = QPushButton(name)
            button.clicked.connect(lambda checked, index=i: self.pages.setCurrentIndex(index))
            nav_bar_layout.addWidget(button)

        nav_bar_layout.addStretch() 

        #nav_vbox = QVBoxLayout()
        #nav_vbox.addStretch(2) 
        #nav_vbox.addLayout(nav_bar)
        

        main_layout.addWidget(nav_bar)
        main_layout.addWidget(self.pages, 1)

        self.pages.setCurrentIndex(0)  # Set the initial page to the main menu


        #left side: ware list viewer
        #ware_list_viewer = WareListViewer.WareList()

        #right side: placeholder for future visualizations
        #warehouse_view = WarehouseViewer.WarehouseViewer()

        #main_layout.addWidget(ware_list_viewer)
        #main_layout.addWidget(warehouse_view,1)

        self.setCentralWidget(central_widget)

app = QApplication(sys.argv)


window = MainWindow()


window.show()
app.exec()


