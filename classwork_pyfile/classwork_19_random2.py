import random
import pandas as pd

def random_generate(s, n):
    mList = [1]*n
    cents = int(s * 100 - n)

    for i in range(n - 1):
        cents_r = random.randint(0, int(2 * cents / (n - i)))
        mList[i] += cents_r
        cents -= cents_r
    mList[n-1] += cents
    for q in range(len(mList)):
        mList[q] /= 100 
    return mList



df = pd.DataFrame([],columns = list(range(1,11)))
for j in range(100):
    jList = random_generate(100, 10)
    df.loc[j] = jList


df.to_excel('random data.xlsx')


