import struct


def hex_to_int(value):
    # by = b''.join(value)
    end = struct.unpack('<f', value)
    print(end)
