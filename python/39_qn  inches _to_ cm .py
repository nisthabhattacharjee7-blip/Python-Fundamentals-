def inches_to_cms(w):
    return (w)* 2.54
w = int(input("Enter value in inches: "))
t = inches_to_cms(w)
print(f"{round(t,2)} cm")