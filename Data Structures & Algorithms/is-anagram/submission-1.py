class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s.lower()) == sorted(t.lower())

        # OR

        if len(s) != len(t):   # if both strings are different lengths then not anagram
            return False

        count = {}   # create a hashmap

        for ch in s:
            count[ch] = count.get(ch, 0) + 1  # loop if the ch in the dict, then add 1, else consider 0 and then add 1

        for ch in t:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1

        return True


        