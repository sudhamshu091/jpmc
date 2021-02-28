class Solution:
    def countBinarySubstrings(self, string):
        length = len(string)
        count, zero, one = 0, 0, 0
        zerocount, onecount = 0, 0
        while True:
            while zero < length and string[zero] == '0':
                zero += 1
            zerocount = zero - one
            count = count + min(zerocount, onecount)
            if zero == length:
                break
            onecount = 0
            one = zero
            while one < length and string[one] == '1':
                one = one + 1
            onecount = one - zero
            count = count + min(zerocount, onecount)
            if one == length:
                break
            zero = one
            zerocount = 0
        return count

s = Solution()
print(s.countBinarySubstrings("10110")) #3
