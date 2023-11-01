#Ludrianna Bazile
#MA130
#AverageFromInput


def main():
    total = 0
    number = 0
    counter = 1
    average = 0

    f = open('numbers.txt','r')

    for i in f:
        number = int(i)
        total = total + number
        print ("I read in ",counter,"number(s) Current number is:    ",number," Total is:    ", total)
        counter = counter + 1
    f.close()

    average = total / (counter-1)

    print("Average: ",average)


if __name__ == '__main__':
    main()
    
