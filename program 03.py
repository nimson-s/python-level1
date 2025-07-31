print("GOVERMENT OF TAMIL NADU")
print("Electricity Borad")
print("-----------------")
no1=input("Enter the EB.NO")
no2=input("Enter the customer name")
no3=int(input("Reading for provious month:"))
no4=int(input("Reading for corrent month:"))
Total=no4-no3
print("Total unit consumed:",Total)
paid=Total*5
print("Amount to be paid Rs.",paid)
