import pandas as pd

df=pd.read_csv('/home/kuldeep/Downloads/PCE-CS-III-ML-Club-master(1)/PCE-CS-III-ML-Club-master/Data Sets/Assignment5.csv',names=['li','l2'])
print(df)
temp=[]
dt2=[]
i=0 
while(i<5):
    j=i
    while(1):
        temp.append(df.loc[j]['l1'])
        if(df.loc[j]['l1'] == df.loc[j]['l2']):
            dt2.append(temp)
            temp=[]
            j+=1
            break
        j +=1
    i+=1
print(dt2)
