# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division and handle potential errors."""
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"  # Format the result to 2 decimal places

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only." 
    except Exception as e:
        return f"Error: {str(e)}"  # Catch any other unforeseen errors