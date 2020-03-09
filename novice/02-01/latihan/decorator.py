def retry(func):
    def retried_func(*args, **kwargs):
        exc = None
        for_in range(3):
            try:
                return func(*args,**kwargs)
            except Exception as exc:
                print("exception raised while calling %s with args:%s, kwargs: %s. Retrying" % (func, args, kwargs))
        raise exc
    return retried_func

    @retry
    def do_something_risky():

    retried_function = retry(do_something_risky