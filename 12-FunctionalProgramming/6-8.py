grades = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
   return lambda pts: pts>=limit

limit = int(input("Minimal grade: "))

print(list(filter(min_pts(limit), grades)))
