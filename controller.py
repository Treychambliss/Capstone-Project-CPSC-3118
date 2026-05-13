from PySide6.QtWidgets import QMainWindow
from view import uiRoot
from model import TemperatureModel

class Controller(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Set up the view
        self.ui = uiRoot()
        self.ui.setupUi(self)
        
        #Set up the model
        self.model = TemperatureModel()
        
        #Connect buttons to functions
        self.ui.btnConvert.clicked.connect(self.processConversion)
        self.ui.btnReset.clicked.connect(self.resetApp)
        self.ui.btnExit.clicked.connect(self.close)  # Built-in PySide6 function to close the window

    def processConversion(self):
        """Grabs Text and sends to model."""
        userInput = self.ui.entFahrenheit.text()
        
        #Perform the calculations
        result = self.model.convert_f_to_c(userInput)
        
        #Display result
        self.ui.lblResult.setText(result)

    def resetApp(self):
        """Clears the fields."""
        self.ui.entFahrenheit.clear()
        self.ui.lblResult.setText("---")