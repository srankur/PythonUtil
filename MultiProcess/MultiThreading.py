import time
import threading

def calc_square(num):
    print("Calculating squares")
    for n in num:
        print("Square", n*n)

def calc_cube(num):
    print("Calculating Cubes")
    for n in num:
        print ("cube", n*n*n)

number = [1,2,3,4]

t = time.time()
t1 = threading.Thread(target = calc_square,args=(range(10),))
#t2 = threading.Thread(target = calc_cube, args = (range(10),))

t1.start()
#t2.start()

t1.join()
#t2.join()

print (" Thread Done in : ", time.time()-t )

start = time.time()
calc_square(range(10))
#calc_cube(range(10))

print (" Seq Done in : ", time.time()- start )

