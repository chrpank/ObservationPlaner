"""
Tool for displaying observing times of solar system objects.
Christian Pankratz, 2022
"""

import argparse

ENABLE_DEBUG_MODE = False

# parse commandline arguments
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("sit_para_path",
                        help="The site parameter filepath.")
arg_parser.add_argument("obj_para_path",
                        help="The object parameter filepath.")
arg_parser.add_argument("obj_data_path",
                        help="The object data filepath.")
arg_parser.add_argument("sun_data_path",
                        help="The sun data filepath.")

print("observation event calculation")
print("sit_para_path = " + arg_parser.parse_args().sit_para_path)
print("obj_para_path = " + arg_parser.parse_args().obj_para_path)
print("obj_data_path = " + arg_parser.parse_args().obj_data_path)
print("sun_data_path = " + arg_parser.parse_args().sun_data_path)

# parse site settings
site_para_file = open(arg_parser.parse_args().sit_para_path)
site_min_azim = site_para_file.readline()[0:8]
site_max_azim = site_para_file.readline()[0:8]
site_para_file.close()

print("observation view data")
print("site_min_azim = " + site_min_azim)
print("site_max_azim = " + site_max_azim)

# parse parameter file
obj_para_file = open(arg_parser.parse_args().obj_para_path)
obj_min_alti = obj_para_file.readline()[0:8]
sun_min_dist = obj_para_file.readline()[0:8]
sun_max_alti = obj_para_file.readline()[0:8]
obj_para_file.close()

print("object condition data")
print("obj_min_alti = " + obj_min_alti)
print("sun_min_dist = " + sun_min_dist)
print("sun_max_alti = " + sun_max_alti)

# calculate obs events
obj_data_file = open(arg_parser.parse_args().obj_data_path)
obj_data_lins = obj_data_file.readlines()[8:]

sun_data_file = open(arg_parser.parse_args().sun_data_path)
sun_data_lins = sun_data_file.readlines()[8:]

print("table of observation events")

EVENT_NOT_FOUND = True

for index in range(len(obj_data_lins)):

    obj_line = obj_data_lins[index]
    sun_line = sun_data_lins[index]

    obj_azim = obj_line[78:78 + 7]
    obj_alti = obj_line[86:86 + 7]
    sun_azim = sun_line[78:78 + 7]
    sun_alti = sun_line[86:86 + 7]

    if ENABLE_DEBUG_MODE:
        print("obj_azim = " + obj_azim)
        print("obj_alti = " + obj_alti)
        print("sun_azim = " + sun_azim)
        print("sun_alti = " + sun_alti)

    # check conditions
    cond_obj_azim = bool(float(obj_azim) >= float(site_min_azim) and
                         float(obj_azim) <= float(site_max_azim))
    cond_obj_alti = bool(float(obj_alti) >= float(obj_min_alti))
    cond_sun_alti = bool(float(sun_alti) <= float(sun_max_alti))
    cond_sun_dist = bool(abs(float(obj_azim) - float(sun_azim))
                         >= float(sun_min_dist))

    if (cond_obj_azim and
        cond_obj_alti and
        cond_sun_alti and
            cond_sun_dist):
        print(obj_line.rstrip())
        EVENT_NOT_FOUND = False

if EVENT_NOT_FOUND is True:
    print("No events found.")

print("end of output")
