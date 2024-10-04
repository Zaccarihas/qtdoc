import sys

from PyQt5.QtWidgets import (
    QApplication
)

from basicmainclass import (
    MyWindow
)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())
