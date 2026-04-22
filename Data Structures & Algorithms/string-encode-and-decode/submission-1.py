class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('*')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            pos = s.find("*", i)
            length = int(s[i:pos])
            start = pos + 1
            end = start + length
            word = s[start:end]
            res.append(word)
            i = end
        
        return res





