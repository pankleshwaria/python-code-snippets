# Type Hints

### What is typ hinting?

In simple words, you hint the type of the object(s) you're using.

Due to the dynamic nature of Python, inferring or checking the type of an object being used is especially hard. This fact makes it hard for developers to understand what exactly is going on in code they haven't written and, most importantly, for type checking tools found in many IDEs [PyCharm, PyDev come to mind] that are limited due to the fact that they don't have any indicator of what type the objects are.

### Why to type hint?

Helps Type Checkers:
- By hinting at what type you want the object to be the type checker can easily detect if, for instance, you're passing an object with a type that isn't expected.

Helps with documentation:
- A third person viewing your code will know what is expected where, how to use it without getting them TypeErrors.

Helps IDEs develop more accurate and robust tools:
- Development Environments will be better suited at suggesting appropriate methods when know what type your object is. You have probably experienced this with some IDE
at some point, hitting the . and having methods/attributes pop up which aren't defined for an object.

### Example:

```
def sum(x:int, y:int)-> int:
	return x + y

print( sum( 5, 2 ) )
```