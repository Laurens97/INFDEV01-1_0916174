n1=input("Please put in a number, and maybe I'll convert it to an absolute number if I'm in a good mood: ")
n2=float(n1)
if n2<0:
    n3=n2*(-1)
    print("The absolute value of %s is %s. That was a hard one...") %(n1, n3)
else:
    print("The absolute value of %s is %s. Didn't even break a sweat.") %(n1, str(n2))