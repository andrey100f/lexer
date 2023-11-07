type_of_atoms = {
    "identifier": 0,
    "constant": 1,
}

keywords = {
    "integer": 2,
    "real": 3,
    "string": 4,
    "char": 5,
    "bool": 6,
    "list": 7,
    "object": 8,
    "function": 9,
    "if": 10,
    "else": 11,
    "elif": 12,
    "for": 13,
    "while": 14,
    "break": 15,
    "continue": 16,
    "read": 17,
    "write": 18,
    "begin": 19,
    "end": 20,
    "of": 21,
    "then": 22,
}

separators = {
    ",": 23,
    ";": 24,
    ".": 25,
    "(": 26,
    ")": 27,
    "[": 28,
    "]": 29,
    "{": 30,
    "}": 31,
    ":": 32,
}

operators = {
    "+": 33,
    "-": 34,
    "*": 35,
    "/": 36,
    "%": 37,
    "^": 38,
    "~": 39,
    "=": 40,
    "!=": 41,
    "<": 42,
    ">": 43,
    "<=": 44,
    ">=": 45,
    "!": 46,
    "&": 47,
    "|": 48,
}

atoms = {**keywords, **separators, **operators}
