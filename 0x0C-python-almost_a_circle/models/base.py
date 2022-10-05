#!/usr/bin/python3
"""Defines a base class for other tasks."""
import json
import csv


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string."""
        if json_string is None:
            return '[]'
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            Writes the string representation of an object of a class
            into a file
        '''
        file_name = cls.__name__ + ".json"

        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)

        with open(file_name, mode="w") as fd:
            json.dump(content, fd)

    def create(cls, **dictionary):
        """ returns an instance with all attributes already set."""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r2 = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            r2 = Square(5)
        r2.update(**dictionary)
        return (r2)

    @classmethod
    def load_from_file(cls):
        '''
            loading dict representing the parameters for
            and instance and from that creating instances
        '''
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF8") as fd:
                content = cls.from_json_string(fd.read())
        except Exception:
            return []

        instances = []

        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)

    @staticmethod
    def draw(list_rectangle, list_square):
        """ Open a new window and draw all the Rectangles and Squares."""
        import turtle

        turtle.penup()
        turtle.bgcolor("grey")
        turtle.color("yellow")
        turtle.goto(-300, 300)
        turtle.speed(2)

        for instance in list_rectangle:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 200
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 300)

        turtle.goto(-300, 100)
        for instance in list_squares:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 100
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 100)

        turtle.exitonclick()
