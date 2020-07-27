class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node
            else: 
                insert(root.left, node)
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val,end=" ") 
        inorder(root.right)

arr = list(map(int,input().split()))
n = int(input())
l = []
for i in range(len(arr)):
    if n - arr[i] in arr and arr[i]!=n-arr[i]:
        if arr[i] not in l:
            l.append(arr[i])
        if n-arr[i] not in l:
            l.append(n-arr[i])
    elif n-arr[i] in arr and arr[i]==n-arr[i] and arr.count(arr[i])>0:
        if arr[i] not in l:
            l.append(arr[i])
        if n-arr[i] not in l:
            l.append(n-arr[i])
        
if len(l)>0:
    x=Node(l[0])
#print(*l)
    for i in range(1, len(l)):
        insert(x, Node(l[i]))
    inorder(x)
else:
    print(-1)
