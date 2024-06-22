def pop_get(dicts,key,default=None):
    if dicts.get(key):
        key_ = dicts.pop(key)
    else:
        key_ = default
    return key_