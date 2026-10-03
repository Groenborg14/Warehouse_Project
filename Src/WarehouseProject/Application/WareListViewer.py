from PySide6.QtWidgets import QListWidget, QPushButton, QVBoxLayout, QWidget
import pandas as pd



def get_data():
    ware_data = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/test_wares.csv")
    return ware_data

class WareList(QWidget):

    def __init__(self):
        super().__init__()


        #Set a width for the ware list
        self.setFixedWidth(300)
        self.setFixedHeight(800)
        self.setWindowTitle("Warehouse List Viewer")

        # create a vertical layout to hold the list widget and button
        layout = QVBoxLayout()
        button = QPushButton("Update List")
        listwidget = QListWidget(sortingEnabled=True)
        
        #Initialize the list with a message
        listwidget.addItem("Click the button to update the list with warehouse data.")  

        # add the list widget and button to the layout
        for widget in [listwidget, button]:
            layout.addWidget(widget)    

        # define a function to update the list widget with data from the CSV file
        def update_list(self):
            data = get_data()

            if listwidget.count() > 0:
                listwidget.clear()
        
            for index, row in data.iterrows():
                listwidget.addItem(f"Name: {row['ware_id']}, weight: {row['weight_kg']}, Sales: {row['sales_per_month']}")

        # connect the button's clicked signal to the update_list function
        button.clicked.connect(update_list)


        # set the layout for the widget
        self.setLayout(layout)
        #self.setCentralWidget(central_widget)
