def perform_operation(num1, num2, operation):
  if operation == "add":
    return num1 + num2
  elif operation == "subtract":
    return num1 - num2
  elif operation == "multiply":
    return num1 * num2
  elif operation == "divide":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        return num1 / num2
  else:
     print("Error: invalid operation specified please use add, subtract, multiply or divide")
     return None