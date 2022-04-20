def pri(num):
    a={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",
       6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",
       11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",
        16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"NineTeen",
       10:"Ten",20:"Twenty",30:"Thirty",40:"Fourty",50:"Fifty",
        60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninty"}
    
    while(num>0):
        if num>99999 and num<1000000:
            print(a[int(str(num)[:1])] +" Lakh"+" ",end="")
            num=num%100000
        elif num>=20000 and num<=99999:
            if int(str(num)[:2])%10==0:
                print(a[int(str(num)[:2])] +" Thousand"+" ",end="")
                num=num-(int(str(num)[:2]))*1000
            else:
                print(a[(int(str(num)[:1]))*10] +" "+a[int(str(num)[1:2])]+" Thousand"+" ",end="")
                num=num-(int(str(num)[:2]))*1000
        elif num>9999 and num<20000:
            print(a[int(str(num)[:2])] +" Thousand"+" ",end="")
            num=num-(int(str(num)[:2]))*1000
        elif num>999 and num<10000:
            print(a[int(str(num)[:1])] +" Thousand"+" ",end="")
            num=num%1000
            continue
        elif num>99 and num<1000:
            print(a[int(str(num)[:1])] +" Hundred"+" ",end="")
            num=num%100
            if num%100==0:
                print()
            continue
        elif num>10 and num<20:
            print(" "+a[num],end="")
            num=0
        elif num>=20 and num<100:
            print(a[int(str(num)[:1])*10],end="")
            if num%10==0:
                print()
            num=num-int(str(num)[:1])*10
        elif num<=10:
            print(" "+a[num],end="")
            num=0
            
        
a=input("enter a number")
a=a.split(".")
if len(a)==2:
    pri(int(a[0]))
    print(" ",end="point")
    print(" ")
    pri(int(a[1]))
else:
    pri(int(a[0]))
    
    
