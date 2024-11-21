class Vehicle(object):
    def __init__(self, model_year=2010, mileage=60000, VIN="HB1678W673DDG", transmission="manual", engine_size=1400, engine_type="diesel", colour="black", options=""):
        self.model_year = model_year
        self.mileage = mileage
        self.__VIN = VIN
        self.transmission = transmission
        self.engine_size = engine_size
        self.engine_type = engine_type
        self.options = options
        self.colour = colour
        if options is not None:
            self.options = options

    def get_vin(self):
        return self.__VIN

    def set_vin(self):
        return self.__VIN = new_VIN

    def __str__(self):
        result_str = "-" * 25 + "\n"
        result_str += "Model Year: " + str(self.model_year) + "\n"
        result_str += "Mileage: " + str(self.mileage) + "\n"
        result_str += "VIN: " + self.VIN + "\n"
        result_str += "Transmission: " + self.transmission + "\n"
        result_str += "Engine Size: " + str(self.engine_size) + "\n"
        result_str += "Engine Type: " + self.engine_type + "\n"
        result_str += "Colour: " + self.colour + "\n"
        if self.options is not None:
            result_str += "Options: "
            for option in self.options:
                result_str += option + ","

        result_str = "-" * 25 + "\n"

        return result_str

class Car(Vehicle):
    pass

class Truck(Vehicle):
    def __init__(self, model_year=2010, mileage=60000, VIN="HB1678W673DDG", transmission="manual", engine_size=1400, engine_type="diesel", colour="black", options=""):
        Vehicle.__init__(self,total_mileage, VIN, engine_size, engine_type, )

class SUV(Vehicle):
    pass


vehicle1 = Vehicle(2016, 24999, "HB49857GFDGSR242D", "manual", 2000, "petrol", "red", "")
print(str(vehicle1))
