def obtaingrade(Marks):
    if Marks>90:
        return "A+"
    elif Marks >= 80 and Marks < 90:
        return "A"
    elif Marks >= 70 and Marks < 80:
        return "B+"
    elif Marks >= 60 and Marks < 70:
        return "B"
    elif Marks >= 50 and Marks < 60:
        return "C"
    elif Marks >= 40 and Marks < 50:
        return "D"
    else:
        return "Fail"
    
def main():
    print("Student Grade Calculator")
    subjects=int(input("Enter number of subjects:"))
    total_marks=0
    if subjects<=0:
        print("Invalid Number of Subjects")
        exit()
    for i in range(1,subjects+1):
        marks=float(input(f"Enter Marks scored in Subject {i}:"))
        if marks>100:
            print("Invalid: Total marks obtained cannot be greater than 100.")
            exit()
        elif marks<0:
            print("Invalid: Marks cannot be negative.")
            exit()
        total_marks+=marks
    average_marks=total_marks/subjects
    Grade=obtaingrade(average_marks)
    Percentage=round((total_marks/(subjects*100))*100,2)
    print(f"\t----Results----\n\tTotal Marks={total_marks}\n\tGrade:{Grade}\n\tPercentage:{Percentage}%")

if __name__ == "__main__":
    main()
