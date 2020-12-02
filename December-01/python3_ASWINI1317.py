import math
number =int(input())
sq = int(math.pow (number, 2))
digits=""
for x in str(sq):
    digits += x 
l=len(digits)
split=l//2
f=digits[:split]
s=digits[split:]
add=int(f)+int(s)
if(add==number) and (number%3==0):
    print("Room:", number)
    print("status:safe")
else:
    print("Room:", number)
    print("status:unsafe")

