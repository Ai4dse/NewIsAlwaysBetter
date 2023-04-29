import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import Qt
import main


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PDF Selector")
        self.setFixedSize(400, 200)

        # Create label for selected file path
        self.label = QLabel("No file selected", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50, 30, 300, 50)

        # Create button to select PDF file
        self.select_button = QPushButton("Select PDF File", self)
        self.select_button.setGeometry(50, 90, 150, 50)
        self.select_button.clicked.connect(self.selectPDF)

        # Create button to start program on selected file
        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(50, 150, 150, 50)
        self.start_button.clicked.connect(self.startProgram)
        self.start_button.setEnabled(False)

        # Create button to stop program on selected file
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(200, 150, 150, 50)
        self.stop_button.clicked.connect(self.stopProgram)
        self.stop_button.setEnabled(False)

        self.show()

    def selectPDF(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","PDF Files (*.pdf)", options=options)
        if fileName:
            self.label.setText(f"Selected file: {fileName}")
            self.selected_file = fileName
            self.start_button.setEnabled(True)

    def startProgram(self):
        global filePath
        filePath = self.selected_file
        # Add your code to process the PDF file here
        # Use self.selected_file to access the selected file path
        print("Starting transcription")
        main.recordAndTranscribe()
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stopProgram(self):
        # Add your code to stop the transcription process here
        print("Stopping transcription")
        main.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def getFilePath(self):
        return filePath


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
