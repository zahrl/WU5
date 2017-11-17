class binary_tree():
	def __init__(self, root_name):
		self.data = root_name
		self.left_child = None
		self.right_child = None

class node():
	def __init__(self, data):
		self.data = data;
		self.left_child = None
		self.right_child = None

class output_tree(): # breadth first
	def __init__(self, root):
		print("ROOT: " + root.data)
		next_left = root.left_child
		while next is not None:
			print("LEFT CHILD: " + next.data)
			next = next.left_child

tree = binary_tree("Habsburg")
tree.root = "Habsburg"
tree.left_child = node("Joseph I.")
tree.right_child = node("Charles VI.")
tree.left_child.left_child = node("Maria Josepha")
tree.left_child.right_child = node("Maria Amalia")
tree.right_child.left_child = node("Maria Theresa")
tree.right_child.right_child = node("Maria Anna")

output_tree(tree)
