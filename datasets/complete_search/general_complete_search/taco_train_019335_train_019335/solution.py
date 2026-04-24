from collections import namedtuple
from bisect import bisect_left
import sys
Place = namedtuple('Place', 'lat, long, height, points')
chunkplaces = {}
chunkvals = {}
giant = False

def getkey(place, off_lat=0, off_long=0):
	return (place.lat // d_lat + off_lat) * 200011 + place.long // d_long + off_long

def recordvalue(place, val):
	if val < 0:
		return
	key = getkey(place)
	if key not in chunkplaces:
		chunkplaces[key] = []
		chunkvals[key] = []
	if giant:
		if len(chunkvals[key]) == 0:
			chunkvals[key].append(-val)
			chunkplaces[key].append(place)
		elif val < -chunkvals[key][0]:
			return
		else:
			chunkvals[key][0] = -val
			chunkplaces[key][0] = place
	else:
		i = bisect_left(chunkvals[key], -val)
		chunkplaces[key].insert(i, place)
		chunkvals[key].insert(i, -val)

def getbestinchunk(place, key, best):
	if key not in chunkvals:
		return 0
	for (i, (cand, val)) in enumerate(zip(chunkplaces[key], chunkvals[key])):
		if -val < best:
			return 0
		if abs(place.lat - cand.lat) <= d_lat and abs(place.long - cand.long) <= d_long:
			return -val
	return 0

def getbest(place):
	best = 0
	for i in [0, 1, -1]:
		for j in [0, 1, -1]:
			key = getkey(place, i, j)
			ret = getbestinchunk(place, key, best)
			if ret > best:
				best = ret
	return best

def calculatevalue(place):
	val = place.points + getbest(place)
	recordvalue(place, val)
	return val
(n, d_lat, d_long) = input().strip().split(' ')
(n, d_lat, d_long) = [int(n), int(d_lat), int(d_long)]
places = []
if d_lat == 200000:
	giant = True
for a0 in range(n):
	(latitude, longitude, height, points) = input().strip().split(' ')
	(latitude, longitude, height, points) = [int(latitude), int(longitude), int(height), int(points)]
	places.append(Place(latitude, longitude, height, points))
places.sort(key=lambda p: -p.height)
best = 0
for p in places:
	ret = calculatevalue(p)
	if ret > best:
		best = ret
print(best)
