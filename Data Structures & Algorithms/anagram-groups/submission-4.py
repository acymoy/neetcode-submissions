class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            bucket = [0 for _ in range(26)]
            for c in s:
                bucket[ord(c) - 97] += 1
            print(bucket)
            t_bucket = tuple(bucket)
            if t_bucket not in m.keys(): 
                m[t_bucket] = [s]
            else:
                m[t_bucket].append(s)
        return list(m.values())