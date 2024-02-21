#一位在中興應數的朋友向我求救的題目，他說是一堂叫微積分python的課給的課後思考題

def print_array(array):
    for i in array:
        print (str(i))

def create_array(n):
    a = [0]*n
    for i in range(n):
        a[i] = [0]*n
    return a

n = int(input("enter a num (n*n): "))

Array = [[1]]
start = 2
for i in range(2,n+1):
    if i%2 == 0:
        new_Array = create_array(i)
        for x in range(len(Array)):
            for y in range(len(Array)):
                new_Array[x][y] = Array[x][y]
        
        for row in range(i):
            new_Array[row][i-1]= start
            start +=1
        for col in range(i-2,-1,-1):
            new_Array[i-1][col]=start
            start +=1
        Array = new_Array.copy()
        print_array (Array)
        print("")


    elif i%2 != 0:
        new_Array = create_array(i)
        for x in range(len(Array)):
            for y in range(len(Array)):
                new_Array[x+1][y+1] = Array[x][y]

        for row in range(i-1,-1,-1):
            new_Array[row][0] = start
            start+=1
        for col in range(1,i):
            new_Array[0][col] = start
            start+=1
        Array = new_Array.copy()
        print_array (Array)
        print("")
