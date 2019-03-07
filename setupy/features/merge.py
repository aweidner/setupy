def merge(*dicts):
    r = {}
    for d in dicts:
        r.update(d)
    return r
