o = int(input("Enter 1 To Convert USD To INR or 2 To Convert INR To USD : "))

if o == 1:
    a = int(input("Enter The Amount In USD To Convert : "))
    b = a * 80
    print(a," USD Converted Into INR is ",b)
elif o == 2:
    a = int(input("Enter The Amount In INR To Convert : "))
    b = a / 80
    print(a," INR Converted Into USD is ",b)
else:
    print("Enter 1 or 2")