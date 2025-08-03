def safe_divide(numerator, denominator):
try:
    numerator = float(numerator)
    denominator = float(denominator)
    if denominator == 0:
         raise ZeroDivisionError("Denominator by zero is not allowed.")
    return numerator / denominator
except ZeroDivisionError as e:
     return str(e)
except ValueError:
     return "Invalid input: Please enter numeric values."
