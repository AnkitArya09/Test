class Test_1:
    def eliminate(self, nums: [1,1,2]) -> int:
        if nums is None:
            return 0

        i = 0
        for j in range(0, len(nums)):
            if nums[j] != nums[i]:
                i = i + 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

        return i + 1
