class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=strs[0]
        for i in strs[1:]:
            if (len(a)>len(i)):
                a = i
        
        prefix = ''
        mismatch = False

        for j in range(len(a)):
            current = a[j]

            for k in strs:
                if(k[j] != current):
                    mismatch = True
            
            if mismatch:
                break

            prefix +=current
        
        return prefix


            