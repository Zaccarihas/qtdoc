from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel
    )

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create the objects that should be presented in the layout
        self.label1 = QLabel("First label")
        self.label2 = QLabel("Second label")

        # Create a widget that can be placed as the central widget of the window
        cw = QWidget()
        
        # Create a layout for the central widget and place the objects into the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        
        
        # Connect the layout to the central widget
        cw.setLayout(layout)
        
        # Set the central widget as the central widget of the window
        self.setCentralWidget(cw)
