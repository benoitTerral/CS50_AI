from dataclasses import dataclass


@dataclass
class Node:
	state: any
	parent: any
	action: any


class StackFrontier():
	def __init__(self):
		self.frontier = []
		
	def add(self, node):
		self.fronter.append(node)

	def contains_state(self, state):
		return any(node.state == state for node in self.frontier)
	
	def enpty(self):
		return len(self.frontier) == 0
	
	def remove(self):
		if self.empty():
			raise Exception("empty frontier")
		else:
			node = self.frontier[-1]
			self.frontier = self.frontier[:-1]
			return node


class QueueFrontier(StackFrontier):
	def remove(self):
		if self.empty():
			raise Exception("empty frontier")
		else:
			node = self.frontier[0]
			self.frontier = self.frontier[1:]
			return node


class Maze():


	def __init__(self, filename):
		with open(filename) as f:
			contents = f.read()
		if contents.count("A") != 1:
			raise Exception("One and only one starting position accepted")
		if contents.count("B") != 1:
			raise Exception("One and only one goal accepted")

