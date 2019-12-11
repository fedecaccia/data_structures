import pytest

class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, ni in enumerate(nums, 0):
            for j, nj in enumerate(nums[i+1:], i+1):
                if ni + nj == target:
                    return [i, j]
        raise Exception("No two sum solution")

class Solution2(object):
    def twoSum(self, nums, target):
        pos = {}
        for i, ni in enumerate(nums):
            pos[ni] = i

        for i, ni in enumerate(nums):
            if (target-ni) in pos and pos[target-ni] != i:
                return [i, pos[target-ni]]
        raise Exception("No two sum solution")

class Solution3(object):
    def twoSum(self, nums, target):
        pos = {}
        for i, ni in enumerate(nums):
            if (target-ni) in pos and pos[target-ni] != i:
                return [i, pos[target-ni]]
            pos[ni] = i
        raise Exception("No two sum solution")


def test_solution1():
    print("Solution 1")
    a1 = Solution1()
    assert(a1.twoSum([2, 7, 11, 15], 9)==[0,1])
    assert(a1.twoSum([3, 2, 4], 6)==[1,2])
    assert(a1.twoSum([3, 3], 6)==[0,1])

def test_solution2():
    print("Solution 2")
    a2 = Solution2()
    assert(a2.twoSum([2, 7, 11, 15], 9)==[0,1])
    assert(a2.twoSum([3, 2, 4], 6)==[1,2])
    assert(a2.twoSum([3, 3], 6)==[0,1])

def test_solution3():
    print("Solution 3")
    a3 = Solution3()
    assert(a3.twoSum([2, 7, 11, 15], 9)==[1,0])
    assert(a3.twoSum([3, 2, 4], 6)==[2,1])
    assert(a3.twoSum([3, 3], 6)==[1,0])
        