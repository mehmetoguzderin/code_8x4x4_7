def from_7_to_8x4x4(a):
    b = [a & 0b001111111 for _ in range(3)]
    b = [i >> j for i, j in zip(b, [0, 1, 2])]
    b = [i               & 0b001001001 for i in b]
    b = [(i ^ (i >> 2))  & 0b000010011 for i in b]
    b = [(i ^ (i >> 2))  & 0b000000111 for i in b]
    return b
def from_8x4x4_to_7(a): # NONE = 0b10000000 = 255
    b = [i               & 0b000000111 for i in a]
    b = [(i | (i << 2))  & 0b000011001 for i in b]
    b = [(i | (i << 2))  & 0b001001001 for i in b]
    b = [i << j for i, j in zip(b, [0, 1, 2])]
    return (b[0] | b[1] | b[2]) & 0b001111111
for i in range(128):
    if from_8x4x4_to_7(from_7_to_8x4x4(i)) != i:
        print(f'{i} is broken, decode: {from_7_to_8x4x4(i)}, encode: {from_8x4x4_to_7(from_7_to_8x4x4(i))}')
for i in range(128):
    print(f'{i}: {from_7_to_8x4x4(i)}')
    
