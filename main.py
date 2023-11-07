import sys
import re

from data_structures.fip import FIP
from data_structures.ts import TS
from lex import Lex
from utils import *


def main():
    ts_identifiers = TS()
    ts_constants = TS()
    fip = FIP()
    lex = Lex(ts_identifiers, ts_constants, fip)

    filename = sys.argv[1]

    with open(filename, "r") as file:
        code = file.readlines()

    line_number = 0

    for line in code:
        line_number += 1
        words = line.split(" ")

        for word in words:
            word = word.strip("\n")
            while word != "":
                found = False
                put = None
                if word.startswith('"'):
                    put = re.match(r'(.*)', word)
                    if put:
                        found = lex.manage_constants(put.group(1))
                        word = word[put.end(0):]
                else:
                    for keyword in keywords:
                        result = re.match('^' + re.escape(keyword), word)
                        if result is not None:
                            found = True
                            put = result

                    if found:
                        lex.manage_atoms(put.group(0))
                        word = word[put.end(0):]
                        continue

                    for separator in separators:
                        result = re.match('^' + re.escape(separator), word)
                        if result is not None:
                            found = True
                            put = result

                    if found:
                        lex.manage_atoms(put.group(0))
                        word = word[put.end(0):]
                        continue

                    for operator in operators:
                        result = re.match('^' + re.escape(operator), word)
                        if result is not None:
                            found = True
                            put = result

                    if found:
                        lex.manage_atoms(put.group(0))
                        word = word[put.end(0):]
                        continue

                    put = re.match(r"^[_a-zA-Z][_a-zA-Z0-9]*$", word)
                    if put is not None:
                        if lex.manage_identifiers(put.group(0)):
                            word = word[put.end(0):]
                            continue
                        else:
                            print("Lexical error on line " + str(line_number) + "(length of identifier)" + line)
                            break

                    put = re.match(r"^-?[0-9]+(\.[0-9]+)?", word)
                    if put is not None:
                        test = re.match(r"^-?[0-9]+(\.[0-9]+)?[_a-zA-Z]", word)
                        if test is not None:
                            lex.manage_constants(put.group(0))
                            word = word[put.end(0):]
                            continue
                        else:
                            print("Error on line " + str(line_number) + "(invalid identifier): " + line)
                            break

                if not found:
                    print("Error on line " + str(line_number) + ": " + line)
                    break

    sorted_ts_constants = sorted(lex.get_ts_constants(), key=lambda x: x[0])
    sorted_ts_identifiers = sorted(lex.get_ts_identifiers(), key=lambda x: x[0])
    fip = lex.get_fip().get_items()

    print("\nTS (Tabel identificatori ordonat lexicografic):")
    print("| Identificator   | Valoare".ljust(50))
    print("-" * 52)
    for identifier, data in sorted_ts_identifiers:
        print(f"| {identifier.ljust(15)} | {data['value']}".ljust(50))

    print("\nTS (Tabel constante ordonat lexicografic):")
    print("| Identificator   | Valoare".ljust(50))
    print("-" * 52)
    for identifier, data in sorted_ts_constants:
        print(f"| {identifier.ljust(15)} | {data['value']}".ljust(50))

    print("\nFIP:")
    print("| Cod Atom       | Adresa".ljust(50))
    print("-" * 52)
    for code, address in fip:
        print(f"| {code}{' ' * (15 - len(str(code)))} | {address}{' ' * (15 - len(str(address)))}")


if __name__ == '__main__':
    main()
