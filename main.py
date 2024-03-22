import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QTimer, pyqtSlot
import random
from dronekit import *
import resources
import math

connection_string = "tcp:127.0.0.1:5762"
vehicle = connect(connection_string, baud=57600, wait_ready=True,rate=50)


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MAP")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.browser = QWebEngineView()
        
        layout.addWidget(self.browser)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.load_map()

        # PyQt5'de QTimer kullanarak rastgele olarak konum güncelleme işlemini gerçekleştirelim
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_marker)
        self.timer.start(100)  # Her 1 saniyede bir güncelle


    def load_map(self):
        with open("map.html", 'r') as file:
            html_content = file.read()
        self.browser.setHtml(html_content)

    @pyqtSlot()
    def update_marker(self):
        # Rastgele bir konum üretelim, gerçek zamanlı güncelleneceğini varsayalım
        new_lat = vehicle.location.global_frame.lat
        new_lon = vehicle.location.global_frame.lon
        angle = math.degrees(vehicle.attitude.yaw)
        print(new_lat,new_lon,angle)
        
        # JavaScript fonksiyonunu çağırarak marker'ın konumunu güncelleyelim
        self.browser.page().runJavaScript(f"updateMarker({new_lat}, {new_lon},{angle})")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())
