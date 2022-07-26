b=int(input('Enter the points\n'))
if(b<=100 and b>=0):
    print("Genin ")
elif(b<=500 and b>100):
    print("Chunin")
elif(b<=1000 and b>500):
    print("Jonin ")
elif(b>1000):
    print("Hokage ")