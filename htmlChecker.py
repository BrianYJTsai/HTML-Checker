#  File: htmlChecker.py
#  Description: Program parses all tags in an html file. Input is a test file with html tags.
#  Output is an analysis of all the tags and whether the text file is formatted correctly based on the order of tags
#  Student's Name: Brian Tsai
#  Student's UT EID: byt76
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created: 10/10/17
#  Date Last Modified: 10/10/17

class Stack:

    # Initialise new stack
    def __init__(self):
        self.items = []

    # Return a copy of the top of the stack
    def peek(self):
        return(self.items[-1])

    # Add a new item to the top of the stack
    def push(self, item):
        self.items.append(item)

    # Remove the top item of the stack
    def pop(self):
        return self.items.pop()

    # Check if the stack is empty
    def isEmpty(self):
        return (self.items == [])

    # Return how many items are on the stack
    def size(self):
        return len(self.items)

    # Return a string representation of the stack
    def __str__(self):
        return str(self.items)

def getTag(html):

    # Initialize a tag flag and the new tag variables
    found = False
    tag = ""
    tags = []

    # Iterate over each line in the text file
    for line in html:

        # Iterate over each character in a line
        for character in line:

            # Stop appending characters when it reaches the end of a tag
            if ((character == '>' or character == ' ') and found):
                found = False
                tags.append(tag)
                tag = ""

            # If the beginning of a tag has been found, then continue appending characters
            if (found):
                tag += character

            # If the front of a tag has been found, then start appending characters
            if (character == '<'):
                found = True

    return tags

# Compare two tags and return if they are equal
def compareTags(frontTag, endTag):
    return frontTag == endTag

# Process all valid tags in the text file
def processTags(tags):

    # Create a new stack
    stack = Stack()

    # Iterate over all the tags in the list
    for tag in tags:

        # Check if the tag is a starting tag
        if (tag[0] != '/'):

            # Check if the tag is in the exceptions list
            if (tag in EXCEPTIONS):
                print("Tag", tag, "does not need to match: stack is still", stack)

            # Else, it is a valid starting tag
            else:

                # Add the tag to the list of valid tags if it is not already in it
                if (tag not in VALIDTAGS):
                    VALIDTAGS.append(tag)
                    print("New tag", tag, "found and added to list of valid tags")

                # Push the starting tag onto the stack for later analysis
                stack.push(tag)
                print("Tag", tag, "pushed: stack is now", stack)

        # Else, it is an ending tag
        elif (tag[0] == '/'):

            # Check that the stack is not empty
            if (not stack.isEmpty()):

                # Check to see if the ending tag matches a starting tag on the stack
                if (compareTags(stack.peek(), tag[1:])):

                    # If the tags go together, then pop the starting tag off the stack
                    stack.pop()
                    print("Tag", tag, "matches top of stack: stack is now", stack.items)

                # Else, there is an error because the ending tag does not match any starting tag due to order
                else:
                    print("Error: tag is", tag, "but top of stack is", stack.peek())
                    return
            # Else, there is an error because the ending tag does not match any starting tag because the stack is empty
            else:
                print("Error: tag is", tag, "but top of stack is empty")
                return


    # If the stack is empty, then all tags have a matching pair
    if (stack.isEmpty()):
        print("Processing complete. No mismatches found.")

    # Else, there are some starting tags that have not been matched
    else:
        print("Processing complete. Unmatched tags remain on stack: ", stack)

    # Output all valid tags and exceptions
    print("List of valid tags: ", VALIDTAGS)
    print("List of valid exceptions: ", EXCEPTIONS)

# A list of valid tags found
VALIDTAGS = []

# A list of exception tags
EXCEPTIONS = ['meta','br','hr']
def main():

    # Open a buffer
    html = open("htmlfile.txt", "r")

    # Parse all the tags
    tags = getTag(html)
    print("The list of all tags is", tags)

    # Find matching pairs for all tags
    processTags(tags)

    # Close the buffer
    html.close()


main()

