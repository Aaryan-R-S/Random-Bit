# 1.
# just select last bit of num
# E.g. 1001 gives 1
# to obtain next num right shift num and leftmost bit will be XOR of last two digit of original num
# 1001  ->  1
# 1100  ->  0
# 0110  ->  0
# 1011  ->  1
# 0101  ->  1
# and so on
# with n bits you can have the random numbers to repeat after (2^n)-1 numbers at max
# for 4 bits above example was best

# 2.
# Improvement - XOR one more time with leftmost digit of original num
# 1101
# 0110
# 1011
# 1101

state = 0b1001
for i in range(20):
    print(f"{state&1}", end="")
    newBit = (state^(state>>1)) & 1             # xor of 0 and 1st bit
    state = (state>>1) | (newBit<<3)            # set the new bit at leftmost place

print("\n")

state = (1<<127) | 1
for i in range(10000):
    print(f"{state&1}", end="")
    newBit = (state^(state>>1)^(state>>2)^(state>>7)) & 1    # xor of 0, 1, 2 & 7th bit
    state = (state>>1) | (newBit<<127)                       # set the new bit at leftmost place