def linear_regression(points, lines):
    int_list = []
    for i in lines:
        int_list.append(get_linedistance(points, i))
    return get_min(int_list)

def get_linedistance(points, line):
    distance = 0
    for i in points:
        distance += pow((line[0] * i[0] + line[1] - i[1]), 2)
    return distance

def get_min(int_list):
    if not int_list:
        return None
    else:
        return min(int_list)