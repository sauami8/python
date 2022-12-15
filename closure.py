def main_func(msg):
    message = msg

    def closure_func():
        print('Closure function access free variable value from outer func --> ', message)
    return closure_func()


main_func('Hello')

main_func(234)