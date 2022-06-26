''' Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33 '''


#CODE

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            output=[[1]]
        elif rowIndex==1:
            output=[[1],[1,1]]
        else:
            output=[[1],[1,1]]
            while rowIndex>1:
                lst=[]
                x=output[-1]
                for i in range(len(x)-1):
                    for j in range(i+1,len(x)):
                        lst.append(x[i]+x[j])
                        break
                lst.insert(0,1)
                lst.append(1)
                output.append(lst)
                rowIndex-=1
        return output[-1]
