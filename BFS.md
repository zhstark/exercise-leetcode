## 279

BFS不止用在图中

```py
import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n<=0:
            return 0
        
        squares=[i*i for i in range(1, int(math.sqrt(n))+1  )   ]
        toCheck={n}
        cnt=0
        while True:
            temp=set()
            cnt+=1
            for j in toCheck:
                for i in squares:
                    if j<i:
                        break
                    if i==j:
                        return cnt

                    temp.add(j-i)
            toCheck=temp
            

```