
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root


def inorder(root):
	if root:
		inorder(root.left)
		print(root.val, end=" ")
		inorder(root.right)

def printPreorder(root):
    if root:
        print(root.val, end=" "),
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end=" ")

if __name__ == '__main__':

	r = Node(50)
	r = insert(r, 30)
	r = insert(r, 20)
	r = insert(r, 40)
	r = insert(r, 70)
	r = insert(r, 60)
	r = insert(r, 80)

	inorder(r)
	print("\n")
	printPreorder(r)
	print("\n")
	printPostorder(r)
