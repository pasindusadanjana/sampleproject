def takeinput():
    global personalinfo,tankinfo,tanks
    personalinfo={"name":None,"mobile":None,"address":None,"Number of tanks":None}
    tankinfo={"height":None,"width":None,"length":None}
    tanks=[]
    for i in personalinfo:
        personalinfo[i]=input("Enter Your :"+i)
    personalinfo["Number of tanks"]=int(personalinfo["Number of tanks"])
    for j in range(personalinfo["Number of tanks"]):        
        fdbk=int(input("Enter what you want us to do for tank %d\n1.replace the bottom\n2.make new tank"%(j+1)))
        for i in tankinfo:
                if(fdbk==1):
                    if(i=="height") :
                        continue
                    tankinfo[i]=float(input("Enter Your :"+i+":"))
                else:
                    tankinfo[i]=float(input("Enter Your :"+i+":"))
        tanks.append(tankinfo)
        print(personalinfo,tanks)
        
def printbill():
    print("customer name",personalinfo["name"])
    print("customer mobile",personalinfo["mobile"])
    print("Delivery address",personalinfo["address"])
    calcost()
    for i in tanks:
        print("details of the takns %d"%(tanks.index(i)+1))
        print("area :",i["area"])
        print("price : ",i["price"])
        totalprice+=i["price"]
    print("toatl price",totalprice)
    
def calcost():
    global unitsqprice
    global profpercentage
    
    unitsqprice=10.0
    profpercentage=25.0
    for i in tanks:
        if(i["height"]==None):
            i["height"]=0
        area=2(i["height"]*i["length"])+2(i["height"]*i["width"])+(i["length"]*i["width"])
        cost =area*unitsqprice   
        price=cost*(1+profpercentage)
        tanks[tanks.index(i)].setdefault("area",area)
        tanks[tanks.index(i)].setdefault("cost",cost)
        tanks[tanks.index(i)].setdefault("price",price)
        
takeinput()
printbill()
