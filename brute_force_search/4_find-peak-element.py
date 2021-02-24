# a = nums[i], b = nums[i+1]이라고 하면
# if a < b이면 b 저장해두고
# if a >= b이면
# if b != 0 (b 있는지 확인)한 후 b와 현재 값 비교, b < 현재값이면 정답
# b == 0인 경우 b를 삭제 (0으로 초기화)

# max_idx는 [3, 2, 1]같이 큰 값이 중간에 있지 않거나
# [1]같이 리스트 길이가 1인 경우 위해
# 탐색 중에 리턴 안되었으면 마지막에 return해주기 위해 저장

# 그냥 max값의 index 찾으면 끝난다...

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_idx = 0
        cmp = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                cmp = nums[i+1]
                max_idx = i+1
            else:
                if (cmp != 0) and (cmp > nums[i+1]):
                    return i
                else:
                    cmp = 0
        return max_idx
