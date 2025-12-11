ratings = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]
# list(filter(lambda y: not y == max(x) and not y == min(x), x))

players = list(map(lambda x: sum(x)-min(x)-max(x), ratings))

print(players)