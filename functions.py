import const
import random as rd


def popall(name):
    const.name_map.pop(name)
    const.M_names.remove(name)
    const.F_names.remove(name)

#extract a subset of the dataset with an option for labelled
def extract(size, labelled=False):
    half = size/2
    result = {} if labelled else []
    for i in range(half):
        index = rd.randint(0, const.M_names if len(const.M_names) > len(const.F_names) else const.F_names)
        if labelled:
            result[const.M_names[index]] = True
            result[const.F_names[index]] = False
        else:
            result.append(const.M_names[index])
            result.append(const.F_names[index])
        popall(const.M_names[index])
        popall(const.F_names[index])
    return result