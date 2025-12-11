def ms_to_kmh(ms):
    result = ms *3600/1000
    return result

ms = float(input("MS: "))

print(ms_to_kmh(ms))