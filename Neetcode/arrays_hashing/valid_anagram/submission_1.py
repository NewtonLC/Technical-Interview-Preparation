"""
Date: 09/15/2025 18:07
Memory: O(n*k)
Runtime: O(n*k)
- n is the number of strings in the input list strs
- k is the maximum length of a string in strs
"""

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # In: str[]
        # Out: str[][]
        # C: strings that are anagrams of each other need to be in their own lists.
        # E:
        # - Empty strings --> their own set of anagrams
        # - Single str --> its own set
        # - all lowercase english words

        # - How do we figure out that two strings are anagrams?
            # - Count through the characters, add them to a map that tracks frequency
                # - If the maps are equal, return True. Else return false.
            # length of two strings are equal. If not, return false.
        
        # - How can we sort the strings into their own lists?
            # 1. Another map --> array of letters --> string anagram sublist
        
        # initialize 26 array
        # loop through array
            # get the array of letters for each string
            # Add the string to the map.
                # If the array of letters does not exist, add it, and set the string to [string] as the value
                # If the array of letters does exist, add string to the sublist.
        def get_frequencies(s):
            alphabet = [0] * 26
            for c in s:
                alphabet[ord(c)-97] += 1
            return tuple(alphabet)

        alphabet = tuple([0] * 26)
        str_sublists = {}

        for s in strs:
            alphabet = get_frequencies(s)
            if alphabet in str_sublists:
                str_sublists[alphabet] += [s]
            else:
                str_sublists[alphabet] = [s]

        return list(str_sublists.values())
"""

def groupAnagrams(strs):
    def get_frequencies(s):
        alphabet = [0] * 26
        for c in s:
            alphabet[ord(c)-97] += 1
        return tuple(alphabet)

    alphabet = tuple([0] * 26)
    str_sublists = {}

    for s in strs:
        alphabet = get_frequencies(s)
        if alphabet in str_sublists:
            str_sublists[alphabet] += [s]
        else:
            str_sublists[alphabet] = [s]

    return list(str_sublists.values())

# Important note: Since the constraint is that only english letters may be used, the length of the hash table will never exceed 26. Thus, the space complexity is O(1).

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(["x"])) # [["x"]]
print(groupAnagrams([""])) # [[""]]
