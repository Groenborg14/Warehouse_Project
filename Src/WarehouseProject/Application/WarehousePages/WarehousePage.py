from PySide6.QtWidgets import QComboBox, QHBoxLayout, QWidget
from .WarehouseView import WarehouseViewer
from .WareListViewer import WareList
from PySide6.QtCore import Qt




class WarehousePage(QWidget):
    def __init__(self):
        super().__init__()

        # Create a horizontal layout for the page
        layout = QHBoxLayout(self)

        # Create the ware list viewer and warehouse viewer
        self.ware_list_viewer = WareList()
        self.warehouse_view = WarehouseViewer()


        selector_layout = QHBoxLayout()
        self.warehouse_selector = QComboBox()

        selector_layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignTop)

        self.warehouse_selector.addItems(["Warehouse 1", "Warehouse 2", "Warehouse 3"]) #input from database or config file in the future

        selector_layout.addWidget(self.warehouse_selector)

        # Add the viewers to the layout
        layout.addWidget(self.ware_list_viewer)
        layout.addWidget(self.warehouse_view, 1)  # Give the warehouse viewer more space
        layout.addLayout(selector_layout)
