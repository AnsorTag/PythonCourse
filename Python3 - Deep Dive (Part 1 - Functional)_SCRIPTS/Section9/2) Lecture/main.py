print("===================================")

print(f"Running main.py - module name: {__name__}")

import Module

print("Importing Module again. . .")
del globals()["Module"]

import Module

Module.print_dict("main.globals", globals())
# import Module

Module.print_dict("main.globals", globals())

print("===================================")
