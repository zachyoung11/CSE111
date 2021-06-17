import pandas as pd

def create_student_dict():
    student_dict = pd.read_csv('students.csv', header=0, index_col=0, squeeze=True).to_dict()
    return student_dict

def main():
    student_dict = create_student_dict()
    print(student_dict)
    get_inumber(student_dict)

def get_inumber(dictionary):
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    if i_number in create_student_dict():
        print(dictionary(i_number))
    else:
        print("No such student")


if __name__ == "__main__":
    main()