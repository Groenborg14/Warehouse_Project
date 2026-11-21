from PySide6.QtWidgets import QHBoxLayout, QWidget, QMainWindow
import WareListViewer as WareListViewer
import WarehouseViewer as WarehouseViewer




class WarehousePage(QWidget):
    def __init__(self):
        super().__init__()

        # Create a horizontal layout for the page
        layout = QHBoxLayout(self)

        # Create the ware list viewer and warehouse viewer
        self.ware_list_viewer = WareListViewer.WareList()
        self.warehouse_view = WarehouseViewer.WarehouseViewer()

        # Add the viewers to the layout
        layout.addWidget(self.ware_list_viewer)
        layout.addWidget(self.warehouse_view, 1)  # Give the warehouse viewer more space
