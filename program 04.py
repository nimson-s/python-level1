print("NIMSON SUPERMARKET")
print("NO.33 gandhi nagar")
print("------------------")
print("Bill Recpit")
print("-----------")
str1=input("Enter the serial number:")
str2=input("Enter the particulars:")
rate=int(input("Ente the rate:"))
quantity=int(input("Enter the quantity:"))
total=rate*quantity
print("total amount Rs:",total)
GST=total*10/100
print("GST(10%):",GST)
paid=total+GST
print("amount to be paid Rs:",paid)                   
