
# -*- coding: utf-8 -*-
SPACE = " "
def expanded_string(stri):
    text = []
    #print (" expanded string\n")
    for l in stri:
        #print(l)
        text.append(l + SPACE)

    return text

"""
def expanded_n_spaces(stri, n):

    #print (" expanded string\n")
    n_spaces = SPACE*n
    stri.append(n_spaces)

    return stri
"""



def len_string_from_list(l):
    string = "".join(l)
    return len(string)

def expanded_text(lines):
    lin_ex=[]
    for lin in lines:


        lon=0
        str2= lin
        #print(str2)
        while (lon<maximum_width):
             str2= expanded_string(str2)
             lon =len_string_from_list(str2)
        lin_ex.append(str2)

        #add the missing spaces.
        #len_lin = len_string_from_list(lin_ex)
        #missing_spaces = maximum_width-len_lin
        #str2= expanded_n_spaces(str2, missing_spaces)

        #lin_ex.append(str2)
    return lin_ex

def justify_text(text,maximum_width):
    #text= "Hey there mate, it’s nice to finally meet you!"
    #text = "In a letter to the National Archives obtained by NBC News, White House Counsel Dana Remus rejected an attempt by Trump’s attorneys to withhold documents requested by the House Select Committee regarding the then-president’s activities on Jan. 6, writing that “President Biden has determined that an assertion of executive privilege is not in the best interests of the United States, and therefore is not justified as to any of the documents.”";

    words = text.split()
    len_linea =0
    linea = []
    lines =[]



    longitud=0
    for word in words:
        #print(word)
        longitud = longitud + len(word)

        if (longitud<=maximum_width):
            linea.append(word)

        else:

            #init of the following line
            lines.append(linea)
            linea = [word]
            longitud = len(word)



    lines.append(linea) #append last line
    """
    print("[")
    for t in lines:
        r = ' '.join(t+[""])
        print("\"" +r+"\",")
    print("]")
    """


    deftext =expanded_text(lines)
    return deftext

def print_text(deftext):

    r=""

    print("[")
    for t in deftext:
        r = ''.join(t)
        print("\"" +r+"\",")
    print("]")

text= "Hey there mate, it’s nice to finally meet you!"
text = "In a letter to the National Archives obtained by NBC News, White House Counsel Dana Remus rejected an attempt by Trump’s attorneys to withhold documents requested by the House Select Committee regarding the then-president’s activities on Jan. 6, writing that “President Biden has determined that an assertion of executive privilege is not in the best interests of the United States, and therefore is not justified as to any of the documents.”";0
maximum_width=50
print_text(justify_text(text, maximum_width))
