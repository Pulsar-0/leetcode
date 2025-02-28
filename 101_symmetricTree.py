class Solution(object):
	def symmetricCheck(self, l, r):
		if not l and not r:
			return True
		if not l or not r or l.val != r.val:
			return False
		
		return (self.symmetricCheck(l.left, r.right) and self.symmetricCheck(l.right, r.left))

	def isSymmetric(self, root):
		return self.symmetricCheck(root.left, root.right)