from DataParser import DataVector
from DataParser import DataParser

if __name__ == "__main__":

    data = DataParser().parseDataFile()

    print(len(data))

    data_entry = DataVector()
    data_entry = data[1]

    print(data_entry.date_year)
