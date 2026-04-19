class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        enc_str = ""
        for s in strs:
            enc_str = enc_str + str(len(s)) + "#" + s
        return enc_str


    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        dc_list = list()
        i=0
        while i < len(s):
            j=i
            while s[j]!="#":
                j += 1
            wd_len = int(s[i:j])
            i = j + 1
            j = i + wd_len
            dc_list.append(s[i:j])
            i=j
        return dc_list