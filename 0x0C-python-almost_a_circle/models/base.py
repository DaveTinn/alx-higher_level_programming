#!/usr/bin/python3
"""
Python Interpreter

The class module
"""
from json import dumps, loads
import json
import csv
"""The CSV module."""


class Base:
    """Instantiating the class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of a string to a file"""
        file_list = []
        if list_objs is not None:
            for obj in list_objs:
                file_list.append(obj.to_dictionary())
        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(file_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new_instance = Rectangle(1, 1)
        elif cls is Square:
            new_instance = Square(1)
        else:
            new_instance = None

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """loads from a file and returns a list of instances"""
        from os import path
        filename = '{}.json'.format(cls.__name__)
        if not path.isfile(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            cls_str = f.read()
            list_instance = Base.from_json_string(cls_str)
            return [cls.create(**d) for d in list_instance]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects."""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            elif cls is Square:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects"""
        from models.rectangle import Rectangle
        from models.square import Square
        my_obj = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(idx) for idx in row]
                if cls is Rectangle:
                    d = {'id': row[0], 'width': row[1], 'height': row[2],
                         'x': row[3], 'y': row[4]}
                else:
                    d = {'id': row[0], 'size': row[1],
                         'x': row[2], 'y': row[3]}
                my_obj.append(cls.create(**d))
        return my_obj

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for idx in list_rectangles + list_squares:
            my_turtle = turtle.Turtle()
            my_turtle.color((randrange(255), randrange(255), randrange(255)))
            my_turtle.pensize(1)
            my_turtle.penup()
            my_turtle.pendown()
            my_turtle.setpos((idx.x + my_turtle.pos()[0], idx.y - my_turtle.pos()[1]))
            my_turtle.pensize(10)
            my_turtle.forward(idx.width)
            my_turtle.left(90)
            my_turtle.forward(idx.height)
            my_turtle.left(90)
            my_turtle.forward(idx.width)
            my_turtle.left(90)
            my_turtle.forward(idx.height)
            my_turtle.left(90)
            my_turtle.end_file()

        time.sleep(5)
