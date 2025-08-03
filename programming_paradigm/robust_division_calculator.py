def safe_divide(numerator:float, denominator:float) -> float:
try:
    if denominator == 0:
         raise ZeroDivisionError("Denominator by zero is not allowed.")
    return numerator / denominator
except ZeroDivisionError as e:
     return str(e)
except ValueError:
     return "Invalid input: Please enter numeric values."
