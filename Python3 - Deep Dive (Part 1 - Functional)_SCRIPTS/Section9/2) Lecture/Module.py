print(f"------------------ Running {__name__} ------------------------")


def print_dict(header, d):
    print("\n\n---------------------------------------------")
    print(f"***** {header} ******")

    for key, value in d.items():
        print(key, value)

    print("---------------------------------------------\n\n")


print_dict("Module.globals", globals())

print(f"------------------ End of {__name__} ------------------------")
