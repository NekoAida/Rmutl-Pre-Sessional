import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("First pytQ5 App")
window.setGeometry(100, 100, 500, 200)

lable = QLabel("Neko Aida", window)
lable.setStyleSheet("font-size: 20px; color: black;")
lable.move(50, 80)

window.show()

sys.exit(app.exec_())
