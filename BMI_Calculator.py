def get_positive_float(prompt):
    """Repeatedly asks for input until a valid positive number is given."""
    while True:
        try:
            user_input = input(prompt).strip()
            # Handle blank inputs
            if not user_input:
                print("Error: Input cannot be blank.")
                continue
            
            value = float(user_input)
            
            # Handle zero or negative inputs
            if value <= 0:
                print("Error: Please enter a positive number greater than zero.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")

def calculate_bmi():
    print("--- BMI Calculator ---")
    
    # Get valid inputs
    weight = get_positive_float("Enter weight in kg: ")
    height_cm = get_positive_float("Enter height in cm: ")
    
    # Calculate BMI
    # Formula: kg/m^2
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    
    # Output result
    print(f"\nYour BMI is: {bmi:.2f}")
    
    # BMI Category
    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 25:
        print("Category: Normal weight")
    elif 25 <= bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obesity")

if __name__ == "__main__":
    calculate_bmi()
