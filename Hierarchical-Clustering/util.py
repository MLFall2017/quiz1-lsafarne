import math


def distance(p1, p2):
    """Compute Euclidean Distance btw two points"""

    temp = 0
    for i in range(len(p1)):
        temp += math.pow(p1[i] - p2[i], 2)
    result = math.sqrt(temp)
    return result


def min_sequence(sec):
    """
    :param sec: 
    :return: result: dict
    """

    # TODO find min in a list and tuple
    result = {}
    if len(sec) > 0:  # if it is not empty
        min_key = list(sec.keys())[0]
        min_val = sec[min_key]
        for i, val in sec.items():
            if val < min_val:
                min_val = val
                min_key = i

        result['min_val'] = min_val
        result['min_key'] = min_key
    return result


def max_sequence(sec):
    """
    :param sec:
    :return: result: dict
    """

    # TODO find min in a list and tuple
    result = {}
    if len(sec) > 1:
        max_key = list(sec.keys())[0]
        max_val = sec[max_key]
        for i, val in sec.items():
            if val > max_val:
                max_val = val
                max_key = i

        result['max_val'] = max_val
        result['max_key'] = max_key
    return result
