
def save_data(string_in:str):
    global list_str
    string_in = string_in.replace(' ','' ).replace('-',' - ' ).replace('+',' + ' ).replace('*',' * ' )\
            .replace('/',' / ' )
    if string_in.startswith(' - '):
        string_in = '-' + string_in[3:]
    list_str = string_in.split()
    while len(list_str) > 1:
        calculate('*','/')
        calculate('+','-')
    return list_str


def calculate(oper_01, oper_02):
    global list_str
    operation = {'+':lambda x,y: x + y,\
                 '-':lambda x,y: x - y,\
                 '*':lambda x,y: x * y,\
                 '/':lambda x,y: x / y,}
    i = 0
    while oper_01 in list_str or oper_02 in list_str :
        if list_str[i] in [oper_01,oper_02]:
            list_str[i-1] = operation.get(list_str[i])(float(list_str[i-1]),float(list_str[i+1]))
            list_str.pop(i)
            list_str.pop(i)
            i = 0
        else:
            i += 1
    return 






    