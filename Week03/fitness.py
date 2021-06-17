# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ")
    birth = input("Please enter your birthdate (YYYY-MM-DD): ")
    weight = float(input("Enter your weight in US pounds: "))
    height = float(input("Enter your height in US inches: "))

    age = compute_age(birth)
    kg_weight = kg_from_lb(weight)
    cm_height = cm_from_in(height)
    bmi = body_mass_index()
    bmr = basal_metabolic_rate(gender, kg, cm, age)


    print(f"Age (years): {age}")
    print(f"Weight (kg): {kg_weight}")
    print(f"Height (cm): {cm_height}")
    print(f"Body Mass Index: {bmi}")
    print(f"Basal Metobolic Rate: {bmr}")




    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    # and basal_metabolic_rate functions as needed.

    # Print the results for the user to see.
    pass


def compute_age(birth):
    """Compute and return a person's age in years.

    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    kg = weight * 0.45359237
    return round(kg, 1)
    pass


def cm_from_in(height):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """

    cm = height * 2.54
    return round(cm, 1)
    pass


def body_mass_index(kg, cm):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * kg_from_lb(weight))/cm_from_height(height)**2
    return round(bmi, 1)
    pass


def basal_metabolic_rate(gender, kg, cm, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    if gender.upper() == "F":
        return 447.593 + 9.247 * kg_from_lb(weight) + 3.098 * cm_from_height(height) - 4.330 * age
    elif gender.upper() == "M":
        return 88.362 + 13.397 * kg_from_lb(weight) + 4.799 * cm_from_height(height) - 5.677 * age
    pass


# Call the main function so that
# this program will start executing.
main()