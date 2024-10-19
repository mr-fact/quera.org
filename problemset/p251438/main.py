import time
from functools import wraps
#
# def print_list(inputs):
#     print(30*'-')
#     for i in inputs:
#         print(i)
#
# def print_dict(inputs):
#     print(30*'-')
#     for i in inputs:
#         print(i, ':', inputs[i])

def conditional_cache(expiry, condition, max_size=5):
    keys = []
    cache = {}
    lock = True

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal lock
            if not condition(*args, **kwargs):
                return None
            key = hash(f"{args}{kwargs}")

            while not lock:
                time.sleep(0.01)
            lock = False
            current_time = time.time()
            if key in cache:
                result, timestamp = cache[key]
                keys.pop(keys.index(key))
                keys.append(key)
                if current_time - timestamp < expiry:
                    lock = True
                    return result

            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            keys.append(key)
            if len(keys) > max_size:
                last_key = keys.pop(0)
                del cache[last_key]
            lock = True
            # print('key')
            # print_list(keys)
            # print('cache')
            # print_dict(cache)
            return result

        return wrapper
    return decorator
