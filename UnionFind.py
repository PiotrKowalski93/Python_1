def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        #Parents
        parents = {}

        def find(x):
            if x not in parents:
                parents[x] = x
            if x != parents[x]:
                parents[x] = find(parents[x])
            print(parents)
            return parents[x]
            
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            print("RootX:", rootX, "RootY:", rootY)
            if rootX > rootY:
                print("RootX > RootY")
                parents[rootX] = rootY
            else:
                print("RootX <= RootY")
                parents[rootY] = rootX
            print(parents)

        for i in range(len(s1)):
            union(s1[i],s2[i])
        
        res = []
        for c in baseStr:
            res.append(find(c))
            print(res)
            
        return ''.join(res)