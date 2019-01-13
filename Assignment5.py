import pandas as pd

df=pd.read_csv('/home/kuldeep/Downloads/PCE-CS-III-ML-Club-master(1)/PCE-CS-III-ML-Club-master/Data Sets/Assignment5.csv',names=['li','l2'])
print(df)
temp=[]
dt2=[]
i=0 
while(i<5):
    while(1):
        temp.append(df.loc[i]['l1'])
        if(df.loc[i]['l1'] == df.loc[i]['l2']):
            dt2.append(temp)
            temp=[]
            dt2.append([df.loc[i]['l1']])
            i+=1
            break
        i +=1
print(dt2)
