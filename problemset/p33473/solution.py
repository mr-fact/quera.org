import math


def square_creator():
    def square(a):
        return a * a
    return square


def circle_creator():
    def circle(r):
        return math.pi * r ** 2
    return circle

def rectangle_creator():
    def rectangle(a, b):
        return a * b
    return rectangle

def triangle_creator():
    def triangle(a, b):
        return a * b / 2
    return triangle


def get_func(ls):
    result_list = []
    for func_name in ls:
        if func_name == 'square':
            result_list.append(square_creator())
        elif func_name == 'circle':
            result_list.append(circle_creator())
        elif func_name == 'rectangle':
            result_list.append(rectangle_creator())
        elif func_name == 'triangle':
            result_list.append(triangle_creator())
    return result_list
