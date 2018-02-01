#! python3

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        sumval = a
        carry = b
        while(carry) :
            tmp = sumval
            sumval = tmp ^ carry
            carry = (tmp & carry) << 1
        return sumval

def main():
    solution = Solution()
    print(solution.aplusb(6,5))

if __name__ == '__main__':
    main()