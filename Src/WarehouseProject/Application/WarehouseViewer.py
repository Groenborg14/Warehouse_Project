from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPen



class WarehouseViewer(QGraphicsView):
    def __init__(self):

        super().__init__()


        # Set up the scene
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        # Set the background color of the scene
        #self.scene.setBackgroundBrush(QBrush(QColor(240, 240, 240)))

        self.draw_warehouse()
        

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

                self.scene.addRect(
                    x,
                    y,
                    shelf_width,
                    shelf_height, QPen(Qt.black), QBrush(QColor(200, 200, 200))
                )

                text = self.scene.addText(
                    f"{row_name}{position + 1:02}"
                )

                text.setPos(x + 3, y + 3)

        