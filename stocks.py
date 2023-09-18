COMMISSION_RATE_PURCHASE = float(input("Enter commission rate percentage on stock purchase: "))
COMMISSION_RATE_SALE = float(input("Enter commission rate percentage on stock sale: "))
NUM_SHARES_PURCHASE = float(input("Enter the number of shares purchased: "))
NUM_SHARES_SOLD = float(input("Enter the number of shares sold: "))
PURCHASE_PRICE = float(input("Enter purchase price per share: "))
SELLING_PRICE = float(input("Enter sell price per share: "))


amountPaidForStock = NUM_SHARES_PURCHASE * PURCHASE_PRICE
purchaseCommission = COMMISSION_RATE_PURCHASE * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES_SOLD * SELLING_PRICE
sellingCommission = COMMISSION_RATE_SALE * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid


print("Amount paid for stock: $",f'{amountPaidForStock:,.2f}')
print("Commission paid on the purchase: $",f'{purchaseCommission:,.2f}')
print("Amount the stock sold for: $",f'{stockSoldFor:,.2f}')
print("Commission paid on the sale: $",f'{sellingCommission:,.2f}')
print("Profit (or lost if negative): $",f'{profitOrLoss:,.2f}')


