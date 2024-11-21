class Vehicle:
    def __init__(self, model_year: int, total_mileage: int, VIN: str, EPAclass, EPAmileage, engine, transmission, options, fuel, kms_per_liter):
        self.__model_year = model_year
        self.__total_mileage = total_mileage
        self.__VIN = VIN
        self.__EPAclass = EPAclass
        self.__EPAmileage = EPAmileage
        self.__engine = engine
        self.__transmission = transmission
        self.__options = options
        self.__fuel = fuel
        self.__kms_per_liter = kms_per_liter

    def __str__(self):
        result = "Model year {} \n".format(self.model_year)
        result += "Total Mileage {} \n".format(self.total_mileage)
        # add all the other atrributes to the string
        return result

    def drive_kms(self, kms):
        try:
            kms = float(kms)
        except ValueError:
            print ("Kms not well formatted")
            return

        self.__fuel -= kms / self.__kms_per_liter
        print ("Vehicle has now {} litres of gasoline".format(self.__fuel))

class Truck(Vehicle):

    def __init__(self, model_year, total_mileage, VIN, EPAclass, EPAmileage, engine, transmission, options, fuel, maximum_seating, cabin_size):
        Vehicle.__init__(model_year, total_mileage, VIN, EPAclass, EPAmileage, engine, transmission, options, fuel)
        self.__maximum_seating = maximum_seating
        self.__cabin_size = cabin_size # kgs
        self.__current_load = 0

    def __str__(self):
        result_str = Vehicle.__str__(self)
        result_str += " {} maximum seating and {} cabin size".format(self.__maximum_seating, self.__cabin_size)

    def add_package(self, kgs):

        try:
            kms = float(kgs)
        except ValueError:
            print ("Kgs not well formatted")
            return

        if self.__current_load + kgs <= self.__cabin_size:
            self.__current_load += kgs
        else:
            print("Cabin size can not handle this package")
            return
