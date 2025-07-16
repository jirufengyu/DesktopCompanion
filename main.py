import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt

class DesktopPet(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the window
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Add a label to display the pet animation
        self.pet_label = QLabel(self)
        # Placeholder for pet animation (e.g., a GIF)
        # self.movie = QMovie("path_to_your_pet.gif")
        # self.pet_label.setMovie(self.movie)
        # self.movie.start()
        
        # Placeholder text until assets are ready
        self.pet_label.setText("PET")
        self.pet_label.setStyleSheet("font-size: 20px; font-weight: bold; color: white; background-color: rgba(0,0,0,150); padding: 10px; border-radius: 5px;")
        self.pet_label.adjustSize()

        self.resize(self.pet_label.size())
        self.show()

    # Allow dragging the window
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_drag:
            self.move(event.globalPos() - self.m_DragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_drag = False


def main():
    """Main function to run the application."""
    app = QApplication(sys.argv)
    pet = DesktopPet()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
