def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zer0'

for x in [-1,1,0]:
    print(sign(x))

# parameters as optional

def hello(name, loud=False):
    if loud:
        print('HELLO, %s!' % name.upper())
    else:
        print('Hello, %s' % name)

hello('Rakesh') # Prints "Hello, Rakesh"
hello('Shashank', loud=True)  # Prints "HELLO, SHASHANK!"