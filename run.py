from DataParser import DataParser
from DataParser import DataVector
from Planer import ObservationPlaner


if __name__ == "__main__":

    data = DataParser().parseDataFile()

    print(len(data))

    data_entry = DataVector()
    data_entry = data[0]

    print(data_entry.horiz_altitude)

    planer = ObservationPlaner()
    planer.calulateObservations()
