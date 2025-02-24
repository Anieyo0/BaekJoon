import sys
input = sys.stdin.readline
from collections import defaultdict

# 전위 순회 (루트 -> 왼쪽 -> 오른쪽)
def preorder(node):
    if node == blank:
        return

    pre_result.append(node)
    preorder(tree[node][0])
    preorder(tree[node][1])


# 중위 순회 (왼쪽 -> 루트 -> 오른쪽)
def inorder(node):
    if node == blank:
        return

    inorder(tree[node][0])
    in_result.append(node)
    inorder(tree[node][1])


# 후위 순회 (왼쪽 -> 오른쪽 -> 루트)
def postorder(node):
    if node == blank:
        return

    postorder(tree[node][0])
    postorder(tree[node][1])
    post_result.append(node)
    

N = int(input())

tree = defaultdict(list)
for _ in range(N):
    parent, left, right = input().split()
    tree[parent].append(left)
    tree[parent].append(right)
    
root = 'A'
blank = '.'

pre_result, in_result, post_result = [], [], []  # 순회 결과 저장용 리스트

preorder(root)
inorder(root)
postorder(root)

print("".join(pre_result))
print("".join(in_result))
print("".join(post_result))