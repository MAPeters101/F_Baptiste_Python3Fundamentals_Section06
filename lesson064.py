message = "The definitive guide to Python"
print(message.upper())
print(message.lower())
print(message)
print(message.title())
print()

print('abc' == 'ABC')
print('abc'.lower() == 'ABC'.lower())
print()


l = '\u03b1'
u = '\u0391'
print(l, u)
print(l == u)
print(l.lower() == u.lower())
print()

a = '🐍'
print(a.lower() == a.upper())
print('-'*80)

print(l.casefold() == u.casefold())
print(l.casefold(), u.casefold())
print()

street = 'stra\N{LATIN SMALL LETTER SHARP S}e'
print(street)
print(street.upper())
print(len(street), len(street.upper()))

data = 'STRASSE'
print(data == street)
print(data.lower() == street.lower())
print(data.lower())
print(data.casefold() == street.casefold())
print('-'*80)

s1 = 'ê'
s2 = 'ê'
print(s1 == s2)

s1 = '\N{LATIN SMALL LETTER E WITH CIRCUMFLEX}'
print(s1)
s2 = '\N{LATIN SMALL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'
print(s2)
print(s1 == s2)
print(s1.upper() == s2.upper())
print(s1.casefold() == s2.casefold())
print('-'*80)

name = 'Peter '
print(name.rstrip(' '))

name = '\t Peter\tJones\t'
print(name)
print(name.strip())
s = 'ababPYTHONabab'
print(s.strip('ab'))

s = 'ababcababPYTHONabab'
print(s.strip('ab'))
print('='*80)

print('Python' + ' ' + 'rocks' + '!')

data = 'Jones,Peter'
split_data = data.split(',')
print(split_data)

data = 'Jones,Peter,100'
split_data = data.split(',')
print(split_data)

data = 'Jones,Peter'
split_data = data.split(',')
last_name, first_name = data.split(',')
print(last_name)
print(first_name)
print('-'*80)

data = ['item 1', 'item 2', 'item 3']
print(', '.join(data))
print(','.join('ABCD'))
print('='*80)

print('rock' in 'python rocks!')
print('Rock' in 'python rocks!')
print('Rock'.casefold() in 'python rocks!'.casefold())
print( 1 in [1, 2, 3])
print( 'abc' in ('abc', 'def'))
print('-'*80)

print('Python rocks'.startswith('Python'))
print('Python rocks'.endswith('rocks'))
print('Python rocks'.casefold().endswith('Rocks'.casefold()))
print('-'*80)

message = 'To every action there is a always an equal and opposite reaction.'
print(message.index('every'))
#print(message.index('Newton'))
print()

print(message.find('every'))
print(message.find('Newton'))
print()

print([1, 2, 3, 4].index(2))
print(2 in [1,2,3,4])
#print([1, 2, 3, 4].find(2))
print('='*80)

print(message.index('action'))
#print(?str.index)
print(message.index('action', 9+len('action')))
print(message.index('action', 11))

