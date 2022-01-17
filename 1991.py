import sys

def solution() :
    n = int(sys.stdin.readline())
    tree = dict()
    
    for _ in range(n) :
        root, left, right = sys.stdin.readline().split()
        tree[root] = [left ,right]
    
    #1 전위 순회(preorder) -> root left right
    def preorder(root) :
        if root == '.' :
            return
        print(root, end = '') # root
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right

    #2 중위 순회(inorder) -> left root right
    def inorder(root) :
        if root == '.' :
            return
        inorder(tree[root][0]) # left
        print(root, end = '') # root
        inorder(tree[root][1]) # right
        
    #3 후위 순회(postorder) -> left right root
    def postorder(root) :
        if root == '.' :
            return
        postorder(tree[root][0]) # left
        postorder(tree[root][1]) # right
        print(root, end = '') # root

    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')
    
solution()