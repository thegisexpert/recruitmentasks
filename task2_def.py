
# task 2. Letters from phone keuboards
# Aleksander Gonzalez


def letters_from_digits(numbers_param):
    numbers_param = numbers_param.replace("1", "a").replace("2", "b").replace("3", "c")

    numbers_param = numbers_param.replace("4", "d").replace("5", "e").replace("6", "f")
    numbers_param = numbers_param.replace("7", "g").replace("8", "h").replace("9", "i").replace("0", "j")

    letters =  numbers_param
    letters = [char for char in letters]

    #teclas =  'A, B'.split(',')

    #building the expresion to evaluate for the keyboards
    # #[+a+ b+c+ d  for a in A for  b in  B for c in C for  d in
    # this is the part one  a+ b+c+ d + ...
    indices = ""
    for i in letters:
        if (len(indices)==0):
            indices = i

        else:
            indices = indices + "+" + i



    #this is the part two for a in A for  b in  B for c in C for  d in

    value = [" for "+a+" in " +a.upper() + " " for a in letters]


    v= ""
    for i in value:
        v = v + i

    #building the expression to evaluate the keyboards
    # #[+a+ b+c+ d  for a in A for  b in  B for c in C for  d in
    expresion_core = "[" + indices + " " + v+ "]"

    return expresion_core

    #deifne the keyboards of the phone
list_str = "A=['']"
exec(list_str)

list_str = "B=['a','b','c']"
exec(list_str)

list_str = "C=['d','e','f']"
exec(list_str)

list_str = "D=['g','h','i']"
exec(list_str)

list_str = "E=['j','k','l']"
exec(list_str)

list_str = "F=['m','n','o']"
exec(list_str)

list_str = "G=['p','q','r','s' ]"
exec(list_str)

list_str = "H=['t','u','v']"
exec(list_str)

list_str = "I=['w','x','y','z' ]"
exec(list_str)

list_str = "J=['+']"
exec(list_str)

stringtovalue = input("Enter digits=   with your value: ")
print (stringtovalue)
stringtovalue = stringtovalue.replace(' ','').replace("digits", "").replace("=", "").replace("\"", "")
numbers_param = stringtovalue

try:
    #If Inserted others rhings than digits, not follow with procedure
    param =int(numbers_param)
    #expresion = expresion_core
    expresion_core=letters_from_digits(numbers_param)
    #evaluate the expression with keyboards
    resultado =eval(expresion_core)
    print(resultado)
    #print(" res")

    #print(string_int)
except ValueError:
    # Handle the exception
    print('Please check your input')
    resultado=0







