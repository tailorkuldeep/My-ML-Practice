import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/home/kuldeep/Downloads/PCE-CS-III-ML-Club-master/Data Sets/Assignment4_SalaryData.csv")
print(df)

plt.plot(df.YearsExperience,df.Salary,color='red',linestyle='dotted', linewidth=2, marker='o', markerfacecolor='blue',markersize=3)
#setting x and y axis range
plt.xlim=(0,12)
plt.ylim=(0,120000)
#labelling axis
plt.xlabel('year of experience')
plt.ylabel('Salary')
plt.grid(True,color="black")
plt.title("experience vs salary graph")

plt.show()

