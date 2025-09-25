
from start_compiler.import_start import *



class savings(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

class client(start):
    def __init__(self, *args):
        self.name = args[0] if len(args) > 0 else start()
        self.savings = args[1] if len(args) > 1 else start()
        self.total_savings = args[2] if len(args) > 2 else start()
try:
    local_vars['bank_account'] = start()
    StartError.lineNumber = 11
    check_events()
    _set('bank_account', local_vars, None)['bank_account'] = client(text("Diana"), savings(number(100), number(30), number(24))).clone()
    StartError.lineNumber = 12
    check_events()
    _set(to_key(text('total_savings')), local_vars, _get('bank_account', local_vars, None)['bank_account'])[to_key(text('total_savings'))] = _add(_add(_get(to_key(number(0)), local_vars, _get(to_key(text('savings')), local_vars, _get('bank_account', local_vars, None)['bank_account'])[to_key(text('savings'))])[to_key(number(0))], _get(to_key(number(1)), local_vars, _get(to_key(text('savings')), local_vars, _get('bank_account', local_vars, None)['bank_account'])[to_key(text('savings'))])[to_key(number(1))]), _get(to_key(number(2)), local_vars, _get(to_key(text('savings')), local_vars, _get('bank_account', local_vars, None)['bank_account'])[to_key(text('savings'))])[to_key(number(2))]).clone()
    StartError.lineNumber = 14
    check_events()
    _print(text("My back account details :"), _get('bank_account', local_vars, None)['bank_account'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
