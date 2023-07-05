import random
import time
import concurrent.futures


def checkdis(x,y):
    dis = x*x+y*y
    if dis <= 1:
        return True
    return False

result_list = [0,0]

def checkpi(n):
    outlist = [0,0]
    for i in range(n):
        x = random.random()
        y = random.random()
        if checkdis(x,y):
            outlist[0] += 1
            continue
        outlist[1] += 1
    return outlist

num = 8
square = 8

if __name__ == "__main__":
    start_time_2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=num) as executor:
        futures = [executor.submit(checkpi,int(10**square/num))
                   for i in range(num)]
        for future in concurrent.futures.as_completed(futures):
            fut_list = future.result()
            for i in range(2):
                result_list[i] += fut_list[i]
    print("Operation time: " +
          str(time.time() - start_time_2), "seconds")

print(result_list)
print(result_list[0]*4/10**square)
