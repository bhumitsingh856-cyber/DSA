def sum_product(arr):
    sm ,of=0,1
    for i in arr:
        sm+=i
        of*=i
    return {"sum":sm , "product":of}
print(sum_product([1,2,3,4,5]))
