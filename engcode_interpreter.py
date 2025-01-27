import re
import importlib

# Standard Library and Built-in Functions
def engcode_print(text):
    print(text)

def engcode_input(prompt):
    return input(prompt)

def engcode_len(variable):
    return len(variable)

def engcode_sum(variable):
    if isinstance(variable, list):
        return sum(variable)
    else:
        raise TypeError(f"{variable} is not a list")

def engcode_max(variable):
    if isinstance(variable, list):
        return max(variable)
    else:
        raise TypeError(f"{variable} is not a list")

def engcode_min(variable):
    if isinstance(variable, list):
        return min(variable)
    else:
        raise TypeError(f"{variable} is not a list")

def engcode_range(start, end):
    return list(range(start, end))

def engcode_read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def engcode_write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    return f"Content written to {file_path}"

def engcode_import(module_name):
    if module_name in standard_library:
        return standard_library[module_name]
    else:
        raise ImportError(f"Module {module_name} not found in standard library")

built_in_functions = {
    'print': engcode_print,
    'input': engcode_input,
    'len': engcode_len,
    'sum': engcode_sum,
    'max': engcode_max,
    'min': engcode_min,
    'range': engcode_range,
    'read_file': engcode_read_file,
    'write_file': engcode_write_file,
    'import': engcode_import
}

# Define the standard_library dictionary
standard_library = {
    'math': __import__('math'),
    'json': __import__('json'),
    # Add other standard library modules as needed
}

# Parser
def parse_code(lines):
    parsed_code = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        try:
            if "create a variable named" in line:
                match = re.search(r"create a variable named '(.*)' with value (.*)", line)
                if match:
                    variable_name = match.group(1)
                    value = match.group(2)
                    try:
                        value = eval(value)
                    except:
                        value = value.strip("'")
                    if isinstance(value, range):
                        value = list(value)
                    parsed_code.append({'type': 'variable_declaration', 'name': variable_name, 'value': value})
                else:
                    raise SyntaxError(f"Syntax error in line: {line}")
            elif "if the variable" in line:
                match = re.search(r"if the variable '(.*)' is greater than (.*)", line)
                if match:
                    variable_name = match.group(1)
                    value = match.group(2)
                    parsed_code.append({'type': 'conditional', 'name': variable_name, 'value': value})
                else:
                    raise SyntaxError(f"Syntax error in line: {line}")
            elif "for each item in the list" in line:
                match = re.search(r"for each item in the list '(.*)'", line)
                if match:
                    list_name = match.group(1)
                    parsed_code.append({'type': 'loop', 'list_name': list_name})
                else:
                    raise SyntaxError(f"Syntax error in line: {line}")
            elif "while the variable" in line:
                match = re.search(r"while the variable '(.*)' is less than (.*)", line)
                if match:
                    variable_name = match.group(1)
                    value = match.group(2)
                    body = []
                    i += 1
                    while i < len(lines) and not lines[i].strip().startswith("end while"):
                        body.append(lines[i].strip())
                        i += 1
                    parsed_code.append({'type': 'while_loop', 'name': variable_name, 'value': value, 'body': body})
                else:
                    raise SyntaxError(f"Syntax error in line: {line}")
            elif "switch the variable" in line:
                match = re.search(r"switch the variable '(.*)'", line)
                if match:
                    variable_name = match.group(1)
                    cases = {}
                    i += 1
                    while i < len(lines) and not lines[i].strip().startswith("end switch"):
                        case_match = re.search(r"case '(.*)':", lines[i].strip())
                        if case_match:
                            case_value = case_match.group(1)
                            case_body = []
                            i += 1
                            while i < len(lines) and not re.match(r"case '(.*)':", lines[i].strip()) and not lines[i].strip().startswith("end switch"):
                                case_body.append(lines[i].strip())
                                i += 1
                            cases[case_value] = case_body
                        else:
                            i += 1
                    parsed_code.append({'type': 'switch', 'name': variable_name, 'cases': cases})
                else:
                    raise SyntaxError(f"Syntax error in line: {line}")
            elif "define a function named" in line:
                match = re.search(r"define a function named '(.*)' that takes parameters (.*)", line)
                if match:
                    function_name = match.group(1)
                    parameters = match.group(2).split(',')
                    body = []
                    i += 1
                    while i < len(lines) and not lines[i].strip().startswith("end function"):
                        body.append(lines[i].strip())
                        i += 1
                    parsed_code.append({'type': 'function_definition', 'name': function_name, 'parameters': parameters, 'body': body})
                else:
                    raise SyntaxError(f"Syntax error in line: {line}")
            elif "call the function" in line:
                match = re.search(r"call the function '(.*)' with arguments \((.*)\)", line)
                if match:
                    function_name = match.group(1)
                    arguments = match.group(2).split(',')
                    parsed_code.append({'type': 'function_call', 'name': function_name, 'arguments': arguments})
                else:
                    raise SyntaxError(f"Syntax error in line: {line}")
            elif "return" in line:
                return_value = line.split('return')[1].strip()
                parsed_code.append({'type': 'return', 'value': return_value})
            elif "try" in line:
                try_block = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith("except"):
                    try_block.append(lines[i].strip())
                    i += 1
                except_block = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith("end try"):
                    except_block.append(lines[i].strip())
                    i += 1
                parsed_code.append({'type': 'try_except', 'try_block': try_block, 'except_block': except_block})
            elif "define a class named" in line:
                match = re.search(r"define a class named '(.*)'", line)
                if match:
                    class_name = match.group(1)
                    class_body = []
                    i += 1
                    while i < len(lines) and not lines[i].strip().startswith("end class"):
                        class_body.append(lines[i].strip())
                        i += 1
                    parsed_code.append({'type': 'class_definition', 'name': class_name, 'body': class_body})
                else:
                    raise SyntaxError(f"Syntax error in line: {line}")
            elif "create an object named" in line:
                match = re.search(r"create an object named '(.*)' of class '(.*)'", line)
                if match:
                    object_name = match.group(1)
                    class_name = match.group(2)
                    parsed_code.append({'type': 'object_creation', 'object_name': object_name, 'class_name': class_name})
                else:
                    raise SyntaxError(f"Syntax error in line: {line}")
            elif "call the method" in line:
                match = re.search(r"call the method '(.*)' on object '(.*)' with arguments \((.*)\)", line)
                if match:
                    method_name = match.group(1)
                    object_name = match.group(2)
                    arguments = match.group(3).split(',')
                    parsed_code.append({'type': 'method_call', 'method_name': method_name, 'object_name': object_name, 'arguments': arguments})
                else:
                    raise SyntaxError(f"Syntax error in line: {line}")
            else:
                parsed_code.append(None)
        except Exception as e:
            print(f"Error parsing line {i+1}: {line}. Error: {e}")
            parsed_code.append(None)
        i += 1
    return parsed_code

# Interpreter
variables = {}
functions = {}
classes = {}

def execute(parsed_code):
    global variables, functions, classes, built_in_functions
    variables = {}
    functions = {}
    classes = {}
    built_in_functions = globals().copy()

    for idx, line in enumerate(parsed_code):
        if line is None:
            continue  # Skip None values

        try:
            if line['type'] == 'variable_declaration':
                variables[line['name']] = line['value']
            elif line['type'] == 'conditional':
                if variables.get(line['name']) and int(variables[line['name']]) > int(line['value']):
                    print("Condition met: You are an adult")
                else:
                    print("Condition not met: You are a minor")
            elif line['type'] == 'loop':
                list_name = line['list_name']
                if list_name in variables and isinstance(variables[list_name], list):
                    for item in variables[list_name]:
                        exec(f"print({repr(item)})", built_in_functions)
                else:
                    raise ValueError(f"List '{list_name}' not found or not a list")
            elif line['type'] == 'while_loop':
                variable_name = line['name']
                value = line['value']
                while variables.get(variable_name) and variables[variable_name] < int(value):
                    for func_line in line['body']:
                        exec(func_line, built_in_functions, variables)
            elif line['type'] == 'switch':
                variable_name = line['name']
                cases = line['cases']
                if variable_name in variables:
                    case_body = cases.get(str(variables[variable_name]))
                    if case_body:
                        for case_line in case_body:
                            exec(case_line, built_in_functions, variables)
                    else:
                        print(f"No match found for switch case: {variables[variable_name]}")
            elif line['type'] == 'function_definition':
                functions[line['name']] = {'parameters': line['parameters'], 'body': line['body']}
                print(f"Function {line['name']} defined.")
            elif line['type'] == 'function_call':
                function = functions.get(line['name'])
                if function:
                    params = function['parameters']
                    body = function['body']
                    arguments = line['arguments']
                    local_vars = variables.copy()
                    for param, arg in zip(params, arguments):
                        local_vars[param.strip()] = eval(arg.strip(), built_in_functions, variables)
                    for func_line in body:
                        exec(func_line, built_in_functions, local_vars)
                else:
                    raise NameError(f"Function {line['name']} not defined.")
            elif line['type'] == 'return':
                return eval(line['value'], built_in_functions, variables)
            elif line['type'] == 'try_except':
                try:
                    for try_line in line['try_block']:
                        exec(try_line, built_in_functions, variables)
                except Exception as e:
                    for except_line in line['except_block']:
                        exec(except_line, built_in_functions, variables)
            elif line['type'] == 'class_definition':
                class_name = line['name']
                class_body = line['body']
                methods = {}
                attributes = {}
                i = 0  # Initialize i
                while i < len(class_body):
                    class_line = class_body[i]
                    if class_line.startswith("define a method named"):
                        method_match = re.search(r"define a method named '(.*)' that takes parameters (.*)", class_line)
                        if method_match:
                            method_name = method_match.group(1)
                            parameters = method_match.group(2).split(',')
                            method_body = []
                            i += 1
                            while i < len(class_body) and not class_body[i].strip().startswith("end method"):
                                method_body.append(class_body[i].strip())
                                i += 1
                            methods[method_name] = {'parameters': parameters, 'body': method_body}
                        else:
                            raise SyntaxError(f"Syntax error in line: {class_line}")
                    elif class_line.startswith("create a variable named"):
                        var_match = re.search(r"create a variable named '(.*)' with value (.*)", class_line)
                        if var_match:
                            var_name = var_match.group(1)
                            var_value = var_match.group(2)
                            attributes[var_name] = eval(var_value)
                        else:
                            raise SyntaxError(f"Syntax error in line: {class_line}")
                    i += 1
                classes[class_name] = {'methods': methods, 'attributes': attributes}
                print(f"Class {class_name} defined.")
            elif line['type'] == 'object_creation':
                object_name = line['object_name']
                class_name = line['class_name']
                if class_name in classes:
                    class_def = classes[class_name]
                    methods = class_def['methods']
                    attributes = class_def['attributes'].copy()
                    variables[object_name] = {'methods': methods, 'attributes': attributes}
                    print(f"Object {object_name} of class {class_name} created.")
                else:
                    raise NameError(f"Class {class_name} not defined.")
            elif line['type'] == 'method_call':
                method_name = line['method_name']
                object_name = line['object_name']
                arguments = line['arguments']
                if object_name in variables:
                    obj = variables[object_name]
                    if method_name in obj['methods']:
                        method_def = obj['methods'][method_name]
                        params = method_def['parameters']
                        body = method_def['body']
                        local_vars = variables.copy()
                        for param, arg in zip(params, arguments):
                            local_vars[param.strip()] = eval(arg.strip(), built_in_functions, variables)
                        for method_line in body:
                            exec(method_line, built_in_functions, local_vars)
                    else:
                        raise NameError(f"Method {method_name} not found in object {object_name}.")
                else:
                    raise NameError(f"Object {object_name} not defined.")
        except Exception as e:
            print(f"Error executing line {idx+1}: {line}. Error: {e}")

# Example usage
code = [
    "create a variable named 'name' with value 'Alice'",
    "create a variable named 'age' with value 25",
    "create a variable named 'tasks' with value ['task1', 'task2', 'task3']",
    "create a variable named 'person' with value {'name': 'Alice', 'age': 25}",
    "print('Name: ' + person['name'])",
    "print('Age: ' + str(person['age']))",
    "if the variable 'age' is greater than 18",
    "print('You are an adult')",
    "for each item in the list 'tasks'",
    "print(item)",
    "define a function named 'greet' that takes parameters 'name, age'",
    "print('Hello, ' + name + '. You are ' + str(age) + ' years old.')",
    "end function",
    "call the function 'greet' with arguments ('Alice', '25')",
    "create a variable named 'counter' with value 0",
    "while the variable 'counter' is less than 3",
    "print('Counter: ' + str(counter))",
    "counter = counter + 1",
    "end while",
    "switch the variable 'age'",
    "case '18':",
    "print('You are 18 years old')",
    "case '25':",
    "print('You are 25 years old')",
    "end switch",
    "define a function named 'add' that takes parameters 'a, b'",
    "return str(a + b)",
    "end function",
    "create a variable named 'sum_result' with value call the function 'add' with arguments ('5', '10')",
    "print('Sum Result: ' + sum_result)",
    "try",
    "print('Trying to open a non-existent file...')",
    "create a variable named 'file_content' with value read_file('non_existent.txt')",
    "print('File content: ' + file_content)",
    "except",
    "print('An error occurred while reading the file.')",
    "end try",
    "create a variable named 'math_lib' with value import('math')",
    "print('Square Root of 16: ' + str(math_lib['sqrt'](16)))",
    "create a variable named 'str_lib' with value import('str')",
    "print('Upper Case: ' + str_lib['upper']('hello'))",
    "define a class named 'Person'",
    "create a variable named 'first_name' with value 'Unknown'",
    "create a variable named 'last_name' with value 'Unknown'",
    "define a method named 'full_name' that takes parameters 'self'",
    "self_return = self['first_name'] + ' ' + self['last_name']",
    "return self_return",
    "end method",
    "end class",
    "create an object named 'person1' of class 'Person'",
    "person1.first_name = 'John'",
    "person1.last_name = 'Doe'",
    "print(person1.first_name + ' ' + person1.last_name)",
    "print(person1.full_name())",
]

parsed_code = parse_code(code)
print(parsed_code)

execute(parsed_code)