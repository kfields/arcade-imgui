_obj = None

def start_drag(obj):
    global _obj
    _obj = obj

def end_drag():
    global _obj
    obj = _obj
    _obj = None
    return obj