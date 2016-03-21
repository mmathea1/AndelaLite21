import random
n = random.randrange(500)
print n

if n % 3.0 == 0:
	print 'fizz'

if n % 5.0 == 0:
	print 'buzz'
"""why is it that elif doesn't display buzz 
if a number is divisible by 3 and 5? 
"""
if n % 5.0 == 0 and n % 3.0 == 0:
	print 'fizzbuzz'

else:
	print n
