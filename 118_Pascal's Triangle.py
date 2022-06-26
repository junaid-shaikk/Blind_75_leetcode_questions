''' Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30 '''

#CODE

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows==1:
            output=[[1]]
        elif numRows==2:
            output=[[1],[1,1]]
        else:
            output=[[1],[1,1]]
            while numRows>2:
                lst=[]
                x=output[-1]
                for i in range(len(x)-1):
                    for j in range(i+1,len(x)):
                        lst.append(x[i]+x[j])
                        break
                lst.insert(0,1)
                lst.append(1)
                output.append(lst)
                numRows-=1
        return output
