text = 'Labai daug teksto ir "kabuciu" va'
kelias = 'c:\\doc\\data.txt'
print(kelias)
print('----------')


kelias1 = r'c:\doc\data.txt'
print(kelias1)
print('----------')


#\n
#\t
t = 'Labas rytas'
print(t[1])
# t[0] = '1'
print(t[3:])
print(t[3:8])
print(t[::3])

t1 = 'Labai '
t2 = 'noriu '
t3 = 'namo'
t4 = t1*3 + '' + t2 + t3
print(t4)

print('%s tara ta ta ta %s %s' % (t1, t2, t3))
print('{}{}{}'.format(t2, t2, t3))

print(2+'3')