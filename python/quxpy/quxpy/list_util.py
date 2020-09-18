
def flatten(target_list):
    flat_list = []
    buf = [target_list]

    while 0 < len(buf):
        elm = buf.pop(0)

        if type(elm) is tuple:
            elm = list(elm)

        if type(elm) is list:
            buf = elm + buf
        else:
            flat_list.append(elm)

    return flat_list
