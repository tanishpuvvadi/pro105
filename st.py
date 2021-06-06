import statistics 
import math 
import csv 
with open("st.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
n = len(data)
total = 0
for x in data: 
    total = total+int(x)
mean  = total/n 
sqlist = []
for i in data:
    a = int(i)-mean
    a = a**2
    sqlist.append(a)
sum = 0
for i in sqlist:
    sum = sum+i
result = sum/(len(data)-1)
st = math.sqrt(result)
print(st)
