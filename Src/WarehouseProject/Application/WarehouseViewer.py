from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPen
import pandas as pd



class WarehouseViewer(QGraphicsView):
    def __init__(self):

        super().__init__()

        # Create dictionary to hold the warehouse locations
        self.locations = {}



        # Set up the scene
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        # Set the background color of the scene
        #self.scene.setBackgroundBrush(QBrush(QColor(240, 240, 240)))

        self.draw_warehouse()
        self.load_assignments()
        

    def draw_warehouse(self):

        rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        shelf_width = 60
        shelf_height = 50

        positions_per_row = 18
        

        horizontal_spacing = 5
        vertical_spacing = 30

        for row_index, row_name in enumerate(rows):

            y = row_index * (
                shelf_height + vertical_spacing
            )

            for position in range(positions_per_row):

                x = position * (
                    shelf_width + horizontal_spacing
                )

                # Create a unique location ID for each shelf
                location_id = f"{row_name}{position}"


                location = WarehouseLocation(
                    location_id,
                    x,
                    y,
                    shelf_width,
                    shelf_height
                )

                self.locations[location_id] = location
                self.scene.addItem(location)

                text = self.scene.addText(
                    f"{row_name}{position}"
                )

                text.setPos(x + 1, y + 1)

    def load_assignments(self):

        data = pd.read_csv(
            "Warehouse_Project/Tests/TestData/GenData/assignments.csv"
        )

        for _, row in data.iterrows():

            ware_id = row["ware_id"]
            location_id = row["location"]
            cost = row["cost"]

            if location_id in self.locations:

                location = self.locations[location_id]
                x = location.rect().x()
                y = location.rect().y()

                location.set_ware(
                    ware_id,
                    cost
                )
                text = self.scene.addText(
                    f"{ware_id}")
                text.setPos(x + 1, y + 20)

   

class WarehouseLocation(QGraphicsRectItem):

    def __init__(
        self,
        location_id,
        x,
        y,
        width,
        height
    ):
        # Create the actual rectangle
        super().__init__(x, y, width, height)

        # Store information about this location
        self.location_id = location_id
        self.ware_id = None
        self.cost = None

        # Appearance
        self.setPen(QPen(Qt.black))
        self.setBrush(QBrush(QColor(200, 200, 200)))

        # Makes the rectangle selectable
        self.setFlag(
            QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable,
            True
        )

        # Show location when hovering over it
        self.update_tooltip()
        


    def mousePressEvent(self, event):
        print(f"Location {self.location_id} clicked.")

        super().mousePressEvent(event)


    def set_ware(self, ware_id, cost):

        self.ware_id = ware_id
        self.cost = cost

        self.setBrush(
            QBrush(QColor(100, 200, 100))
        )

        self.update_tooltip()


    def update_tooltip(self):

        if self.ware_id is None:
            self.setToolTip(
                f"Location: {self.location_id}\n"
                f"Empty"
            )

        else:
            self.setToolTip(
                f"Location: {self.location_id}\n"
                f"Ware ID: {self.ware_id}\n"
                f"Cost: {self.cost:.3f}"
            )


