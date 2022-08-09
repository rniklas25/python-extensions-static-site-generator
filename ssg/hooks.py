_callbacks = {}

def register(hook, order=0):
    def register_callback(func):
        _callbacks.setdefault(hook, {}).setdefault(order, []).append()
        return func

    return register_callback
