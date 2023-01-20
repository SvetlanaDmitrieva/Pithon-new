#05-03.Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах
string01 = ""
string02 = ""
f01 = open(r"file-05-03.txt","r", encoding = "utf-8")
data = f01.read()
f01.close()
print(data)
# сжатие данных
string01 = data[0]
count = 0
for item in data: 
    if item == string01:
        count += 1
        item2 = item
    else:
        string01 = item
        string02 += str(count)+ item2
        item2 = item
        count = 1
else:
    string02 += str(count)+ item2
print(string02)
#запись сжатых данных в файл 
with open('file-05-03-arh.txt','w') as f01:
    f01.write(string02)
f01.close()
#декодировка (восстановление) данных
f01 = open('file-05-03-arh.txt', 'r')
f02 = open('file-05-03-decode.txt', 'w')
while True:
    data = f01.readline()
    count = ""
    newStr = ""
    if not data:
        break
    else:
        for str01 in data :
            if str01.isdigit():
                count += str01
            else:
                newStr = newStr + str01*int(count)
                count = ""
        print(newStr,end = "")       
        f02.write(newStr)
f01.close()
f02.close()
