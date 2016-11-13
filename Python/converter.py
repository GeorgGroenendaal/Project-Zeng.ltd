import struct


def hex_to_int(value):
    newdata = value[2:-1]
    int_val = struct.unpack_from('<f', newdata, 0)[0]
    return int_val
