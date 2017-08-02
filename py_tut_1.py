def fib2(n):
    result=[]
    a,b=0,1
    while a < n:
        result.append(a)
        a,b=b,b+a
    return result
f100=fib2(18)

print f100


# def ask_ok(prompt, retries =4, complaint ='Yes or No, dude!'):
#     while True:
#         ok = raw_input(prompt)
#         if ok in ('y','ye','yes'):
#             return True
#         if ok in ('n','no','nop','nope'):
#             return False
#         retires = retries -1
#         if retries < 0:
#             raise IOError ('refusenik user')
#         print complaint
# ask_ok('Do you really want to quit?')

# ask_ok('OK to overwrite the file?',2)

# ask_ok('OK to overwrite the file',2,'Come on, only yes or no!')


def parrot(voltage, state='a stiff',action='voom',type='Norwegian Blue'):
    print "--This parrot wouldn't",action,
    print "if you put", voltage, "volts throught it."
    print "--Lovely plumage, the",type
    print "--It's",state,"!"


# parrot (1000)
# # print ''
# print '### 1 positional argument ###'
# # print ''
# parrot (voltage=1000)
# # print ''
# print '# 1 keyword argument'
# # print ''
# parrot (voltage=1000000,action='VOOOOOM')
# # print ''
# print '### 2 keyword arguments ###'
# # print ''
# parrot (action='VOOOOOOOM',voltage=2000000)
# # print ''
# print '### 2 keyword arguments ###'
# # print ''
# parrot ('a million','bereft of life','jump')
# # print ''
# print '### 3 positional arguments ###'
# # print ''
# parrot ('a thousand',state='pushing up the daisies')
# # print ''
# print '### 1 positional, 1 keyword ###'

def cheeseshop(kind, *arguments, **keywords):
    print "--Do you have any",kind,"?"
    print "--I'm sorry, we're all out of",kind,"."
    for arg in arguments:
        print arg
    print "-" * 69
    keys = sorted (keywords.keys())
    for kw in keys:
        print kw, ":",keywords[kw]
cheeseshop("Limburger","It's very runny, sir.",
        "It's really very, VERY runny, sir.",
        shopkeeper='Michael Palin',
        client="John Clease",
        sketch="Cheese Shop Sketch")

 asdf
