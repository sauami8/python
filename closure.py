def main_func(msg):
    message = msg

    def closure_func():
        print('Closure function access free variable value from outer func --> ', message)
    return closure_func()


main_func('Hello')

main_func(234)

def h(m):
    mymsg = m
    print('message is: ', mymsg)


h1 = h('morning')
h2 = h('evening')

h1
h2