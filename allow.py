class allow(object):
    def __init__(self, *exception_types):
        self.suppressed_exceptions = set(exception_types)

    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_type is None:
            return True

        return exception_type in self.suppressed_exceptions
