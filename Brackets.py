# we create 2 list for the brackets
open_brackets = ["[","{","("]
close_brackets = ["]","}",")"]

# Function to check brackets
def check(brackets):
	stack = [] #stack for the 2 list to append the input i
	for i in brackets: #check i in the function
		if i in open_brackets: # check i in the first list
			stack.append(i)#use append function to add i in the stack
		elif i in close_brackets: # check i in the second list
			pos = close_brackets.index(i) # using pos to check on the index i
			# build the condition  to check balanced or unbalanced in the stack
			if ((len(stack) > 0) and
				(open_brackets[pos] == stack[len(stack)-1])):
				stack.pop() # to return the stack to top element
			else:
				return "Unbalanced"
	if len(stack) == 0:
		return "Balanced"
	else:
		return "Unbalanced"


# outputs call to compile the code we print the output then check it on the function

output_1 = "{[]{()}}"
print(output_1,"-", check(output_1))

output_2 = "[{}{})(]"
print(output_2,"-", check(output_2))

output_3 = "((()"
print(output_3,"-",check(output_3))

output_4 = "{()}"
print(output_4,"-",check(output_4))
