txt = 'mano batai buvo du, bet kaZkas atsitiko - nerandu'

print(len(txt))
print(txt[len(txt)-1])
print(txt[-1])
# kiek yra zodziu
kiekZodziu = txt.count(' ')+1
print(kiekZodziu)

print(txt.capitalize()) #sakinio stilius
print(txt.upper()) #sakinio stilius
print(txt.lower()) #sakinio stilius
print(txt.title()) #sakinio stilius

print(txt.islower())
print(txt.isupper())

print(txt.find('a'))
print(txt.find('a', 5, 15))
print(txt.find('ch', 5, 15))

t = ' 123  abc 456  , '
t1 = '123abc456'
t2 = '     '
t3 = ''
# print(t.isalnum())
# print(t1.isalnum()) # tikrina ar tiktais raides ir skaiciai nes jeigu simboliai duoda False.
# print(t1.isalpha()) #tikrina ar tiktais raides.
# print(t2.isspace()) # tikrina ar yra tarpu
# print(t3.isspace()) # tikrina ar yra tarpu
# t4 = t.strip(' ')
# print(t4)
t5 = 'Man patinka Coca cola'
print(t5.replace('Coca', 'Pepsi'))
print(t5.replace(' ', ''))
print(ord('a'))
print(chr(101))