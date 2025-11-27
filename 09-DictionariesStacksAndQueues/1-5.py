countries = [
{"name":"Poland", "population":38000000},
{"name":"Poland2", "population":83000000}
]

for e in countries:
    for k,v in e.items():
        print(f"{k}: {v}", end=' ')
    print()