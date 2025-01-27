### `syntax.md`

```markdown
# Syntax

EngCode’s syntax is designed to be as close to natural English as possible, making it intuitive and easy to use. This guide provides a comprehensive overview of EngCode’s syntax with examples for each construct.

## Variable Declarations

In EngCode, you can declare variables and assign values to them using simple English phrases.

```engcode
create a variable named 'name' with value 'Alice'
create a variable named 'age' with value 25
```

You can also create more complex variables such as lists and dictionaries:

```engcode
create a variable named 'tasks' with value ['task1', 'task2', 'task3']
create a variable named 'person' with value {'name': 'Alice', 'age': 25}
```

## Conditional Statements

EngCode supports conditional statements that allow you to perform different actions based on conditions.

```engcode
if the variable 'age' is greater than 18
print('You are an adult')
else
print('You are a minor')
```

You can use comparison operators like `greater than`, `less than`, `equal to`, and `not equal to` in your conditions.

## Loops

EngCode supports both `for` and `while` loops, making it easy to iterate over lists or repeat actions while a condition is true.

### For Loop

A `for` loop in EngCode iterates over each item in a list:

```engcode
create a variable named 'tasks' with value ['task1', 'task2', 'task3']
for each item in the list 'tasks'
print(item)
```

### While Loop

A `while` loop repeats a block of code as long as a condition is true:

```engcode
create a variable named 'counter' with value 0
while the variable 'counter' is less than 3
print('Counter: ' + str(counter))
counter = counter + 1
end while
```

## Functions

Functions in EngCode allow you to encapsulate code into reusable blocks. You can define functions with parameters and call them with arguments.

### Function Definition

A function definition in EngCode looks like this:

```engcode
define a function named 'greet' that takes parameters 'name'
print('Hello, ' + name)
end function
```

### Function Call

To call a function, use the `call the function` statement:

```engcode
call the function 'greet' with arguments ('Alice')
```

## Classes

EngCode supports object-oriented programming through classes. You can define classes, create objects, and define methods within classes.

### Class Definition

A class definition in EngCode looks like this:

```engcode
define a class named 'Person'
create a variable named 'first_name' with value 'Unknown'
create a variable named 'last_name' with value 'Unknown'
define a method named 'full_name' that takes parameters 'self'
self_return = self['first_name'] + ' ' + self['last_name']
return self_return
end method
end class
```

### Object Creation

To create an object of a class, use the `create an object named` statement:

```engcode
create an object named 'person1' of class 'Person'
person1.first_name = 'John'
person1.last_name = 'Doe'
print(person1.full_name())
```

## Standard Library Functions

EngCode includes a standard library with functions for mathematical and string operations.

### Mathematical Functions

EngCode provides several built-in functions for common mathematical operations.

#### Square Root

```engcode
create a variable named 'math_lib' with value import('math')
print('Square Root of 16: ' + str(math_lib['sqrt'](16)))
```

#### Power

```engcode
print('2 to the power of 3: ' + str(math_lib['pow'](2, 3)))
```

### String Manipulation Functions

EngCode also includes functions for manipulating strings.

#### Uppercase Conversion

```engcode
create a variable named 'str_lib' with value import('str')
print('Upper Case: ' + str_lib['upper']('hello'))
```

#### Replace

```engcode
print('Replace o with a: ' + str_lib['replace']('hello', 'o', 'a'))
```