class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            h_array = [0] * 26
            for l in s:
                position = ord(l) - 96 - 1
                print(position)
                h_array[position] += 1

            t = tuple(h_array)
            if t in m.keys():
                m[t].append(s)
            else:
                m[t] = [s]
        print(m)
        return list(m.values())