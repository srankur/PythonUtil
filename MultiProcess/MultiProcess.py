# https://www.youtube.com/watch?v=sp7EhjLkFY4&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN&index=4

import time
import multiprocessing


result = []

def calc_square(num, q):
    global result
    print("Calculating squares")
    for n in num:
        result.append(n*n)
        q.put(n*n)

    print("Inside Process Address space", result )




if __name__ == "__main__":
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square, args=(range(10), q))

    p1.start()

    p1.join()

    # result is inside the address space
    print("Outside of the Process adddress space", result)

    # Queue is shared between the Process(IPC)
    while q.empty() is False:
        print(q.get(), end= " ")

