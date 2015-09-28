C=raw_input("Temperature in Celcius? ")
while True:
    try:
       float(C)
       break
    except:
        C=raw_input("The temperature has to be a number. Please input the temperature again: ")
Cfloat=float(C)
while Cfloat<-273.15:
    C=raw_input("The temperature cannot be lower than -237.15 degrees Celcius. Please input the temperature again: ")
    Cfloat=float(C)
else:
    K=Cfloat+273.15
    print("%s degrees Celcius converts to %s degrees Kelvin!") %(C, str(K))