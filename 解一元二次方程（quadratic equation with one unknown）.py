#请将待计算一元二次方程化为一般形式，然后输入二次项系数、一次项系数、常数项
#若该一元二次方程有实数根，将输出其两个实数根；反之，将输出根的判别式并报出无实根
a,b,c=float(input('a')),float(input('b')),float(input('c'))#输入（对应一般形式的a,b,c）
d=(b*b)-(4*a*c)#计算判别式
print("根的判别式为",d)
if d>=0:            #有实根
    m=(b**2-4*a*c)**0.5#计算根德尔塔
    print("该一元二次方程有实数根，为",(m-b)/2/a,(-m-b)/2/a)

if d<0:             #无实根
    print("该一元二次方程无实数根") 

    
#Update: Cancel the error report when the original equation has no real roots, and instead report "This one-dimensional quadratic equation has no real roots"(2022/6/1)
