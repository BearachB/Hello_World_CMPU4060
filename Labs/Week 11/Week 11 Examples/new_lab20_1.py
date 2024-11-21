class Vehicle(object):

    def __init__(self,
                 total_mileage: int,
                 VIN: str,
                 engine: str,
                 options=None,
                 tax_in_date=False,
                 transmission="manual",
                 model_year=0):
        self.total_mileage = total_mileage
        self.__VIN = VIN
        self.engine = engine
        if options is not None:
            self.options = options
        self.transmission = transmission
        self.model_year = model_year
        self.tax_in_date = tax_in_date

    def update_mileage(self, new_mileage):
        self.total_mileage = new_mileage

    def get_vin(self):
        return self.__VIN

    def set_vin(self, new_vin):
        self.__VIN = new_vin

    def __str__(self):
        result_str = "-" * 25 + "\n"
        result_str += "Vehicle Information\n"
        result_str += "Model year: " + str(self.model_year) + "\n"
        result_str += "Total mileage: " + str(self.total_mileage) + "\n"
        result_str += "VIN: " + self.get_vin() + "\n"
        result_str += "Engine: " + self.engine + "\n"
        if self.options is not None:
            result_str += "Options: "
            for option in self.options:
                result_str += option + ", "
            # result_str = result_str[:-2] + "\n"
            result_str = result_str.strip(", ") + "\n"

        if self.tax_in_date:
            result_str += "Tax in date \n"
        else:
            result_str += "Tax not in date \n"

        result_str += "Transmission: " + self.transmission + "\n"
        result_str += "-" * 25 + "\n"
        return result_str

class Truck(Vehicle):

    def __init__(self,
                 total_mileage: int,
                 VIN: str,
                 engine: str,
                 cargo_capacity:int,
                 trailer_length:float,
                 options=None,
                 tax_in_date=False,
                 transmission="manual",
                 model_year=0):

        Vehicle.__init__(self, total_mileage, VIN, engine, options, tax_in_date, transmission, model_year)
        self.cargo_capacity = cargo_capacity
        self.trailer_length = trailer_length

    def __str__(self):
        # Gets the string representation from Vehicle
        # Breaks it into a list, so we can add new string before the last line
        return_str = Vehicle.__str__(self).split("\n")[:-1]
        last_line = return_str[-1][:]
        return_str[-1] = "Cargo capacity: " + str(self.cargo_capacity)
        return_str.append("Trailer length: " + str(self.trailer_length))
        return_str.append(last_line)
        return_str = "\n".join(return_str)
        return return_str

# Main code
vehicle1 = Vehicle(60000,
                   "1HGBH41JXMN109186",
                   "diesel",
                   ["eletric windows", "air con", "sat nav", "alloy wheels"],
                   model_year=2012)

truck1 = Truck(60000,
               "1HGBH41JXMN109186",
               "diesel",
               4000,
               12.5,
               ["eletric windows", "air con", "sat nav", "alloy wheels"],
               model_year=2012)

#print(vehicle1)
print(truck1)
truck1.update_mileage(70000)
print(truck1)
