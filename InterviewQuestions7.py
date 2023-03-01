import math
def twins(age, dist, frac):
    c=299792458 #speed of light
    dist*=2#as it's a round trip
    #converting to SI units
    speed=frac*c
    dist*=(60*60*24*365*c)
    
    T0=dist/speed
    
    T=T0*(math.sqrt(1-((frac*frac))))
    #converting to years
    T/=(60*60*24*365)
    T0/=(60*60*24*365)

    T=round(T,1)
    T0=round(T0,1)

    print("Jack's age is "+str(T+age)+", Jill's age is "+str(T0+age)+" :p")

twins(20,10,0.4)
twins(20,10,0.8)
twins(10,16.73,0.999)