import sys
input = sys.stdin.readline

N = int(input())
trees = {}
for i in range(N):
    root, left, right = input().split()
    trees[root] = (left, right)

def preorder(node):
    if node == ".":
        return
    print(node, end="")
    preorder(trees[node][0])
    preorder(trees[node][1])

def inorder(node):
    if node == ".":
        return
    inorder(trees[node][0])
    print(node, end="")
    inorder(trees[node][1])

def postorder(node):
    if node == ".":
        return
    postorder(trees[node][0])
    postorder(trees[node][1])
    print(node, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")

    