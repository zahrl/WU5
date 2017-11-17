class node():
	def __init__(self, data):
		self.data = data;
		self.left_child = None
		self.right_child = None

class output_tree():
	def __init__(self, node):
		if node.data:
			print(node.data)
		if node.left_child:
			output_tree(node.left_child)
		if node.right_child:
			output_tree(node.right_child)

tree = node("Habsburg")
tree.left_child = node("Joseph I.")
tree.right_child = node("Charles VI.")
tree.left_child.left_child = node("Maria Josepha")
tree.left_child.right_child = node("Maria Amalia")
tree.right_child.left_child = node("Maria Theresa")
tree.right_child.right_child = node("Maria Anna")

output_tree(tree)