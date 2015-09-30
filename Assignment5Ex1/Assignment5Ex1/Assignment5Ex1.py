firsttxt=raw_input("Please input text to reverse: ") #input text
#newtxt=txt[::-1]    #reversing string by extended slice
txt=list(firsttxt)
x=len(txt)
txt2=list(firsttxt)

"""
#TESTING#
print "txt"
print txt
print "x "+str(x)
print "txt2"
print txt2
#TESTING#
"""

while not x==0:
    y=x*(-1)
    z=x-1
    txt2[z] = txt[y]
    x-=1
    
newtxt="".join(txt2)
print(newtxt)       #print result