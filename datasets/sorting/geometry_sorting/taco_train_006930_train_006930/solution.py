def a():
	(t1, t2) = map(int, input().split())
	cinema = complex(*map(int, input().split()))
	house = complex(*map(int, input().split()))
	shop = complex(*map(int, input().split()))
	cinema_to_house = abs(house - cinema)
	cinema_to_shop = abs(shop - cinema)
	shop_to_house = abs(house - shop)
	alice_max = cinema_to_shop + shop_to_house + t1
	bob_max = cinema_to_house + t2

	def check(d):
		(c1, c2, c3) = ((cinema, d), (house, bob_max - d), (shop, alice_max - d - shop_to_house))
		for i in range(3):
			status = intersect(c1, c2)
			if status == 0:
				return False
			if status == 1:
				return intersect(c1 if c1[1] < c2[1] else c2, c3)
			for intersection in status:
				if abs(intersection - c3[0]) - 1e-10 <= c3[1]:
					return True
			(c1, c2, c3) = (c2, c3, c1)
	if cinema_to_shop + shop_to_house <= bob_max:
		print(min(alice_max, bob_max))
	else:
		(lower, upper) = (0, min(alice_max, bob_max))
		while upper - lower > 1e-10:
			mid = (lower + upper) * 0.5
			if check(mid):
				lower = mid
			else:
				upper = mid
		print(lower)

def intersect(a, b):
	dif = b[0] - a[0]
	dist = abs(dif)
	if dist > a[1] + b[1] + 1e-10:
		return 0
	if dist <= abs(a[1] - b[1]) - 1e-10:
		return 1
	k = (dist * dist + a[1] * a[1] - b[1] * b[1]) / (2 * dist)
	u = dif * k / dist
	v = dif * 1j / dist * (a[1] * a[1] - k * k) ** 0.5
	return [a[0] + u + v, a[0] + u - v]
a()
