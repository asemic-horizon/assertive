# Copyright (c) 2022, xheimlich/asemic-horizon/Diego Navarro

import traceback

VERBOSE = True
test_registry = dict()
traceback_log = dict()


def print_function(func, *args):
    if VERBOSE:
        print(func.__name__, func.__doc__, *args)
    return


def print_traceback_log():
    for failed_func, traceback in traceback_log.items():
        print(len(failed_func.__name__) * "-")
        print_function(failed_func)
        print(traceback)

def assertive(func):
    global test_registry
    global traceback_log

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print_function(func, "OK")
            return True
        except Exception:
            traceback_log[func] = traceback.format_exc()
            print_function(func, "FAILED")
            return False

    test_registry[func.__name__] = wrapper
    wrapper.__doc__ = func.__doc__ if func.__doc__ is not None else ""
    return wrapper


def run_tests():
    test_results = {name: None for name in test_registry}
    for name in test_results:
        test_results[name] = test_registry[name]()
    return test_results
