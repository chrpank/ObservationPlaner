from DataParser import DataParser
from DataParser import DataVector


class SiteSettings:

    def __init__(self):
        self.min_value_for_azimuth = 130.0  # degrees
        self.max_value_for_azimuth = 160.0  # degress
        self.min_value_for_altitude = 30.0  # degrees
        self.max_value_for_altitude = 90.0  # degress


class Object():

    def __init__(self):
        self.object_name = ""
        self.data_files = ["",
                           "",
                           ""]
        self.sun = Sun()
        self.allowed_sun_high = +90.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []

    def calculateObservations(self):
        for i in range(len(self.data_files)):
            object_data = DataParser().parseDataFile(self.data_files[i])
            sun_data = DataParser().parseDataFile(self.sun.data_files[i])

            for j in range(len(object_data)):

                # angular conditions
                # ******************
                objval = DataVector()
                objval = object_data[j]

                condition_obj_azimuth_1 = bool(
                    float(objval.horiz_azimuth) >=
                    SiteSettings().min_value_for_azimuth)
                condition_obj_azimuth_2 = bool(
                    float(objval.horiz_azimuth) <=
                    SiteSettings().max_value_for_azimuth)

                condition_obj_altitude = bool(
                    float(objval.horiz_altitude) >=
                    SiteSettings().min_value_for_altitude)
                condition_obj_altitude_2 = bool(
                    float(objval.horiz_altitude) <=
                    SiteSettings().max_value_for_altitude)

                # sun conditions
                # **************
                sunval = DataVector()
                sunval = sun_data[j]

                condition_sun_altitude_1 = bool(
                    float(sunval.horiz_altitude) <=
                    self.allowed_sun_high)

                # all conditions fullfilled
                # *************************
                can_be_observed = bool(
                    condition_obj_azimuth_1 and
                    condition_obj_azimuth_2 and
                    condition_obj_altitude and
                    condition_obj_altitude_2 and
                    condition_sun_altitude_1)

                # print(can_be_observed)
                if can_be_observed:
                    self.observation_data.append(objval)
                    print(objval.horiz_azimuth)
                    print(objval.horiz_altitude)
                    print(objval.date_day)


class Sun():

    def __init__(self):
        self.object_name = "Sun"
        self.data_files = ["data/Sun2019.txt",
                           "data/Sun2020.txt",
                           "data/Sun2021.txt"]
        self.allowed_sun_high = +90.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Moon(Object):

    def __init__(self):
        self.object_name = "Moon"
        self.data_files = ["data/Moon2019.txt",
                           "data/Moon2020.txt",
                           "data/Moon2021.txt"]
        self.sun = Sun()
        self.allowed_sun_high = +20.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Mercury(Object):

    def __init__(self):
        self.object_name = "Mercury"
        self.data_files = ["data/Mercury2019.txt",
                           "data/Mercury2020.txt",
                           "data/Mercury2021.txt"]
        self.sun = Sun()
        self.allowed_sun_high = +90.0  # degrees
        self.allowed_sun_distance = +50.0  # degrees
        self.observation_data = []


class Venus(Object):

    def __init__(self):
        self.object_name = "Venus"
        self.data_files = ["data/Venus2019.txt",
                           "data/Venus2020.txt",
                           "data/Venus2021.txt"]
        self.sun = Sun()
        self.allowed_sun_high = +90.0  # degrees
        self.allowed_sun_distance = +40.0  # degrees
        self.observation_data = []


class Mars(Object):

    def __init__(self):
        self.object_name = "Mars"
        self.data_files = ["data/Mars2019.txt",
                           "data/Mars2020.txt",
                           "data/Mars2021.txt"]
        self.sun = Sun()
        self.allowed_sun_high = +00.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Jupiter(Object):

    def __init__(self):
        self.object_name = "Jupiter"
        self.data_files = ["data/Jupiter2019.txt",
                           "data/Jupiter2020.txt",
                           "data/Jupiter2021.txt"]
        self.sun = Sun()
        self.allowed_sun_high = +10.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Saturn(Object):

    def __init__(self):
        self.object_name = "Saturn"
        self.data_files = ["data/Saturn2019.txt",
                           "data/Saturn2020.txt",
                           "data/Saturn2021.txt"]
        self.sun = Sun()
        self.allowed_sun_high = +00.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Uranus(Object):

    def __init__(self):
        self.object_name = "Uranus"
        self.data_files = ["data/Uranus2019.txt",
                           "data/Uranus2020.txt",
                           "data/Uranus2021.txt"]
        self.sun = Sun()
        self.allowed_sun_high = -20.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Neptune(Object):

    def __init__(self):
        self.object_name = "Neptune"
        self.data_files = ["data/Neptune2019.txt",
                           "data/Neptune2020.txt",
                           "data/Neptune2021.txt"]
        self.sun = Sun()
        self.allowed_sun_high = -30.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Pluto(Object):

    def __init__(self):
        self.object_name = "Pluto"
        self.data_files = ["data/Pluto2019.txt",
                           "data/Pluto2020.txt",
                           "data/Pluto2021.txt"]
        self.sun = Sun()
        self.allowed_sun_high = -30.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []
