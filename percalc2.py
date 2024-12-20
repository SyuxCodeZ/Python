def calculate_percentage(obtained_marks, full_marks):
    """Calculates the percentage of marks obtained."""
    if not isinstance(obtained_marks, (int, float)) or not isinstance(full_marks, (int, float)):
        raise ValueError("Please enter valid numeric values for obtained marks and full marks.")
    if obtained_marks > full_marks:
        raise ValueError("Obtained marks cannot be greater than full marks.")

    percentage = (obtained_marks / full_marks) * 100
    return int(percentage)

if __name__ == "__main__":
    try:
        obtained_marks = float(input("Enter the obtained marks: "))
        full_marks = float(input("Enter the full marks: "))

        percentage = calculate_percentage(obtained_marks, full_marks)

        print(f"Obtained Marks: {obtained_marks}")
        print(f"Full Marks: {full_marks}")
        print(f"Percentage: {percentage}%")

    except ValueError as e:
        print(f"Error: {e}")