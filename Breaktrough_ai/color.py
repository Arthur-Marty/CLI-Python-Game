def red(arg):
    print('\x1b[31;1m' + str(arg)+ '\x1b[39;0m')

def green(arg):
    print('\x1b[32;1m' + str(arg)+ '\x1b[39;0m')

def yellow(arg):
    print('\x1b[33;1m' + str(arg)+ '\x1b[39;0m')

def navy(arg):
    print('\x1b[34;1m' + str(arg)+ '\x1b[39;0m')

def magenta(arg):
    print('\x1b[35;1m' + str(arg)+ '\x1b[39;0m')

def blue(arg):
    print('\x1b[36;1m' + str(arg)+ '\x1b[39;0m')

def gray(arg):
    print('\x1b[37;1m' + str(arg)+ '\x1b[39;0m')

def black(arg):
    print('\x1b[38;1m' + str(arg)+ '\x1b[39;0m')

def regular(arg):
    print('\x1b[39;1m' + str(arg)+ '\x1b[39;0m')

jaune = '\x1b[33;1m'
reg = '\x1b[39;0m'


def colors():
    red('red()')
    green('green()')
    yellow('yellow()')
    navy('navy()')
    magenta('magenta()')
    blue('blue()')
    gray('gray()')
    black('black()')
    regular('regular()')
