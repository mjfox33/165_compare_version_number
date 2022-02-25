class Solution:
    #returns -1 if v1<v2, 1 if v1>v2, 0 if v1==v2
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        n = len(v1)
        v2 = [int(i) for i in version2.split('.')]
        m = len(v2)
        shorter = min(n,m)
        for i in range(shorter):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        if n > m:
            for i in range(m,n):
                if v1[i] > 0:
                    return 1
            return 0
        if m > n:
            for i in range(n,m):
                if v2[i] > 0:
                    return -1
            return 0

        return 0