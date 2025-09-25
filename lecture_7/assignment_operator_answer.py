
from start_compiler.import_start import *



class grade(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg
try:
    local_vars['grades'] = start()
    local_vars['p'] = start()
    StartError.lineNumber = 7
    check_events()
    _set('p', local_vars, None)['p'] = number(10)
    StartError.lineNumber = 8
    check_events()
    _set('grades', local_vars, None)['grades'] = grade(_get('p', local_vars, None)['p'], _get('p', local_vars, None)['p'], _get('p', local_vars, None)['p'], _get('p', local_vars, None)['p'], _get('p', local_vars, None)['p']).clone()
    StartError.lineNumber = 11
    check_events()
    _print(_get('grades', local_vars, None)['grades'])
    StartError.lineNumber = 12
    check_events()
    number(42).copy(_set(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))])
    StartError.lineNumber = 13
    check_events()
    _print(_get('grades', local_vars, None)['grades'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
