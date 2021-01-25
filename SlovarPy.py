def checkspis(f):
    fail=open(f,'r',encoding='utf-8-sig')
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

rus=checkspis('rus.txt')
eng=checkspis('eng.txt')
print(rus)
print(eng)

def addword(f, text):
 fail=open(f, 'a', encoding="utf-8-sig")
 fail.write(text+'\n')
 fail.close()
 mas=[]
 mas=checkspis(f)
 return mas

def trans():
 pass

while True:
 try:
     print('1)С eng на rus')
     print('2)С rus на eng')
     print('3)Добавить новое слово')
     ch=input('Выберете вариант: ')
     if ch == '3':
      russ = input('Введи слово на rus: ')
      engs = input('Введи слово на eng: ')
      rus = addword('rus.txt', russ)
      eng = addword('eng.txt', engs)
 except:
  TypeError
