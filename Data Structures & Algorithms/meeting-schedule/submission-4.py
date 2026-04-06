"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)>0:
            intervals.sort(key=lambda x: x.start)
            char_list = []
            char_list.append(intervals[0])
            for right in range(1, len(intervals)):
                curr = intervals[right]
                last = char_list[-1]

                if curr.start < last.end:
                    return False
                char_list.append(curr)
            return True
        else:
            return True

