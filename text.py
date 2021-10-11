


def expanded_string(stri):
    result = ""
    for l in stri:
        result = result+ l + "*"

    return result

def len_string_from_list(l):
    string = "".join(l)
    return len(string)

text= "Hey there mate, it’s nice to finally meet you!"
text = "In a letter to the National Archives obtained by NBC News, White House Counsel Dana Remus rejected an attempt by Trump’s attorneys to withhold documents requested by the House Select Committee regarding the then-president’s activities on Jan. 6, writing that “President Biden has determined that an assertion of executive privilege is not in the best interests of the United States, and therefore is not justified as to any of the documents.”";

words = text.split()
len_linea =0
len_margen=16
linea = []
lines =[]
SPACE = " "


longitud=0
for word in words:
    #print(word)
    longitud = longitud + len(word)

    if (longitud<=len_margen):
        linea.append(word)



    else:

        #init of the following line
        lines.append(linea)
        linea = [word]
        longitud = len(word)



lines.append(linea) #append last line

print(lines)
def expanded_text(lines):
    lin_ex=[]
    for lin in lines:


        lon=0
        str2= lin
        while (lon<20):
             str2= expanded_string(str2)
             lon =len_string_from_list(str2)
        lin_ex.append(str2)
    return lin_ex


print(expanded_text(lines))




#print_lines(get_updated_lines(lineas, len_margen))