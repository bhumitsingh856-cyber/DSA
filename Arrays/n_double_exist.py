# def double_exist(arr):
#     for i in range(len(arr) - 1):
#         for j in range(i + 1, len(arr)):
#             if arr[i] * 2 == arr[j]:
#                 return True
#     return False

def double_exist(arr):
    arr.sort()
    p1=0
    p2=len(arr)-1
print(double_exist([3, 1, 7, 11, 6]))
