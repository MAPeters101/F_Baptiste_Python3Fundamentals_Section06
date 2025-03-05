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





