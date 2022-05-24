test = [1,5,6,4,1,4,5,1,12,2,20,10,10]#type your sample data here
print(sorted(test))
#even numbers
if len(test)%2 == 0:
    mid = (sorted(test)[int(len(test)/2)] + sorted(test)[int(len(test)/2)+1])/2
#odd number
else:
    mid = sorted(test)[int(len(test)/2)]
print(mid)
