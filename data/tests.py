class a:
    v = 12
    b = 12
    c = 12
    def __init__(self,v = 121):
        ...
    def __set__(self, instance, value):
        a = value
    def __get__(self):
        return 12
class b(a):
    ...
# c = b()
# print(a.__dict__)
# print(a.v)
# print(c.__getattribute__('v'))



# ReadBuffer(ascii)
ascii_bytes = b"4d 65 6e 75"
ascii_string = ascii_bytes.decode()
field_from_ascii_string = bytearray.fromhex(ascii_string).decode()
print(f"ASCII: <{ascii_bytes}> ---> <{ascii_string}> ---> <{field_from_ascii_string}>")

# ReadBuffer(EBCDIC)
ebcdic_bytes = b"c0"
ebcdic_string = ebcdic_bytes.decode()
# https://en.wikipedia.org/wiki/Code_page#EBCDIC-based_code_pages
# IBM Code Page 1140 or IBM Code Page 500
field_from_ebcdic_string = ebcdic_bytes.decode('cp1141')  # or 'cp500'
print(f"EBCDIC: <{ebcdic_bytes}> ---> <{ebcdic_string}> ---> <{field_from_ebcdic_string}>")