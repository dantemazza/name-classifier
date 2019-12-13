import csv

import configuration as config


def get_data():
    M_names = []
    F_names = []
    name_M_map = {}
    name_F_map = {}
    name_map = {}
    with open("NationalNames.csv") as file:
        reader = csv.reader(file, delimiter= ',')
        for row in reader:
            if row[2] == "Year":
                continue
            name = row[1].lower()
            gender = row[3]


            if int(row[2]) >= config.starting_year:
                if gender == "M":
                    name_M_map[name] = name_M_map[name] + 1 if name in name_M_map else 1
                else:
                    name_F_map[name] = name_F_map[name] + 1 if name in name_F_map else 1

    def x(dict1, dict2):
        for key in dict1:
            if key in dict2:
                if dict1[key] >= dict2[key]:
                    dict2.pop(key)

    x(name_M_map, name_F_map)
    x(name_F_map, name_M_map)

    for key in name_M_map:
        M_names.append(key)
        name_map[key] = 1
    for key in name_F_map:
        F_names.append(key)
        name_map[key] = 0

    return M_names, F_names, name_map




