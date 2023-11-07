import re
from utils import *


class Lex:
    def __init__(self, ts_identifiers, ts_constants, fip):
        self.__ts_identifiers = ts_identifiers
        self.__ts_constants = ts_constants
        self.__fip = fip

    def get_ts_identifiers(self):
        return self.__ts_identifiers.get_items()

    def get_ts_constants(self):
        return self.__ts_constants.get_items()

    def get_fip(self):
        return self.__fip

    def manage_atoms(self, symbol):
        self.__fip.add(atoms[symbol], "-1")

    def manage_identifiers(self, identifier):
        if not (0 < len(identifier) < 250):
            return False
        else:
            if identifier not in self.get_ts_identifiers():
                value = {
                    "type": type_of_atoms["identifier"],
                    "value": self.__ts_identifiers.get_length() + self.__ts_constants.get_length(),
                }
                self.__ts_identifiers.set(identifier, value)

            self.__fip.add(type_of_atoms["identifier"], self.__ts_identifiers.get_value(identifier)["value"])

        return True

    def add_constants_to_ts(self, constant_value):
        if constant_value not in self.get_ts_constants():
            value = {
                "type": type_of_atoms["constant"],
                "value": self.__ts_identifiers.get_length() + self.__ts_constants.get_length(),
            }
            self.__ts_constants.set(constant_value, value)

        self.__fip.add(type_of_atoms["constant"], self.__ts_constants.get_value(constant_value)["value"])

    def manage_constants(self, constant):
        put_string_value = re.match(r'[^"]*("([^"]*)")[^"]*', constant)
        if put_string_value:
            string_value = put_string_value.group(1)
            self.add_constants_to_ts(string_value)
            return True

        put_numeric_value = re.match(r'^-?[0-9]+(\.[0-9]+)?$', constant)
        if put_numeric_value:
            numeric_value = put_numeric_value.group(0)
            self.add_constants_to_ts(numeric_value)
            return True

        print("Error: Invalid constant format: " + constant)
        return False
