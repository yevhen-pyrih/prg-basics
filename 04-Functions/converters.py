def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_in(n):
    return n/2.54


def in_to_cm(n):
    return n*2.54


def feet_to_cm(n):
    return n*30

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')

    print(f'532feet = {feet_to_cm(532)}cm')
    print(f'532cm = {cm_to_in(532)}in')
    print(f'532in = {in_to_cm(532)}cm')




