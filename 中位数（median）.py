test = [1,5,6,4,1,4,5,1,12,2,20,10,10]#在此键入你的数据
print(sorted(test))
#偶数
if len(test)%2 == 0:
    mid = (sorted(test)[int(len(test)/2)] + sorted(test)[int(len(test)/2)+1])/2
#奇数
else:
    mid = sorted(test)[int(len(test)/2)]
print(mid)
