import time
import math
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
names_1.sort()
names_2.sort()
duplicates = []

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def create_tree(sorted_array):
    return helper(sorted_array, 0, len(sorted_array) - 1)

def helper(sorted_array, left, right):
    if right < left:
        return None
    mid = math.floor((left + right) / 2)
    node = BinarySearchTree(sorted_array[mid])
    node.left = helper(sorted_array, left, mid - 1)
    node.right = helper(sorted_array, mid + 1, right)
    return node
tree = create_tree(names_2)


# def check_comparison(name):
#     index = 0
#     length = len(name)
#     first_letter = name[0]
#     first_letter.lower()
#     current_node = tree
#     current_first_letter = current_node.value[0]
#     current_first_letter.lower()
#     while 1 == 1:
#         if current_node == None:
#             return None
#         if current_node.value == name:
#             return duplicates.append(name)
#         if current_first_letter == first_letter:
#             index +=1
#             first_letter = name[index]
#             first_letter.lower()
#             current_first_letter = current_node.value[index]
#             current_first_letter.lower()
#         elif current_first_letter > first_letter:
#             if (index != 0):
#                 for i in range(0, index):
#                     if name[i] > current_node.value[i]:
#                         current_node = current_node.right
#                         return 1
#                     elif name[i] < current_node.value[i]:
#                         current_node = current_node.left
#                         return 1
                    
#             else:
#                 current_node = current_node.left
#                 current_first_letter = current_node.value[index]
#                 current_first_letter.lower()
#         else:
#             if (index != 0):
#                 while 1 == 1:
#                     i = 0
#                     if name[i] > current_node.value[i]:
#                         current_node = current_node.right
#                         break
#                     if name[i] < current_node.value[i]:
#                         current_node = current_node.left
#                         break
#                     i +=1
#                     if i == index:
#                         break
#                     print(i)
#             else:
#                 current_node = current_node.right    
#                 current_first_letter = current_node.value[index]
#                 current_first_letter.lower()
#         print(current_node.value, current_node.right.value, current_node.left.value, first_letter, current_first_letter)
        
        
def contains(self, target):
    current_node = self
    while 1 == 1:
        if current_node.value == target:
            return True
        elif target > current_node.value:
            current_node = current_node.right
        else: 
            current_node = current_node.left
        if current_node == None:
            return False
for name in names_1:
    if contains(tree, name) is not False:
        duplicates.append(name)
# print(check_comparison("Dominique Beck"))
# print(duplicates)
# duplicates = set(names_1) & set(names_2)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
