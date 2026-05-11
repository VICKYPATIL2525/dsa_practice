# Count frequency of each character in a string

userinput = "tgatggggaassaatbs"
unique_values = set(userinput)
print(unique_values)

for i in unique_values:
    tmp = i
    varcnt = 0
    for j in userinput:
       
       if j== tmp:
           varcnt +=1
    print(tmp, "=", varcnt)
   
    

        
    