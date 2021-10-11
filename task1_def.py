def inverted(nro):

    negative =False
    if (nro<0):
       nro = nro*-1
       negative =True
    inverted =0


    while round(nro)>1:
        lastdigit = nro%10;
        inverted = (inverted*10)+ lastdigit
        nro = nro//10;

    if (negative):
        inverted = inverted*-1

    return inverted

print("inverted ");

numbers_param = input("Enter the number to be inverted, x=    ")
numbers_param = numbers_param.replace("x", "").replace("X", "").replace("=", "")

#isnegative = numbers_param.find("-")
#numbers_param = numbers_param.replace("-", "")



try:
    param =int(numbers_param)
    resultado = inverted(param)
    #print(string_int)
except ValueError:
    # Handle the exception
    print('Please check your input')
    resultado=0



print(resultado)
#print(inverted(432456778));