"""
You will be given a list of 32 bit unsigned integers. Flip all the bits (1〉 O and 0-> 1) and return the
result as an unsigned integer.
Example
m = 910
910= 10012. Were working with 32 bits, So:
000000000000000000000000000010012= 910
111111111111111111111111111101102= 429496728610
Return 4294967286.
Function Description
Complete the flippingBits function in the editor below.
flippingBits has the following parameter(S):
• int n: an integer
Returns
• int: the unsigned decimal integer result
Input Format
The first line of the input contains g, the number of queries.
Each of the next g lines contain an integer, n, to process.
Constraints
1≤g≤ 100
0≤n< 232
Sample input
3
2147483647
1
0
Sample Output
2147483648
4294967294
4294967295
Explanation
Take 1 for example, as unsigned 32-bits is 00000000000000000000000000000001 and doing the
flipping we get 11111111111111111111111111111110 which in turn is 4294967294.
"""


def flippingBits(n):
    # 1. n은 10진수
    # 2. n을 2진수로 변환
    # 3. n을 32비트로 변환하고 0을 1로 치환
    # 4. 다시 10진수로 변환

    n = int(n)
    n = bin(n)[2:]
    n = n.zfill(32)
    n = list(n)
    for idx, str in enumerate(n):
        if str == "0":
            n[idx] = "1"
        else:
            n[idx] = "0"
    n = "".join(n)
    n = int(n, 2)
    print(n)
    return n


flippingBits(5)
