def welcome_statement():
    print("Welocme sir!, this is an AI model that predicts the average score of students taking three tests: Math, Reading, and Writing.")
    print("-----------------------------------------------------------")
    print("The prediction is base on the following features:")
    print("1- Gender")
    print("2- Race/ethnicity")
    print("3- Parental level of education")
    print("4- Student had/didn't have lunch before exam")
    print("5- Student copleted the test preparation course")
    print("-----------------------------------------------------------")
    print("Please answer the following questions to get the prediction score of the student.\n")

def get_gender():
    print("Gender:")
    gender = ""
    while(True):
        try:
            inp = int(input("For male write 1\nFor female write 2\n"))
            if(inp == 1):
                gender = "male"
                break
            elif(inp == 2):
                gender = "female"
                break
            else:
                print("ERROR: Invalid input.\n")
        except:
            print("ERROR: Invalid input.\n")
    return gender


def get_race():
    print("\nRace/ethnicity:")
    race = ""
    while(True):
        try:
            inp = int(input("For group A write 1\nFor group B write 2\nFor group C write 3\nFor group D write 4\nFor group E write 5\n"))
            if(inp == 1):
                race = "group A"
                break
            elif(inp == 2):
                race = "group B"
                break
            elif(inp == 3):
                race = "group C"
                break   
            elif(inp == 4):
                race = "group D"
                break
            elif(inp == 5):
                race = "group E"
                break
            else:
                print("ERROR: Invalid input.\n")
        except:
            print("ERROR: Invalid input.\n")
    return race


def get_parent_edu():
    print("\nParental level of education:")
    level = ""
    while(True):
        try:
            inp = int(input("For bachelor's degree write 1\nFor some college write 2\nFor master's degree write 3\nFor associate's degree write 4\nFor high school write 5\n"))
            if(inp == 1):
                level = "bachelor's degree"
                break
            elif(inp == 2):
                level = "some college"
                break
            elif(inp == 3):
                level = "master's degree"
                break   
            elif(inp == 4):
                race = "associate's degree"
                break
            elif(inp == 5):
                race = "high school"
                break
            else:
                print("ERROR: Invalid input.\n")
        except:
            print("ERROR: Invalid input.\n")
    return level


def get_lunch():
    print("\nStudent had/didn't have lunch before exam:")
    lunch = ""
    while(True):
        try:
            inp = int(input("For YES write 1\nFor NO write 2\n"))
            if(inp == 1):
                lunch = "standard"
                break
            elif(inp == 2):
                lunch = "free/reduced"
                break
            else:
                print("ERROR: Invalid input.\n")
        except:
            print("ERROR: Invalid input.\n")
    return lunch

def get_course():
    print("\nStudent completed\didn't complete the test preparation course:")
    course = ""
    while(True):
        try:
            inp = int(input("For YES write 1\nFor NO write 2\n"))
            if(inp == 1):
                course = "completed"
                break
            elif(inp == 2):
                course = "none"
                break
            else:
                print("ERROR: Invalid input.\n")
        except:
            print("ERROR: Invalid input.\n")
    return course

def prediction(x_pred):
    import joblib
    model = joblib.load("model.pkl")
    y_pred = model.predict(x_pred)
    print("The predicted average score for the student is: ", y_pred)

def main():
    welcome_statement()
    gender = get_gender()
    race = get_race()
    level = get_parent_edu()
    lunch = get_lunch()
    course = get_course()

    def data_transformation():
        import pandas as pd

        data = {
        "gender_female"                                   : [float(gender == "female")]  ,
        "gender_male"                                     : [float(gender == "male")]    ,
        "race/ethnicity_group A"                          : [float(race == "group A")]   ,
        "race/ethnicity_group B"                          : [float(race == "group B")]   ,
        "race/ethnicity_group C"                          : [float(race == "group C")]   ,
        "race/ethnicity_group D"                          : [float(race == "group D")]   ,
        "race/ethnicity_group E"                          : [float(race == "group E")]   ,
        "parental level of education_associate's degree"  : [float(level == "associate's degree")]  ,
        "parental level of education_bachelor's degree"   : [float(level == "bachelor's degree")]  ,
        "parental level of education_high school"         : [float(level == "high school")]  ,
        "parental level of education_master's degree"     : [float(level == "master's degree")]  ,
        "parental level of education_some college"        : [float(level == "some college")]  ,
        "parental level of education_some high school"    : [float(level == "high school")]  ,
        "lunch_free/reduced"                              : [float(lunch == "free/reduced")]  ,
        "lunch_standard"                                  : [float(lunch == "standard")]  ,
        "test preparation course_completed"               : [float(course == "completed")],
        "test preparation course_none"                    : [float(course == "none")]
        }
        data = pd.DataFrame(data)
        return data

    prediction(data_transformation())

main()

