#User function Template for python3

class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        #code here
        st = []
        exp = ['*', '+', '/', '-']
        for each in S:
            if each not in exp:
                st.append(each)
            else:
                a = int(st.pop())
                b = int(st.pop())
                if each == '*':
                    st.append(a * b)
                elif each == '/':
                    st.append(b // a)
                elif each == '+':
                    st.append(a + b)
                else:
                    st.append(b - a)
        return st[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        S = input()
        obj = Solution()
        print('{0:g}'.format(float(obj.evaluatePostfix(S))))
# } Driver Code Ends