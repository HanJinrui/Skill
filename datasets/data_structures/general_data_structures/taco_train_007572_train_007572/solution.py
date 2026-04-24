from collections import namedtuple
import bisect
DistTuple = namedtuple('distance', ['h', 'v'])

def insort_right(arr, dist, hv):
	x_key = dist.h if hv == 'h' else dist.v
	lo = 0
	hi = len(arr)
	while lo < hi:
		mid = (lo + hi) // 2
		a_mid = arr[mid].h if hv == 'h' else arr[mid].v
		if x_key < a_mid:
			hi = mid
		else:
			lo = mid + 1
	arr.insert(lo, dist)

def bisect_right(arr, x_key, hv):
	lo = 0
	hi = len(arr)
	while lo < hi:
		mid = (lo + hi) // 2
		a_mid = arr[mid].h if hv == 'h' else arr[mid].v
		if x_key < a_mid:
			hi = mid
		else:
			lo = mid + 1
	return lo

class DistsGroup:

	def __init__(self):
		self.delta_h = 0
		self.delta_v = 0
		dist = DistTuple(0, 0)
		self.dists_h_sorted = [dist]
		self.dists_v_sorted = [dist]

	def append_dist(self, h, v, append=True):
		self.delta_h += h
		self.delta_v += v
		dist = DistTuple(-self.delta_h, -self.delta_v)
		if append:
			insort_right(self.dists_h_sorted, dist, 'h')
			insort_right(self.dists_v_sorted, dist, 'v')
		index_h = bisect_right(self.dists_h_sorted, H_max - self.delta_h, 'h')
		for elem in self.dists_h_sorted[index_h:]:
			self.dists_v_sorted.remove(elem)
		del self.dists_h_sorted[index_h:]
		index_v = bisect_right(self.dists_v_sorted, V_max - self.delta_v, 'v')
		for elem in self.dists_v_sorted[index_v:]:
			self.dists_h_sorted.remove(elem)
		del self.dists_v_sorted[index_v:]
		if append:
			paths_count = max(0, len(self.dists_v_sorted) - 1)
			return paths_count

	def append_group(self, other_group, h, v):
		good_cross_paths = 0
		other_group.append_dist(h, v, False)
		dists_h1 = self.dists_h_sorted
		delta_h1 = self.delta_h
		delta_v1 = self.delta_v
		dists_h2 = other_group.dists_h_sorted
		delta_h2 = other_group.delta_h
		delta_v2 = other_group.delta_v
		dists_only_v2 = []
		dist_h2_index = 0
		dist_h2_len = len(dists_h2)
		if len(dists_h1) and len(dists_h2) and (dists_h1[-1].h + delta_h1 + dists_h2[-1].h + delta_h2 < H_max) and (self.dists_v_sorted[-1].v + delta_v1 + other_group.dists_v_sorted[-1].v + delta_v2 < V_max):
			good_cross_paths += len(dists_h1) * len(dists_h2)
		else:
			for dist_h1 in reversed(dists_h1):
				rest_h = H_max - (dist_h1.h + delta_h1)
				rest_v = V_max - (dist_h1.v + delta_v1)
				while dist_h2_index < dist_h2_len:
					if dists_h2[dist_h2_index].h + delta_h2 <= rest_h:
						bisect.insort_right(dists_only_v2, dists_h2[dist_h2_index].v + delta_v2)
						dist_h2_index += 1
					else:
						break
				dist_v2_index = bisect.bisect_right(dists_only_v2, rest_v)
				good_cross_paths += dist_v2_index
		for dist_h2 in dists_h2:
			dist_new = DistTuple(dist_h2.h + delta_h2 - delta_h1, dist_h2.v + delta_v2 - delta_v1)
			self.dists_h_sorted.append(dist_new)
			self.dists_v_sorted.append(dist_new)
		self.dists_h_sorted.sort()
		self.dists_v_sorted.sort(key=lambda k: k.v)
		return good_cross_paths
good_paths = 0
(N, H_max, V_max) = map(int, input().split())
junctions = {}
for i in range(1, N + 1):
	(xi, yi) = map(int, input().rstrip().split())
	junctions[i] = {'x': xi, 'y': yi, 'edges': [], 'dists_group': None}
for i in range(1, N):
	(ui, vi) = map(int, input().rstrip().split())
	dH = abs(junctions[ui]['x'] - junctions[vi]['x'])
	dV = abs(junctions[ui]['y'] - junctions[vi]['y'])
	junctions[ui]['edges'].append({'junction_id': vi, 'dH': dH, 'dV': dV})
	junctions[vi]['edges'].append({'junction_id': ui, 'dH': dH, 'dV': dV})
one_edge_queue = []
for (key, value) in junctions.items():
	edge_count = len(junctions[key]['edges'])
	junctions[key]['edge_count'] = edge_count
	if edge_count == 1:
		one_edge_queue.append(key)
		junctions[key]['dists_group'] = DistsGroup()
while len(one_edge_queue) > 1:
	junction_id = one_edge_queue[0]
	edge_to_next = junctions[junction_id]['edges'][0]
	next_junction_id = edge_to_next['junction_id']
	if junctions[next_junction_id]['dists_group']:
		paths_added = junctions[next_junction_id]['dists_group'].append_group(junctions[junction_id]['dists_group'], edge_to_next['dH'], edge_to_next['dV'])
		good_paths += paths_added
	else:
		dists_group = junctions[junction_id]['dists_group']
		paths_added = dists_group.append_dist(edge_to_next['dH'], edge_to_next['dV'])
		good_paths += paths_added
		junctions[next_junction_id]['dists_group'] = dists_group
	for edge in junctions[next_junction_id]['edges']:
		if edge['junction_id'] == junction_id:
			junctions[next_junction_id]['edges'].remove(edge)
			break
	if len(junctions[next_junction_id]['edges']) == 1:
		one_edge_queue.append(next_junction_id)
	one_edge_queue.remove(junction_id)
print(int(N * (N - 1) / 2) - good_paths)
