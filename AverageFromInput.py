#Ludrianna Bazile
#MA130
#AverageFromInput



def getValues():
    
    
    f = open('numbers.txt','r')
    number = 0

    global total
    total = 0

    global counter 
    counter = 1
    
    for i in f:
        number = int(i)
        total = total + number
        print (f"I read in {counter} number(s) Current number is: {number} Total is: {total}")
        counter = counter + 1
    f.close()
    

    
def getAverage():
    global average
    average = (total/(counter-1))
    
    
def printAverage():
    print(f"Average = {average}")

def main():
    
    getValues()
    getAverage()
    printAverage()

    


if __name__ == '__main__':
    main()

