# EngCode Examples

This section provides examples of EngCode in action, demonstrating its syntax and features through practical use cases.

## Basic Example

This example shows how to declare variables, perform conditional checks, and print output.

```engcode
create a variable named 'name' with value 'Alice'
create a variable named 'age' with value 25
print('Name: ' + name)
print('Age: ' + str(age))
if the variable 'age' is greater than 18
    print('You are an adult')
else
    print('You are a minor')
```

## Loop Example

This example demonstrates how to use a for loop to iterate over a list.

```engcode
create a variable named 'tasks' with value ['task1', 'task2', 'task3']
for each item in the list 'tasks'
    print(item)
```

## While Loop Example

This example demonstrates how to use a while loop.

```engcode
create a variable named 'counter' with value 0
while the variable 'counter' is less than 3
    print('Counter: ' + str(counter))
    counter = counter + 1
end while
```

## Function Example

This example shows how to define and call a function.

```engcode
define a function named 'greet' that takes parameters 'name'
    print('Hello, ' + name)
end function

call the function 'greet' with arguments ('Alice')
```

## Class and Object Example

This example shows how to define a class, create an object, and call a method.

```engcode
define a class named 'Person'
    create a variable named 'first_name' with value 'Unknown'
    create a variable named 'last_name' with value 'Unknown'
    define a method named 'full_name' that takes parameters 'self'
        self_return = self['first_name'] + ' ' + self['last_name']
        return self_return
    end method
end class

create an object named 'person1' of class 'Person'
person1.first_name = 'John'
person1.last_name = 'Doe'
print(person1.full_name())
```

## Advanced Example

This advanced example combines variables, loops, functions, and classes to create a more complex program.

```engcode
create a variable named 'tasks' with value ['task1', 'task2', 'task3']
for each item in the list 'tasks'
    print(item)

define a function named 'add' that takes parameters 'a, b'
    return a + b
end function

create a variable named 'result' with value call the function 'add' with arguments (5, 10)
print('Result: ' + result)

define a class named 'Person'
    create a variable named 'first_name' with value 'Unknown'
    create a variable named 'last_name' with value 'Unknown'
    define a method named 'full_name' that takes parameters 'self'
        self_return = self['first_name'] + ' ' + self['last_name']
        return self_return
    end method
end class

create an object named 'person1' of class 'Person'
person1.first_name = 'John'
person1.last_name = 'Doe'
print(person1.full_name())
```

```