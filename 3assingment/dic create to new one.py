# Write a Python script to concatenate following dictionaries to create a new one.




d1 = {"divya ": 10, "yuvraj": 20}
d2 = {"tops": 30, "tecnology": 40}
d3 = {1.2: 50, 6: 60}

d4 = {}

for i in (d1, d2, d3):
     d4.update(i)
print(d4) 
