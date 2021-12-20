import csv
from collections import Counter
with open("height-weight.csv",newline="")as f:
    r=csv.reader(f)
    data=list(r)
data.pop(0)
newdata=[]
for i in range(len(data)):
    n_num=data[i][1]
    newdata.append(float(n_num))
n=len(newdata)
total=0
for x in newdata:
    total +=x
mean=total/n
print("Mean (Average) is -> "+str(mean))
n1=len(newdata)
newdata.sort()
if n1%2==0:
    m1=float(newdata[n//2])
    m2=float(newdata[n//2-1])
    median=(m1+m2)/2
else:
    median=newdata[n//2]
print("Median is -> "+str(median))
d=Counter(newdata)
mdr={
    "50-60":0,
    "60-70":0,
    "70-80":0,
}
for h,o in d.items():
    if 50<float(h)<60:
        mdr["50-60"] +=o
    elif 60<float(h)<70:
        mdr["60-70"] +=o
    elif 70<float(h)<80:
        mdr["70-80"] +=o
mr,mo=0,0
for r,o in mdr.items():
    if o > mo:
        mr,mo=[int(r.split("-")[0]),int(r.split("-")[1])],o
mode=float((mr[0]+mr[1])/2)
print(f"Mode is -> {mode:2f}")