input()
nums = list(map(int, input().split()))
part = [n for n in nums[1:] if n <= nums[0]] + [nums[0]] + [n for n in nums[1:] if n > nums[0]]
print(' '.join(map(str, part)))
