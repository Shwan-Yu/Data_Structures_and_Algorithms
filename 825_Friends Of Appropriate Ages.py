class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = collections.Counter(ages)
        res = 0
        for age, num in count.items():
            for another_age, another_num in count.items():
                if age*0.5+7 < another_age <= age:
                    # person of same age, cannot follow themselves
                    # res += (num-(age==another_age))* another_num
                    res = res+(num-1)*another_num if age == another_age else res+num*another_num
        return res
    
# age 14, 15 won't follow anyone
