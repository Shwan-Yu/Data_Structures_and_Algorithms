```
class Solution(object):
    def reorganizeString(self, S):
        # e.g. "a a a a" . Then assign b and c betweem a, so b and c are definately separate,
		# just check if a are separate: if total number of other char greater than count[a] -1.
        count = collections.Counter(S)
        max_char, max_count = count.most_common()[0][0], count.most_common()[0][1]
        reorg = [max_char] * max_count
        index = 0
        for other_char in count.keys():
            if other_char != max_char:
                for i in range(count[other_char]):
                    reorg[index % len(reorg)] += other_char
                    index += 1
        # if we have n max_char, we need at least n-1 other chars to separate them.
        return "".join(reorg) if index >= max_count-1 else ""
```
