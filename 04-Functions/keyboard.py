###
# Functions to read any data type from the keyboard
#
def input_string(message):
    result = input(message)
    return result

def input_integer(message):
    result = int(input(message))
    return result

def input_real(message):
    result = float(input(message))
    return result

def input_boolean(message):
    result = input(message)
    if(result == "y"):
        result = True
    elif result == "n":
        result = False
    return result

if __name__ == "__main__":
    input_boolean("Write boolean")