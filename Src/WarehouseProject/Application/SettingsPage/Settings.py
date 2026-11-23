from PySide6.QtWidgets import QComboBox, QHBoxLayout, QLabel, QLineEdit, QWidget,QVBoxLayout
from PySide6.QtCore import Qt
import keyring


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        # Create a horizontal layout for the page
        layout = QHBoxLayout(self)
        layout.addStretch(1) 

        API_widget = QVBoxLayout()
        API_selector = QComboBox()

        API_widget.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        API_selector.addItems(["LagerSystem", "WMS 2", "WMS 3"])


        # Connect signals to slots
        API_selector.currentIndexChanged.connect(self.index_changed)
        API_selector.currentTextChanged.connect(self.text_changed)

        API_input = QLineEdit()
        API_input.setPlaceholderText("Enter API Key")
        API_input.setMaxLength(300)
        

        
        API_selector.setFixedWidth(200)
        API_widget.addWidget(API_selector)
        API_widget.addWidget(API_input)

        
        layout.addLayout(API_widget)


    def index_changed(self, index):
        print(f"Selected index: {index}")

    def text_changed(self, text):
        print(f"Selected text: {text}")
        



