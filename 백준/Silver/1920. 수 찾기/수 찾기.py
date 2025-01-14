n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
find_num = list(map(int, input().split()))


def find(num):
	right = len(nums) - 1
	left = 0

	while left <= right:
		mid = (left + right) // 2

		if nums[mid] <= num:
			left = mid + 1

		if nums[mid] >= num:
			right = mid - 1

		if nums[mid] == num:
			return 1
	return 0

for i in range(len(find_num)):
	print(find(find_num[i]))