#Ludrianna Bazile
#CS-175
#expensePieChart

import matplotlib.pyplot as plt

def main():
    try:
        
        expenseFile = open('expenses.txt','r')
        expenses = expenseFile.readlines()


        expenseList = []

        for expenseFile in expenses:
            e = expenseFile.strip().split('\t')
            expenseList.append(e)

        expenseFile.close()

        #Breaks down the list by variables for easier use 

        label1 = expenseList[0]
        category1 = label1[0]
        amount1 = int(label1[1])

        label2 = expenseList[1]
        category2 = label2[0]
        amount2 = int(label2[1])

        label3 = expenseList[2]
        category3 = label3[0]
        amount3 = int(label3[1])

        label4 = expenseList[3]
        category4 = label4[0]
        amount4 = int(label4[1])

        label5 = expenseList[4]
        category5 = label5[0]
        amount5 = int(label5[1])

        label6 = expenseList[5]
        category6 = label6[0]
        amount6 = int(label6[1])

        #Creates a list each cost amount
        cost = [amount1,amount2,amount3,amount4.amount5,amount6]

        #Creates a list of labels for the slices
        slice_labels = [category1, category2, category3, category4, category5, category6]

        # Add a title.
        plt.title('Expenses by Month')
            
        # Display the pie chart.
        plt.show()
    except ValueError:
        print("Invalid value detected. Must be valid number")
    except IOError:
        print("An error occured trying to read")
        print("the file ", expenses.txt)




# Call the main function.
if __name__ == '__main__':
    main()
