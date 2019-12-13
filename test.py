k = 4
asc = ord('x')

print(asc)

print(chr(96 + ((asc + k) - 122) ))
print(chr(asc + k))

if asc + k > 122:
    # print(asc + k)
    # print(96 + ((asc + k) - 122) )
    print(chr(96 + asc + k - 122 ))
else:
    print(chr(asc + k))