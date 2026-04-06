class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ''
        for i in strs:
            # length = len(i)
            st += '@2'+i
        return st
    def decode(self, s: str) -> List[str]:
        return s.split('@2')[1:]
        

