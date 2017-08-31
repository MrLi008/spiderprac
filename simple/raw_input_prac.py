# coding=utf8
numbers = raw_input('input: ')


addresult = 0
for num in numbers.split():
    addresult += int(num)

print 'addresult: ', addresult