#for y in map(lambda x:"%s%s%s"%(""if x%3 else"Fizz",""if x%5 else"Buzz",str(x) if x%3*x%5 else ""),range(1,101)):print y
#for y in map(lambda x:{0:"Fizz"}.get(x%3,"")+{0:"Buzz"}.get(x%5,"")+(str(x) if x%3*x%5 else ""),range(1,101)):print y
#for y in map(lambda x:{0:"Fizz"}.get(x%3,"")+{0:"Buzz"}.get(x%5,"")+{0:""}.get(x%3*x%5,str(x)),range(1,101)):print y

# 106
def y(x):print{0:"Fizz"}.get(x%3,"")+{0:"Buzz"}.get(x%5,"")+{0:""}.get(x%3*x%5,str(x))
map(y,range(1,101))
