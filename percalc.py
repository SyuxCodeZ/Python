# first type the obtained marks of the test

obtainedmarks = float(input("Enter The Obtained Marks: "))

# then type the full marks of the subject

fullmarks = float(input("Enter The Full Marks: "))

# then calculate the percentage

percentage = obtainedmarks / fullmarks * 100
percentage = int(percentage)

# then print the number with the % symbol and add error messages

if obtainedmarks <= fullmarks:

    print(f"{percentage}%")

elif obtainedmarks == fullmarks:

    print("Obtained Marks And Full Marks Cannot Have The Same Value")

elif fullmarks <= obtainedmarks:

    print("Obtained Marks Should Be Lower Than Full Marks")