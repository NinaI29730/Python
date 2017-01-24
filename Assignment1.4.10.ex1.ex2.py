print("""Davy's auto shop services\n
1.Oil change -- $35
2.Tire rotation -- $19
3.Car wash -- $7
4.Car wax -- $19
""")
selection1= input("Select fist service:")
selection1 = int(selection1)
        
if   selection1 == 1: 
      print("Oil change -- $35")
elif selection1 == 2: 
      print("Tire rotation -- $19")
elif selection1 == 3:
      print("Car wash -- $7") 
elif selection1 == 4: 
      print("Car wax -- $19")
else: 
      print("Unknown Option Selected!") 

selection2= input("Select second service:")
selection2 = int(selection2)
          
if selection2 == 1: 
      print("Oil change -- $35")
elif selection2 == 2: 
      print("Tire rotation -- $19")
elif selection2 == 3:
      print("Car wash -- $7") 
elif selection2 == 4: 
      print("Car wax -- $19")
else: 
      print("Unknown Option Selected!") 
