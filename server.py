# server.py
# where your python app starts

# init project
from flask import Flask, jsonify, render_template, request
application = Flask(__name__)

# -----------------------------------------------------------------
# -----------------------------------------------------------------

# The idea of this question is to build a simple postfix interpreter.
# While we usually use infix expressions, it's easier for code to handle postfix expressions.
# The code evaluating the expression doesn't have to handle order of operations, and can find the result using a stack.  

#     Infix       Postfix         Result
#     3+5         3 5 +           [8]
#     7-3         7 3 -           [4]
#     5 * 3-10    5 3 * 10 -      [5]
#     5(3-10)     5 3 10 - *      [-35]

#     The expression is processed from left to right.  When a number is encountered, the number is pushed onto the stack.
# When an operator is encountered, two numbers are popped from the stack, the operator is applied to those two numbers,
# and the result is pushed back onto the stack.  If the expression is well-formed, the result will be left on top of the stack.  
# For the purposes of this exercise we'll assume that the expressions will all be valid.

# First test cases - pushing operands onto the stack:
# "1 2" -> [1, 2]
# "15 6 2" -> [15, 6, 2]

# Your code here
print('Print output displays in the log panel below under the tools menu')





# listen for requests :)
if __name__ == "__main__":
    from os import environ
    application.run(host='0.0.0.0', port=int(environ['PORT']))