###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = True # False - switch off, True - switch on
light_switch2 = True
bulbs_on = 0

def lightbulbs_on(s1, s2):
    result = 0
    if(s1):
        result += 1
    if(s2):
        result += 2
    return result

bulbs_on = lightbulbs_on(light_switch1, light_switch2)
print(bulbs_on)