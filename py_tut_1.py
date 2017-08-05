# def fib2(n):
#     result=[]
#     a,b=0,1
#     while a < n:
#         result.append(a)
#         a,b=b,b+a
#     return result
# f100=fib2(18)

# print f100

# Default Argument Values
# ------------------------------

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

# Keyword Arguments
#---------------------------

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

#Arbitrary Argument Lists
#--------------------------------------

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> d173df64ab4c81dedbf1b38a811642f6f48f48eb
print '-' * 69

# Unpacking Argument Lists
#-----------------------------


def parrot(voltage, state='a stiff', action='voom'):
    print "-- This parrot wouldn't", action ,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOOM"}
parrot(**d)


print '-' *69

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)


print f(0)
print f(11)


print '-' *69

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair:pair[1])
print pairs



print '-' *69


<<<<<<< HEAD
>>>>>>> d173df64ab4c81dedbf1b38a811642f6f48f48eb
=======
>>>>>>> d173df64ab4c81dedbf1b38a811642f6f48f48eb


