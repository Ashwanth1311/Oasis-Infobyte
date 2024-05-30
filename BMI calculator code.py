#formula for BMI calculator
def formula_bmi(weigth,heigth):
    bmi = weigth/(heigth ** 2)

#category in BMI 
def process_bmi(bmi):
    if bmi < 18.5:
        return "Under weigth"
    elif bmi < 24.4:
        return"Normal weigth"
    elif bmi < 29.9:
        return "Over weigth"
    elif bmi < 34.9:
        return "Moderately obese"
    elif bmi < 39.9:
        return "Severely obese"
    elif bmi < 40.0:
        return "Morbidly obese"
    else:
        return "Obese" 
#user-input method to get the values of weigth and heigth from user
def start():
    try:
        weigth = float(input("Enter your weigth in kilograms: "))
        heigth = float(input("Enter your heigth in meters: "))
        if weigth <= 0 or heigth <= 0:
            print("Invalid input! Your value must be greater than zero.")
        else:
            bmi = formula_bmi(weigth,heigth)
            category = process_bmi(bmi)

            print(f"Your BMI is: {bmi}")
            print("category:",category)
    except ValueError:
            print("Invaild input! Your value must be numeric values.")

#Main program
if __name__ == "__main__":
    start()