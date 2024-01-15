#!/usr/bin/python3
'''initializes a class'''

import json


class Base:
    '''defines a class base'''
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns JSON string rep of list_dictionaries'''
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON str rep to a file'''
        filename = cls.__name__ + ".json"

        if list_objs is None:
            with open(filename, 'w') as file:
                file.write("[]")
        else:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
            with open(filename, 'w') as file:
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''returns list of the JSON string representation'''
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if cls.__name__ == 'Rectangle':
            new_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_instance = cls(1)
        else:
            raise ValueError

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                if not json_string:
                    return []
                else:
                    json_info = cls.from_json_string(json_string)

                    instances = [cls.create(**info) for info in json_info]
                    return instances

        except FileNotFoundError:
            return []
