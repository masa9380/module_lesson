myvariable = "This is global variable"


def myfunc():
    print("This is my function!")

def _anotherfunc():
    print('This is another function!')

if __name__ == "__main__":
    print('This is my module!!')
    print(f'mymodule.__name__:{__name__}')