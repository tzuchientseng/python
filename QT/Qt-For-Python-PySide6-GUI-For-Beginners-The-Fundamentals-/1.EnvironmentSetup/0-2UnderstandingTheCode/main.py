# Importing the components of PySide6
from PySide6.QtWidgets import QApplication, QWidget

# The sys module is responsible for processing command line arguments
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

# Start the event loop
# app.exec_() // Old version, not recommended
app.exec()
