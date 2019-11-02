class Solution():
    def findWays(expr):
        nums, ops = [], []
        num = 0
        for c in expr:
            if '0'<= c <='9':
                num = num * 10 + ord(c) - 48
            else:
                ops.append(c)
                nums.append(num)
                num = 0
        else:
            nums.append(num)

    def calc(nums, ops):
        if not ops:
            return [nums[0]]
        if len(ops) == 1:
            if ops[0] == '+':
                return [nums[0] + nums[1]]
            if ops[0] == '-':
                return [nums[0] - nums[1]]
            else:
                return [nums[0] * nums[1]]
        res = []
        for i in range(len(ops)):
            for num1 in calc(nums[:i + 1], ops[:i]):
                for num2 in calc(nums[i + 1:],ops[i + 1:]):
                    res.append(calc([num1,num2],[ops[i]])[0])
        return res

    return calc(nums, ops)

expr = input()
s = Solution
a = (list(set(s.findWays(expr))))
a.sort()
print(",".join(str(i) for i in a))