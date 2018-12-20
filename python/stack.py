from sys import maxsize 

def createStack():
  stack = []
  return stack

def isEmpty(stack):
  return len(stack) == 0

def push(stack, item):
  stack.append(item)
  print(item + "pushed to stack")

def pop(stack):
  if isEmpty(stack):
    return str(-maxsize -1)
  return stack.pop()


# Driver program to test above functions     
stack = createStack() 
push(stack, str(10)) 
push(stack, str(20)) 
push(stack, str(30)) 
print(pop(stack) + " popped from stack") 
