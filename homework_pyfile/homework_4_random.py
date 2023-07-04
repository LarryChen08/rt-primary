#Casino3
import random
import time
import matplotlib.pyplot as plt
import concurrent.futures

def sortlist(list1):
    resList = []
    for item in list1:
        if resList == []:
            resList.append(item)
            continue
        for i in range(len(resList)):
            if item > resList[i]:
                resList.insert(i,item)
                break
    return resList

result_list = [0,0,0,0]
def check(a):
    out_list = [0,0,0,0]
    for i in range(int(a*(10**8)/len(number_list))):
        d1,d2,d3 = random.randint(1,6),random.randint(1,6),random.randint(1,6)
        dList = [d1,d2,d3]
        dList = sortlist(dList)       
        #baozi
        if d1 == d2 == d3:
            out_list[0] += 1
        #shunzi
        elif d1 - d2 == 1 and d2 - d3 == 0:
            out_list[1] += 1
        #duizi
        elif d1 == d2 or d1 == d3 or d2 == d3:
            out_list[2] += 1
        #else
        else:
            out_list[3] += 1
    return out_list

number_list = [1,1,1,1,1,1,1,1]

if __name__ == "__main__":
    start_time_2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=len(number_list)) as executor:
        futures = [executor.submit(check, item)
                   for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            fut_list = future.result()
            for i in range(4):
                result_list[i] += fut_list[i]
    print("Operation time: " +
          str(time.time() - start_time_2), "seconds")

print(result_list)#[2778765, 2313942, 39353145, 55554148]

x = ['baozi','shunzi','duizi','else']
y = result_list

plt.subplot(2,1,1)
plt.bar(x,y,width=0.8,label='Times')
plt.title('Appereance comparison')
plt.ylabel('Times')
plt.xlabel('Combinations')
plt.ylim(0,80000000)
for a,b in zip(x,y):
    plt.text(a,b,b,va='bottom',ha='center')
plt.grid(axis='y')
plt.legend(loc='upper left')

plt.subplot(2,1,2)
plt.pie(y,labels=x,autopct='%4f%%',labeldistance=1.1,startangle=90)
plt.show