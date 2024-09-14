def get_maxm():
    celsius=[10,13.5,12.3,19]   #the lists always contain string.
    val_celsius= [float(i) for i in celsius]  #converting string to values using list comprehension.
    maximum=max(val_celsius)
    return maximum

fahrenheit= get_maxm() *1.8 +32
print(fahrenheit)
