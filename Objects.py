from DataParser import DataParser
from DataParser import DataVector


class SiteSettings:

    def __init__(self):
        self.min_value_for_azimuth = 130.0  # degrees
        self.max_value_for_azimuth = 160.0  # degress
        self.min_value_for_altitude = 30.0  # degrees
        self.max_value_for_altitude = 90.0  # degress


class Object:

    def __init__(self):
        self.object_name = ""
        self.data_files = []
        self.allowed_sun_high = +0.0  # degrees
        self.allowed_sun_distance = +0.0  # degrees
        self.observation_data = []

    def calculateObservations(self):
        for filepath in self.data_files:
            data_object = DataParser().parseDataFile(filepath)
            data_entry = DataVector()

            # for data_entry in data_object:

            # azimut_is_in_range =
            # float(data_entry.horizontal_azimuth) >
            # SiteSettings().min_value_for_azimuth and
            # float(data_entry.horizontal_azimuth) <
            # SiteSettings().max_value_for_azimuth

            # suns_position_is_suitable = \
            # self.allowed_sun_high > SiteSettings().min_value_for_azimuth and
            # float(data_entry.horizontal_azimuth) <
            # SiteSettings().max_value_for_azimuth

            # if  :
            #    self.observation_data.append(data_entry)


class Moon(Object):

    def __init__(self):
        self.object_name = "Moon"
        self.data_files = ["Moon2019.txt",
                           "Moon2020.txt",
                           "Moon2021.txt"]
        self.allowed_sun_high = +20.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Mercury(Object):

    def __init__(self):
        self.object_name = "Mercury"
        self.data_files = ["Mercury2019.txt",
                           "Mercury2020.txt",
                           "Mercury2021.txt"]
        self.allowed_sun_high = +90.0  # degrees
        self.allowed_sun_distance = +50.0  # degrees
        self.observation_data = []


class Venus(Object):

    def __init__(self):
        self.object_name = "Venus"
        self.data_files = ["Venus2019.txt",
                           "Venus2020.txt",
                           "Venus2021.txt"]
        self.allowed_sun_high = +90.0  # degrees
        self.allowed_sun_distance = +40.0  # degrees
        self.observation_data = []


class Mars(Object):

    def __init__(self):
        self.object_name = "Mars"
        self.data_files = ["Mars2019.txt",
                           "Mars2020.txt",
                           "Mars2021.txt"]
        self.allowed_sun_high = +00.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Jupiter(Object):

    def __init__(self):
        self.object_name = "Jupiter"
        self.data_files = ["Jupiter2019.txt",
                           "Jupiter2020.txt",
                           "Jupiter2021.txt"]
        self.allowed_sun_high = +10.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Saturn(Object):

    def __init__(self):
        self.object_name = "Saturn"
        self.data_files = ["Saturn2019.txt",
                           "Saturn2020.txt",
                           "Saturn2021.txt"]
        self.allowed_sun_high = +00.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Uranus(Object):

    def __init__(self):
        self.object_name = "Uranus"
        self.data_files = ["Uranus2019.txt",
                           "Uranus2020.txt",
                           "Uranus2021.txt"]
        self.allowed_sun_high = -20.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Neptune(Object):

    def __init__(self):
        self.object_name = "Neptune"
        self.data_files = ["Neptune2019.txt",
                           "Neptune2020.txt",
                           "Neptune2021.txt"]
        self.allowed_sun_high = -30.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []


class Pluto(Object):

    def __init__(self):
        self.object_name = "Pluto"
        self.data_files = ["Pluto2019.txt",
                           "Pluto2020.txt",
                           "Pluto2021.txt"]
        self.allowed_sun_high = -30.0  # degrees
        self.allowed_sun_distance = +180.0  # degrees
        self.observation_data = []
