# import datetime as dt
#
# date1 = dt.date(2020, 1, 1)
# date2 = dt.date(2026,7,13)
# print(date2 - date1)


# def ReserverStr(s:str):
#     tokens = s.split(' ')
#     tokens.reverse()
#     return ' '.join(tokens)
#
# print(ReserverStr('this is word'))


# def rotateString(self, s, goal):
#     """
#     :type s: str
#     :type goal: str
#     :rtype: bool
#     """
#     if len(s) != len(goal):
#         return False
#     return goal in (s + s)



# def countPrefixes(self, words, s):
#     """
#     :type words: List[str]
#     :type s: str
#     :rtype: int
#     """
#     count = 0
#     for word in words:
#         if s.startswith(word):
#             count+=1
#     return count