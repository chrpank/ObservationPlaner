

class DataVector:

    def __init__(self):
        self.date_year = ""
        self.date_month = ""
        self.date_day = ""
        self.date_hour = ""
        self.date_minute = ""
        self.date_second = ""

        self.equa_hour_angle_hour = ""
        self.equa_hour_angle_minute = ""
        self.equa_dec_degrees = ""
        self.equa_dec_arcmin = ""

        self.horiz_azimuth = ""
        self.horiz_altitude = ""


class LinePositions:

    def __init__(self):
        self.date_year_start = 17
        self.date_year_end = 20
        self.date_month_start = 14
        self.date_month_end = 15
        self.date_day_start = 11
        self.date_day_end = 12
        self.date_hour_start = 1
        self.date_hour_end = 2
        self.date_minute_start = 4
        self.date_minute_end = 5
        self.date_second_start = 7
        self.date_second_end = 8

        self.equa_hour_angle_hour_start = 54
        self.equa_hour_angle_hour_end = 55
        self.equa_hour_angle_minute_start = 57
        self.equa_hour_angle_minute_end = 60
        self.equa_dec_degrees_start = 62
        self.equa_dec_degress_end = 64
        self.equa_dec_arcmin_start = 66
        self.equa_dec_arcmin_end = 67

        self.horiz_azimuth_start = 79
        self.horiz_azimuth_end = 85
        self.horiz_altitude_start = 87
        self.horiz_altitude_end = 93


class DataParser:

    def __init__(self):
        self.version = "1"

    def parseDataFile(self, filename="data/Moon2019.txt"):

        temp_data = DataVector()
        parsed_data = []

        datafile = open(filename)
        lines = datafile.readlines()
        data = lines[8:]

        for line in data:
            temp_data.date_year = \
                line[LinePositions().date_year_start - 1:
                     LinePositions().date_year_end]

            temp_data.date_month = \
                line[LinePositions().date_month_start - 1:
                     LinePositions().date_month_end]

            temp_data.date_day = \
                line[LinePositions().date_day_start - 1:
                     LinePositions().date_day_end]

            temp_data.date_hour = \
                line[LinePositions().date_hour_start - 1:
                     LinePositions().date_hour_end]

            temp_data.date_minute = \
                line[LinePositions().date_minute_start - 1:
                     LinePositions().date_minute_end]

            temp_data.date_second = \
                line[LinePositions().date_second_start - 1:
                     LinePositions().date_second_end]

            temp_data.equa_dec_degrees = \
                line[LinePositions().equa_dec_degrees_start - 1:
                     LinePositions().equa_dec_degress_end]

            temp_data.equa_dec_arcmin = \
                line[LinePositions().equa_dec_arcmin_start - 1:
                     LinePositions().equa_dec_arcmin_end]

            temp_data.equa_hour_angle_hour = \
                line[LinePositions().equa_hour_angle_hour_start - 1:
                     LinePositions().equa_hour_angle_hour_end]

            temp_data.equa_hour_angle_minute = \
                line[LinePositions().equa_hour_angle_minute_start - 1:
                     LinePositions().equa_hour_angle_minute_end]

            temp_data.horiz_azimuth = \
                line[LinePositions().horiz_azimuth_start - 1:
                     LinePositions().horiz_azimuth_end]

            temp_data.horiz_altitude = \
                line[LinePositions().horiz_altitude_start - 1:
                     LinePositions().horiz_altitude_end]

            parsed_data.append(temp_data)

        datafile.close()

        return parsed_data
