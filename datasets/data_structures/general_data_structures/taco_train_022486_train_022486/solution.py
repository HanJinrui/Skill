from collections import defaultdict
from dataclasses import dataclass
from random import random

def print_tree(tree, pfx=''):
	if tree is None:
		return
	print_tree(tree.left, pfx + ' ')
	print(f'{pfx}{tree.value}: {count(tree)}')
	print_tree(tree.right, pfx + ' ')

@dataclass
class Node:
	value: int
	count: int
	prior: float
	rev: bool
	left: 'Node'
	right: 'Node'
	parent: 'Node'

def prior(node):
	if node is None:
		return 0
	return node.prior

def count(node):
	if not node:
		return 0
	return node.count

def update_count(node):
	if node:
		node.count = count(node.left) + count(node.right) + 1

def heapify(node):
	if node is None:
		return
	max_prior = node.prior
	max_node = None
	if prior(node.left) > max_prior:
		max_prior = prior(node.left)
		max_node = node.left
	if prior(node.right) > max_prior:
		max_prior = prior(node.right)
		max_node = node.right
	if max_node:
		max_node.prior = node.prior
		node.prior = max_prior
		heapify(max_node)

def build(lookup, start, end):
	if start == end:
		return None
	middle = (start + end) // 2
	node = Node(middle, 0, random(), False, build(lookup, start, middle), build(lookup, middle + 1, end), None)
	for child in (node.left, node.right):
		if child:
			child.parent = node
	lookup[middle] = node
	heapify(node)
	update_count(node)
	return node

def push(t):
	if t is None:
		return
	if t.rev:
		t.rev = False
		(t.left, t.right) = (t.right, t.left)
		if t.left:
			t.left.rev ^= True
		if t.right:
			t.right.rev ^= True

def set_parent(node, par):
	if node:
		node.parent = par

def split(t, ix):
	if t is None:
		return (None, None)
	push(t)
	if count(t.left) < ix:
		(center, right) = split(t.right, ix - count(t.left) - 1)
		t.right = center
		set_parent(center, t)
		update_count(t)
		set_parent(t, None)
		set_parent(right, None)
		return (t, right)
	else:
		(left, center) = split(t.left, ix)
		t.left = center
		set_parent(center, t)
		update_count(t)
		set_parent(left, None)
		set_parent(t, None)
		return (left, t)

def merge(left, right):
	if left is None:
		return right
	push(left)
	push(right)
	if prior(left) >= prior(right):
		left.right = merge(left.right, right)
		set_parent(left.right, left)
		update_count(left)
		return left
	else:
		right.left = merge(left, right.left)
		set_parent(right.left, right)
		update_count(right)
		return right

def reverse(t, a, b):
	(left, not_left) = split(t, a)
	(center, right) = split(not_left, b - a + 1)
	if not center:
		return merge(left, right)
	center.rev = True
	not_right = merge(left, center)
	return merge(not_right, right)

def value(t, ix):
	push(t)
	if ix < count(t.left):
		return value(t.left, ix)
	elif ix == count(t.left):
		return t.value
	else:
		return value(t.right, ix - count(t.left) - 1)
	return t.value

def index_rec(t):
	if t.parent is None:
		return count(t.left)
	elif t.parent.left is t:
		return index_rec(t.parent) - count(t.right) - 1
	else:
		return index_rec(t.parent) + count(t.left) + 1

def index(t):
	parents = []
	p = t
	while p is not None:
		parents.append(p)
		p = p.parent
	while parents:
		push(parents.pop())
	return index_rec(t)
(N, Q) = (int(x) for x in input().split(' '))
node_lookup = [None for _ in range(N + 1)]
treap = build(node_lookup, 1, N + 1)
for _ in range(Q):
	(q, *args) = (int(x) for x in input().split(' '))
	if q == 1:
		(a, b) = args
		reverse(treap, a - 1, b - 1)
	elif q == 2:
		elem = args[0]
		pos = index(node_lookup[elem]) + 1
		print(f'element {elem} is at position {pos}')
	elif q == 3:
		pos = args[0]
		elem = value(treap, pos - 1)
		print(f'element at position {pos} is {elem}')
	else:
		raise ValueError(f"Unexpected argument: {q} {' '.join(args)}")
