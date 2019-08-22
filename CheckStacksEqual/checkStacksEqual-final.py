from stack import Stack
def checkStacksEqual(stack1, stack2):
#Function to check if two stacks are equal.
#   Two stacks are declared equal if all the elements in the two
#   stacks are equal and appear in the same order. 
#   The two stacks should be restored to the state they were in
#   a the start before returning out of the function: all the elements of
#   both the stacks should be placed back in the stacks in the original
#   order.
#   Hint: Use a temporary Stack in your processing to save the elements as you pop
#       the elements from the original stacks to compare them.
    temp = Stack()
    if (stack1.size() != stack2.size()):
        return False
    retVal = True
    while (not stack1.isEmpty()):
        if (stack1.peek() != stack2.peek()):
            retVal = False
            break
        else:
            temp.push(stack1.pop())
            stack2.pop()
    assert(retVal == False or stack2.isEmpty())
    while (not temp.isEmpty()):
        stack1.push(temp.pop())
        stack2.push(stack1.peek())
    return retVal


def createStack(l):
    '''Method to create a stack with elements from the list
    '''
    s = Stack()
    for k in l:
        s.push(k)
    return s

def checkContents(l,s):
    '''confirm contents are the same in the list and the stack
    Note: the stack will be left empty at the end of the function.
    '''
    if (len(l) != s.size()):
        return False
    k = len(l)-1
    while (not s.isEmpty()):
        if (l[k] != s.pop()):
            return False
        k -= 1
    return (k == -1)

def main():
    lol = [
           [[10,20,30,40,50], True],
           [[], False],
           [[10], False],
           [[0,20,30,40,50], False],
           [[10,20,30,40,50], True],
           [[10,20,30,40,60], False],    
           [[10,20,30,40,50], True],
           [[10,20,90,40,60], False],
           [[10,20,30,40,50], True]
           ]           
    # Create a list of stacks from the above data
    allstacks = [createStack(lol[k][0]) for k in range(len(lol))]
    
    print("Checking all the stacks with allstacks[0]")
    for k in range(1,len(allstacks)):
        print(f"Comparing allstacks[0] with allstacks[{k}] should be {lol[k][1]}: {checkStacksEqual(allstacks[0], allstacks[k])}")
        assert(checkContents(lol[k][0], allstacks[k]))#confirm contents are unchanged
    print("Goodbye!")
        
if __name__ == "__main__":
    main()



    

    
