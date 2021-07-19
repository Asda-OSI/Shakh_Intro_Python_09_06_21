import random


def create_point(min_limit, max_limit):
    point = {
        'x': random.randint(min_limit, max_limit),
        'y': random.randint(min_limit, max_limit)
    }
    return point


def create_triangle(points_name_str, min_limit, max_limit):
    return {key: create_point(min_limit, max_limit) for key in points_name_str}


triangle_ABC = create_triangle('ABC', -10, 10)
triangle_MNK = create_triangle('MNK', -100, 100)
triangle_QWE = create_triangle('QWE', -15, 15)

print(triangle_ABC)
print(triangle_MNK)
print(triangle_QWE)