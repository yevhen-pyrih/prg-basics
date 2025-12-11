def avg_speed(distance,hours,minutes):
    return distance/(hours + minutes/60)

d = float(input("Distance: "))
h = float(input("Hours: "))
m = float(input("Minutes: "))

print(avg_speed(d,h,m))