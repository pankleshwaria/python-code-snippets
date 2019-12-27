from Decorators.exception_decorator import log_exception


@log_exception
def divide():
    return 1/0


if '__main__' == __name__:
    divide()

