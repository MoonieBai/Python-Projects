#Create a small python project where the dictionary keys are names of rooms 
# and values are temperatures. + write a loop that prints only rooms hotter than 25c

my_dict = {
"Marabella":25,
"Bangalore":30,
"Sydney":40,
"Shanghai":50,
"Seoul":28,
"BangKok":35
}
val = 25

for key, value in my_dict.items():
    if val < value:
        print("Value: ", value)
        



  