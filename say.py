import datetime
text = 'hello mister John!'

n = 'hello'
print(datetime.datetime.now().time().strftime(("%H:%M")))
print(datetime.date.today().strftime("%B %d, %Y"))

if n in text:
    print('Yes')
else:
    print('')