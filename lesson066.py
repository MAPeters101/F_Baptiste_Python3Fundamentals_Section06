open_, high, low, close = 98, 100, 95, 99

msg1 = 'open: ' + str(open_) + ', high: ' + str(high) + ', low: ' + str(low) + ', close: ' + str(close)
print(msg1)

msg2 = 'open: {}, high: {}, low: {}, close: {}'.format(open_, high, low, close)
print(msg2)

#msg3 = 'open: {}, high: {}, low: {}, close: {}'.format(open_, high, low)
#print(msg3)

msg4 = 'open: {}, high: {}, low: {}, close: {}'.format(open_, high, low, close, 100)
print(msg4)
print('-'*80)

bid = 1.5760
ask = 1.5763
msg5 = 'bid: {}, ask: {}, spread: {}'.format(bid, ask, ask-bid)
print(msg5)

msg6 = f'bid: {bid}, ask: {ask}, spread: {ask-bid}'
print(msg6)
print()

msg7 = 'bid: {b}, ask: {a}, spread: {spread}'.format(a=ask, spread=ask-bid, b=bid)
print(msg7)
print()

print(format(0.1, '.10f'))
print('-'*80)

msg8 = 'bid: {:.4f}, ask: {:.4f}, spread: {:.4f}'.format(bid, ask, ask-bid)
print(msg8)

msg9 = f'bid: {bid:.4f}, ask: {ask:.4f}, spread: {(ask-bid):.4f}'
print(msg9)

msg10 = 'bid: {b:.4f}, ask: {a:.4f}, spread: {spread:.4f}'.format(a=ask, spread=ask-bid, b=bid)
print(msg10)
print()




