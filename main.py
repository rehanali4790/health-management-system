client_list = ["","rehan","ali","samo"]
list_of_excercise = ["",open("rehan ex.txt","a"),open("ali ex.txt","a"),open("samo ex.txt","a")]
list_of_diet = ["",open("rehan.txt","a"),open("ali.txt","a"),open("samo.txt","a")]
def date_time():
    import datetime
    return datetime.datetime.now()

def health_system():
    while True:
        print("what you wanna enter? excercise or diet?")
        access_ = input()
        print("Which client you want to look in"
              " enter client number, 1 , 2 , 3 for rehan, ali, samo respectively")
        client_ = int(input())
        if access_ == "excercise":
             print("you are in \t", client_list[client_], access_, "program")
             f = list_of_excercise[client_]
             print("enter excercise done by client")
             excercise = input()
             f.write(excercise)
             print("Do you want to enter more details? press /'y/' for yes")
             again_ = input()
             if again_ == 'y':
                 continue
             else:
                 break
        elif access_ == "diet":
             print("you are in \t", client_list[client_], access_, "program")
             f = list_of_diet[client_]
             print("enter diet done by client")
             diet_ = input()
             f.write(diet_)
             print("Do you want to enter more details? press /'y/' for yes")
             again_ = input()
             if again_ == 'y':
                 continue
             else:
                 break
        else:
             print("The program you choose doesn't exist")
             break

health_system()

#         for client_ in access_:
#             print(access_client_)




