class TemperatureModel:
    def __init__(self):
        self.last_result = ""

    def convert_f_to_c(self, temp_string):
        """Converts Fahrenheit to Celsius."""
        try:
            #Convert to a float
            f_temp = float(temp_string)
            
            #Calculations
            c_temp = (f_temp - 32) * 5.0 / 9.0
            
            #Round to 2 decimal places
            self.last_result = f"{c_temp:.2f} °C"
            return self.last_result
            
        except ValueError:
            #Error handling
            self.last_result = "Error: Invalid Input"
            return self.last_result