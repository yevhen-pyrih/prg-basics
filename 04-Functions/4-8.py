def time_string(hours, minutes, time_format="24"):
    time = ""
    if(time_format == "24"):
        time = f"{hours}:{minutes}"
    elif time_format== "12":
        if(hours>12):
            time = f"{hours-12}:{minutes}pm"
        else:
            time = f"{hours}:{minutes}am"
    return time


print(time_string(12, 45))
print(time_string(22, 12, "12"))
print(time_string(14, 30, "12"))
print(time_string(7, 30, "12"))
print(time_string(7, 30))


