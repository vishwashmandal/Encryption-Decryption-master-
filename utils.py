
def algo(key1,key2,text):
    # l=input("Enter First key ")
    # l="Group07IT"
    l=key1
    data=key2
    plaintxt=text
    arr=[]
    for e in l:
        arr.extend(list(str(bin(ord(e))[2:])))
    a1 = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
    a2= [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
    a3 = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
    a4 = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
    n=len(arr)
    i=0
    # data=input("Enter Secon key ")
    # data="UITbu@itG07"
    k=0
    while k<len(data): 
            array_final = arr[i%len(arr)]+arr[(i+1)%len(arr)]
            if array_final == '00':
                array_final = a1
            elif array_final == '01':
                array_final = a2
            elif array_final == '10':
                array_final = a3
            elif array_final == "11":
                array_final= a4

            row = (int(arr[(i+2)%n]+arr[(i+3)%n]+arr[(i+4)%n],2) - 1)%5
            col = (int (arr[(i+5)%n]+arr[(i+6)%n]+arr[(i+7)%n],2))%5
            # print((row,col))
            if array_final[row][col]!=-1:
                i = i+1
            else:
                array_final[row][col]= data[k]
                k+=1
                i=(i+8)%n
    # print(a1,a2,a3,a4)
    # data="chandkumr7396"
    asci=[x for x in range(32,128)]
    asci.extend([0,8,9,27])
    for e in set(data):
        asci.remove(ord(e))
    i=0
    while i<len(asci):
        for row in a1:
            for index,e in enumerate(row):
                if e ==-1:
                    row[index]=chr(asci[i])
                    i+=1
        for row in a2:
            for index,e in enumerate(row):
                if e ==-1:
                    row[index]=chr(asci[i])
                    i+=1
        for row in a3:
            for index,e in enumerate(row):
                if e ==-1:
                    row[index]=chr(asci[i])
                    i+=1
        for row in a4:
            for index,e in enumerate(row):
                if e ==-1:
                    row[index]=chr(asci[i])
                    i+=1
        else:
            i=len(asci)
    # print(a1)
    # print(a2)
    # print(a3)
    # print(a4)
    b1,b2,b3,b4=a1,a2,a3,a4
    cipher_arr=[]
    # plaintxt=input("Enter plain Text ")
    len_of_plaintext=len(plaintxt)
    z=0
    # print(len_of_plaintext%3,"asdf")
    if len_of_plaintext%3!=0:
        if len_of_plaintext%3 == 2:
            plaintxt+='0'
            z=1
        elif len_of_plaintext%3 == 1:
            plaintxt+='10'
            z=2


    # print(plaintxt)


    # plaintxt="Project Group07"
    for i in range(0,len(plaintxt),3):
        # print(plaintxt[i]+plaintxt[i+1]+plaintxt[i+2])
        for row in b1:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_row = b1.index(row)
                if e == plaintxt[i+1]:
                    final_col = index
                if e == plaintxt[i+2]:
                    final_mat = b1

        for row in b2:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_row = b2.index(row)
                if e == plaintxt[i+1]:
                    final_col = index
                if e == plaintxt[i+2]:
                    final_mat = b2

        for row in b3:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_row = b3.index(row)
                if e == plaintxt[i+1]:
                    final_col = index
                if e == plaintxt[i+2]:
                    final_mat = b3

        for row in b4:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_row = b4.index(row)
                if e == plaintxt[i+1]:
                    final_col = index
                if e == plaintxt[i+2]:
                    final_mat = b4
        cipher_arr.append(final_mat[final_row][final_col])
        for row in b1:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_mat = b1
                if e == plaintxt[i+1]:
                    final_row = b1.index(row)
                if e == plaintxt[i+2]:
                    final_col = index

        for row in b2:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_mat = b2
                if e == plaintxt[i+1]:
                    final_row = b2.index(row)
                if e == plaintxt[i+2]:
                    final_col = index

        for row in b3:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_mat = b3
                if e == plaintxt[i+1]:
                    final_row = b3.index(row)
                if e == plaintxt[i+2]:
                    final_col = index

        for row in b4:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_mat = b4
                if e == plaintxt[i+1]:
                    final_row = b4.index(row)
                if e == plaintxt[i+2]:
                    final_col = index
        cipher_arr.append(final_mat[final_row][final_col])
        for row in b1:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_col = index
                if e == plaintxt[i+1]:
                    final_mat = b1
                if e == plaintxt[i+2]:
                    final_row = b1.index(row)

        for row in b2:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_col = index
                if e == plaintxt[i+1]:
                    final_mat = b2
                if e == plaintxt[i+2]:
                    final_row = b2.index(row)

        for row in b3:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_col = index
                if e == plaintxt[i+1]:
                    final_mat = b3
                if e == plaintxt[i+2]:
                    final_row = b3.index(row)

        for row in b4:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_col = index
                if e == plaintxt[i+1]:
                    final_mat = b4
                if e == plaintxt[i+2]:
                    final_row = b4.index(row)
        cipher_arr.append(final_mat[final_row][final_col])            
    # print(cipher_arr)
    sunny=[]
    # arr = ['1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '1', '0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0', '1', '1', '0', '1', '0', '1', 
    # '0', '0']
    keys=cipher_arr
    # keys = ['n', 'V', 'o', 'e', 'g', 't', 'E', 'Q', ')', '%', 'o', 'y', 'q', 'w', 'G']
    i=0
    k=0
    from ast import literal_eval
    for index,e in enumerate(keys):
        decimal = ord(e)
        binary = str(bin(decimal))[2:]
        result = ''
        if len(binary)<7:
            no_of_zeros = 7-len(binary)
            for x in range(no_of_zeros):
                binary='0'+binary

        for e in binary:
            if e == '1':
                result+='0'
            else:
                result+='1'
        binary=result

        result = ''

        n=len(arr)
        for e in "".join(arr[i%n:(i+7)%n]):
            if e == '1':
                result+='0'
            else:
                result+='1'
        # print("".join(arr[i%n:(i+7)%n]))
        i=(i+1)%n

        ans = int(binary,2)+int(result,2)
        # sunny.append(chr(ans))

        if ans<31 or ans>127:
            # sunny.append("",hex(ans),end=" ")
            sunny.append(" ")
            sunny.append(hex(ans))
            sunny.append(" ")
        else:
            sunny.append(chr(ans))
    sunny.append(str(z))
    return ''.join(sunny)
    
    # print(sunny)
def decrypt(key1,key2,text):
    # l=input("Enter first key ")
    l=key1  # l="Group07IT"
    data=key2
    keys=text
    arr=[]
    for e in l:
        arr.extend(list(str(bin(ord(e))[2:])))
    a1 = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
    a2= [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]

    a3 = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]

    a4 = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]

    n=len(arr)
    i=0
    # data=input("Enter Second key ")
    # data="UITbu@itG07"
    k=0
    while k<len(data):
    
            array_final = arr[i%len(arr)]+arr[(i+1)%len(arr)]
            if array_final == '00':
                array_final = a1
            elif array_final == '01':
                array_final = a2
            elif array_final == '10':
                array_final = a3
            elif array_final == "11":
                array_final= a4

            row = (int(arr[(i+2)%n]+arr[(i+3)%n]+arr[(i+4)%n],2) - 1)%5
            col = (int (arr[(i+5)%n]+arr[(i+6)%n]+arr[(i+7)%n],2))%5
            # print((row,col))

            if array_final[row][col]!=-1:
                i = i+1

            else:
                array_final[row][col]= data[k]
                k+=1
                i=(i+8)%n

    # print(a1,a2,a3,a4)

    asci=[x for x in range(32,128)]
    asci.extend([0,8,9,27])
    for e in set(data):
        asci.remove(ord(e))

    i=0
    while i<len(asci):
        for row in a1:
            for index,e in enumerate(row):
                if e ==-1:
                    row[index]=chr(asci[i])
                    i+=1
        for row in a2:
            for index,e in enumerate(row):
                if e ==-1:
                    row[index]=chr(asci[i])
                    i+=1
        for row in a3:
            for index,e in enumerate(row):
                if e ==-1:
                    row[index]=chr(asci[i])
                    i+=1
        for row in a4:
            for index,e in enumerate(row):
                if e ==-1:
                    row[index]=chr(asci[i])
                    i+=1
        else:
            i=len(asci)

    b1,b2,b3,b4=a1,a2,a3,a4
    cipher_arr=[]

    # keys=input("Enter Encrypt text")
    z= keys[-1]
    keys=keys[:len(keys)-1]

    length_of_keys=len(keys)
    temp=[]

    i=0

    while i<length_of_keys:
        try:
            # if keys[i]==" " and i == length_of_keys-1:
            #     temp.append(keys[i])
            #     i+=1
            #     break
            if keys[i]==" " and keys[i+1]=='0' and keys[i+2] == 'x':
                i+=1
                continue
            # elif not (keys[i]=='0' and keys[i+1]=='x'):
            #     temp.append(keys[i])
            #     i+=1
            elif keys[i]=='0' and keys[i+1]=='x':
                s=''
                while keys[i]!=" ":
                    s+=keys[i]
                    i+=1
                else:
                    i+=1
                temp.append(s)
            else:

                temp.append(keys[i])
                i+=1
    
        except:
            temp.append(keys[i])
            i+=1

    for i,e in enumerate(temp):
        if e.startswith("0x"):
            temp[i]=int(e,16)
        else:
            temp[i] = ord(e)
    n= len(arr)
    i=0
    result_arr=[]
    i=0
    for j,e in enumerate(temp):

        result=''
        for ele in "".join(arr[i%n:(i+7)%n]):
            # print("".join(arr[i%n:(i+7)%n]))
            if ele == '1':
                result+='0'
            else:
                result+='1'
        decimal_result = int(result,2)
        kucho = abs(decimal_result-int(e))
        binary_kucho = str(bin(kucho)[2:])
        if len(binary_kucho)<7:
            no_of_zeros = 7-len(binary_kucho)
            for x in range(no_of_zeros):
                binary_kucho='0'+binary_kucho
        rakh_lo = ""
        for element in binary_kucho:
            if element == '1':
                rakh_lo+='0'
            else:
                rakh_lo+='1'
        result_arr.append(chr(int(rakh_lo,2)))
        i=(i+1)%n
    plaintxt=result_arr
    for i in range(0,len(plaintxt),3):
        for row in b1:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_row = b1.index(row)
                if e == plaintxt[i+1]:
                    final_mat = b1
                if e == plaintxt[i+2]:
                    final_col = index

        for row in b2:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_row = b2.index(row)
                if e == plaintxt[i+1]:
                    final_mat = b2
                if e == plaintxt[i+2]:
                    final_col = index

        for row in b3:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_row = b3.index(row)
                if e == plaintxt[i+1]:
                    final_mat = b3
                if e == plaintxt[i+2]:
                    final_col = index

        for row in b4:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_row = b4.index(row)
                if e == plaintxt[i+1]:
                    final_mat = b4
                if e == plaintxt[i+2]:
                    final_col = index
        cipher_arr.append(final_mat[final_row][final_col])
        for row in b1:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_col = index
                if e == plaintxt[i+1]:
                    final_row = b1.index(row)
                if e == plaintxt[i+2]:
                    final_mat = b1

        for row in b2:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_col = index
                if e == plaintxt[i+1]:
                    final_row = b2.index(row)
                if e == plaintxt[i+2]:
                    final_mat = b2

        for row in b3:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_col = index
                if e == plaintxt[i+1]:
                    final_row = b3.index(row)
                if e == plaintxt[i+2]:
                    final_mat = b3

        for row in b4:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_col = index
                if e == plaintxt[i+1]:
                    final_row = b4.index(row)
                if e == plaintxt[i+2]:
                    final_mat = b4
        cipher_arr.append(final_mat[final_row][final_col])
        for row in b1:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_mat = b1
                if e == plaintxt[i+1]:
                    final_col = index
                if e == plaintxt[i+2]:
                    final_row = b1.index(row)

        for row in b2:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_mat = b2
                if e == plaintxt[i+1]:
                    final_col = index
                if e == plaintxt[i+2]:
                    final_row = b2.index(row)

        for row in b3:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_mat = b3
                if e == plaintxt[i+1]:
                    final_col = index
                if e == plaintxt[i+2]:
                    final_row = b3.index(row)

        for row in b4:
            for index,e in enumerate(row):
                if e == plaintxt[i]:
                    final_mat = b4
                if e == plaintxt[i+1]:
                    final_col = index
                if e == plaintxt[i+2]:
                    final_row = b4.index(row)
        cipher_arr.append(final_mat[final_row][final_col])


    if any([z=="1"]):
        cipher_arr.pop()
    elif z=="2":
        cipher_arr.pop()
        cipher_arr.pop()

    return "".join(cipher_arr)






    

