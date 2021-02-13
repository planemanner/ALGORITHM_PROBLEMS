''' 3. Longest Substring Without Repeating Characters '''

"""
Problem description

Given a string s, find the length of the longest substring without repeating characters.

Example. 1)
Input: s = "abcabcbb"
Output: 3

Explanation: The answer is "abc", with the length of 3.

Example. 2)

Input: s = "bbbbb"
Output: 1

Explanation: The answer is "b", with the length of 1.

Example. 3)
Input: s = "pwwkew"
Output: 3

Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example. 4)
Input: s = ""
Output: 0

"""
import collections
class Solution(object):  # My Solution
    def lengthOfLongestSubstring(self, s):

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            pattern_list = collections.deque()
            pattern = s[0]
            eot = False
            idx = 1
            repeat_idx = 0
            while (not eot) and (idx <= (len(s)-1)):

                ch = s[idx]
                pattern_start_ch = pattern[0]

                if pattern_start_ch != ch and ch != pattern[-1] and ch not in pattern:
                    '''pattern update'''
                    pattern += ch
                    idx += 1

                else:
                    '''catch probably same pattern'''
                    '''case 1: ababcdef'''
                    """
                    새로운 패턴을 찾을 건가? abbabc 의 경우 어떻게?
                    이후 패턴이 기존 패턴과 일치하는지  
                    """
                    if len(s[idx:]) >= len(pattern):  # 잔여 길이가 pattern 문자열보다 길면
                        if s[idx:idx+len(pattern)] == pattern and ch not in pattern:  # pattern 이랑 같으면 jump!
                            idx += len(pattern)
                            pattern_list.append(pattern)  # Add a kind of pattern
                            if idx < (len(s)-1):
                                pattern = s[idx]  # Initialize a new pattern when characters are left
                                idx += 1
                                # print("{} check".format(idx))
                            '''abcabcd'''
                        elif ch in pattern:
                            '''dvdf-> vdf, vdadf, avdabf, xxzqi->xzqi, xxzqiyxzqi'''

                            repeat_idx = s.find(ch, repeat_idx) + 1
                            pattern_list.append(pattern)
                            pattern = s[repeat_idx]
                            idx = repeat_idx + 1

                        else:
                            pattern_list.append(pattern)
                            idx += 1
                            pattern = s[idx]  # new pattern initialization
                            idx += 1

                            '''abcaddd, abcagdef, wwkew'''
                    else:
                        if ch in pattern:
                            repeat_idx = s.find(ch, repeat_idx) + 1
                            pattern_list.append(pattern)
                            pattern = s[repeat_idx]
                            idx = repeat_idx + 1
                        else:
                            idx += 1

            pattern_list.append(pattern)
            return max([len(a_pattern) for a_pattern in pattern_list])


class Best_solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        for i, value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength

solver = Solution()
b_solver = Best_solution()
print(b_solver.lengthOfLongestSubstring("abcabcf"))
# print(solver.lengthOfLongestSubstring("abcabcf"))  # abcf
# print(solver.lengthOfLongestSubstring('dvdf'))  # vdf
# print(solver.lengthOfLongestSubstring('abcb'))  # abc
# print(solver.lengthOfLongestSubstring('xxzqi'))  # xzqi
# print(solver.lengthOfLongestSubstring('avdabf'))  # vdabf : 5
# print(solver.lengthOfLongestSubstring('xxzqiyclqiabcdefg'))  # lqiabcdefg : 10
# print(solver.lengthOfLongestSubstring('ckilbkd'))  # ckilb
print(solver.lengthOfLongestSubstring("hkcpmprxxxqw"))  #  hkcpm



