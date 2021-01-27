def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zer0'

for x in [-1,1,0]:
    print(sign(x))