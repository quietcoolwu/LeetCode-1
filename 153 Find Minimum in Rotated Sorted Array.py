"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
__author__ = 'Danyang'
class Solution:
    def findMin(self, num):
        """
        similar to find target in rotated sorted array

        :type num: list
        :param num: a list of integer
        :return: an integer
        """
        start = 0
        end = len(num)
        mini = 1<<32
        while start<end:
            mid = (start+end)/2  # skew to right
            mini = min(mini, num[mid])
            if num[start]<=num[mid]<=num[end-1]:
                mini = min(mini, num[start])  # rather than directly return num[start]
                break
            elif num[start]>num[mid]<num[end-1]:
                end = mid
            else:
                start = mid+1

        return mini

if __name__=="__main__":
    num = [7, 1, 2, 3, 4, 5, 6]
    print Solution().findMin(num)
