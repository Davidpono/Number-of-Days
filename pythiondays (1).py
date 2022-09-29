
#program that counts the amount of days between a gieven data and then tells you how much informations
#has been transmitted givent he perceateg of time the data is being transmited and how fast the transmiission is
#fucntions checks if year is leap year
def checkYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False
def checkYear900(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
                return True
        else:
             return True
    else:
        return False       
#gets a string removes - hashes and makes them into a list then turns the elements into ints and checks months arent above 12 no negeative months no negative years the days input corralte witht he months like no more than 31 days for jan etc etc
def makelist():
    print("Enter starting date in this format month-date-year all digits")
    start = input()
    print("Enter ending date in this format month-date-year all digits")
    ending = input()
    startstring = start.replace("-", " ")
    endingtring = ending.replace("-", " ")
    startlist=startstring.split()
    endinglist=endingtring.split()
    startlist = [int(i) for i in startlist]
    endinglist = [int(i) for i in endinglist]
    if(startlist[0]>12 or startlist[0]==0 ):
        print("starting month is greater than 12 invalid entry please fix month")
        s = input()
        s = int(s)
        startlist[0]=s
    if(endinglist[0]>12 or endinglist[0]==0):
        print("ending month is greater than 12 invalid entry please fix month")
        s = input()
        s = int(s)
        endinglist[0]=s

    if(startlist[2]>endinglist[2]):
        print("Your starting year is lower than ending year please fix ending year")
        s = input()
        s = int(s)
        endinglist[2]=s
    if (startlist[0]>endinglist[0]) and (endinglist[2]-startlist[2]<=0):
            print("you are in negative months please correct ending month")
            s = input()
            s = int(s)
            endinglist[0]=s
    if (startlist[0]==1 or startlist[0]==3 or startlist[0]==5 or startlist[0]==7 or startlist[0]==8 or startlist[0]==10 or startlist[0]==12 )  and startlist[1] >31:
        print("date is out of range for given startingmonth please input correct date")
        s = input()
        s = int(s)
        startlist[1]=s
    if (startlist[0]==4 or startlist[0]==6 or startlist[0]==9 or startlist[0]==11)  and startlist[1] >30:
        print("date is out of range for given startingmonth please input correct date")
        s = input()
        s = int(s)
        startlist[1]=s
    if startlist[0]==2 and startlist[1] >29:
        print("date is out of range for given startingmonth please input correct date")
        s = input()
        s = int(s)
        startlist[1]=s
        if checkYear(startlist[2])==0 and startlist[1] >28:
            print("date is out of range for given startingmonth please input correct date")
            s = input()
            s = int(s)
            startlist[1]=s
    if (endinglist[0]==1 or endinglist[0]==3 or endinglist[0]==5 or endinglist[0]==7 or endinglist[0]==8 or endinglist[0]==10 or endinglist[0]==12 )  and endinglist[1] >31:
        print("date is out of range for given  ending month please input correct date")
        s = input()
        s = int(s)
        endinglist[1]=s
    if (endinglist[0]==4 or endinglist[0]==6 or endinglist[0]==9 or endinglist[0]==11)  and endinglist[1] >30:
        print("date is out of range for given ending month please input correct date")
        s = input()
        s = int(s)
        endinglist[1]=s
    if endinglist[0]==2 and endinglist[1] >29:
        print("date is out of range for given edding month please input correct date")
        s = input()
        s = int(s)
        endinglist[1]=s
        if checkYear(endinglist[2])==0 and endinglist[1] >28:
            print("date is out of range for ending given month please input correct date")
            s = input()
            s = int(s)
            endinglist[1]=s
    return startlist, endinglist



#calcualtions for the days ittirates over list for how many months there is 
def getdays():
    startlist, endinglist = makelist()
    monthlist =[1,2,3,4,5,6,7,8,9,10,11,12]
    monthlist.extend([0]*1)
    currentmonth = startlist[0]
    endingmonth = endinglist[0]
    currentyear = startlist[2]
    endingyear = endinglist[2]
    startyear = currentyear
    ogstartingday = startlist[1]
    ogendingdate = endinglist[1]
    days=0
    months = 1
    years = endingyear -currentyear

    y=0
    i=currentmonth-1
    m= 0
    n=0
    var=0
    #checks how many months there is in between the given years
    if years == 1:
        months=12-currentmonth+endingmonth
    if years>1:
        months=12-currentmonth+endingmonth+(12*(years-1))
    if years==0:
        months=endingmonth-currentmonth
        var=1
    leap=0

    #ittirates through araray the amount of months there is and for each itteration there is an equivelnt amount of days that its added if arr[0]=1 jan then adds equivelnt amount tot he count
    while n < months and var==0:
            if(i==12):
                
                m=0
                i=0
                startyear += 1
            if(monthlist[i] == 1):
                days=days+31
            if(monthlist[i] == 2):

                if(checkYear(startyear) and startyear>1582):
                    
                    days=days+29
                    
                    leap += 1
                else:
                     
                    days=days+28
            if(monthlist[i] == 3):
                days=days+31
            if(monthlist[i] == 4):
                days=days+30
            if(monthlist[i] == 5):
                days=days+31
            if(monthlist[i] == 6):
                days=days+30
            if(monthlist[i] == 7):
                days=days+31
            if(monthlist[i] == 8):
                days=days+31
            if(monthlist[i] == 9):
                days=days+30
            if(monthlist[i] == 10):
                days=days+31
            if(monthlist[i] == 11):
                days=days+30
            if(monthlist[i] == 12):
                days=days+31
            i += 1
            m += 1
            n += 1
        #checks the starting date and ending date to add to the count 
    temp = days+ogendingdate-ogstartingday
    
    p = ogendingdate-ogstartingday

    return temp



temp=getdays()

print("Number of days")
print(temp)
print("Enter percentage in decimal")

p= input() 
p=float(p)
print("Enter enter how many MB")   
k= input()  
k=float(k)
#amount of date in bytes is calculated by percentage of time transimited tthere is x days * 86400 seconds/day * percentage* amount of megabyte * 2^20
datapersecinbytes=temp*86400*p*k*(1/8)
#datapersecinbytes=temp*86400*p*k*1000000
#bytes/kilobytes
datainkilo=datapersecinbytes/pow(2,10)
#bytes/megabytes
datainmega=datapersecinbytes/pow(2,20)
#bytes/gigaytes
dataingiga=datapersecinbytes/pow(2,30)

print("Data ammount in MB")
print(datapersecinbytes)
print("Data ammount in GB")
print(datainkilo)
print("Data ammount in TB")
print(datainmega)
print("Data ammount in PB")
print(dataingiga)


