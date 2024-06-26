
"""
# Distance in astronomical units
auplanets = {'Jupiter' : 5.203,
             'Saturn'  : 9.539,
             'Uranus'  : 19.2,
             'Neptune' : 30.0611}

result = {kv[0]:kv[1]*149.597870 for kv in auplanets.items()}
print(result)
"""

planets = {'Mercury' : 57.91,
           'Venus'   : 108.2,
           'Earth'   : 149.597870,
           'Mars'    : 227.94,
           'Jupiter' : 778.36,
           'Saturn'  : 1427.014,
           'Uranus'  : 2872.28,
           'Neptune' : 4497.077}

# Sort by distance from the Earth
print(planets)
dist = sorted(planets.items(),key=lambda kv:kv[1])
print(dist)

for kv in dist:
    print("{0:<8s} {1:08.2f} Gm".format(kv[0],kv[1]))

