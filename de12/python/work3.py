import prompt_toolkit
from zmq import Again


name=input("名前を教えて")
waist=int(input("腹囲は？") )
age=int(input("年齢は？"))
print(name,"さんは胸囲",waist,"cmで年齢は",age,"才ですね")
if age>40:
    print("年齢は40歳以上である")
else:
    print("40歳未満である")