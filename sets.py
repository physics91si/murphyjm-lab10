class Set(object):
	"""Set data structure that contains a collection of arbitrary objects, each element is unique."""
	def __init__(self):
		super(Set, self).__init__()
		self.elements = []

	def add(self, elem):
		"""Adds a single element to the set. If the set already contains the element to be added, nothing happens."""
		if not self.contains(elem):
			return self.elements.append(elem)

	def contains(self, elem):
		"""Returns a boolean indicating whether or not the set contains the element passed"""
		return (elem in self.elements)

	def remove(self, elem):
		"""Removes the element from the set. If the set does not contain the element, nothing happens."""
		if self.contains(elem):
			self.elements.remove(elem)

	def size(self):
		"""Returns an int containing the number of elements in the set."""
		return len(self.elements)

	def __or__(self, setB):
		"""Overrides the | operator. Returns a new set containing elements belonging to self or setB. Syntax: setC = setA | setB"""
		new_set = Set()
		new_set.elements = self.elements
		for elem in setB.elements:
			new_set.add(elem)
		return new_set

	def __and__(self, setB):
		"""Overrides the & operator. Returns a new set containing only the elements that were in both self and setB. Syntax: setC = setA & setB"""
		new_set = Set()
		for elem in setB.elements:
			if self.contains(elem):
				new_set.add(elem)
		return new_set

	def __sub__(self, setB):
		"""Overrides the - operator. Returns a new set containing all elements that were in self, but not setB. Syntax: setC = setA - setB"""
		new_set = Set()
		for elem in self.elements:
			if not setB.contains(elem):
				new_set.add(elem)
		return new_set