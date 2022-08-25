

def print_result(function):
    def new_func(*args):
        res = function(*args)
        print(res)
        return res
    return new_func
