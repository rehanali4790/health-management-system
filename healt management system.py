client_list = ["","rehan","ali","samo"]
list_of_excercise = ["",open("rehan ex.txt","a"),open("ali ex.txt","a"),open("samo ex.txt","a")]
list_of_diet = ["",open("rehan.txt","a"),open("ali.txt","a"),open("samo.txt","a")]
# rehan1 = open("rehan.txt")
# rehan2 = open("rehan ex.txt")
# ali1 = open("ali.txt")
# ali2 = open("ali ex.txt")
# samo1 = open("samo.txt")
#samo2 = open("samo ex.txt")
def date_time():
    import datetime
    return datetime.datetime.now()
def health_system():
    """This function manages the data for clients diet and excercise"""
    print("what you wanna enter? excercise or diet?")
    access_ = input()
    print("Which client you want to look in"
          " enter client number, 1 , 2 , 3 for rehan, ali, samo respectively")
    client_ = int(input())
    while client_ != "none":
         if access_ == "excercise":
             print("you are in \t", client_list[client_], access_, "program")
             f = list_of_excercise[client_]
             print("enter excercise done by client")
             excercise = input()
             f.write(date_time()+excercise, end="")
             break
         else:
             print("you are in \t", client_list[client_], access_, "program")
             f = list_of_diet[client_]
             print("enter diet done by client")
             diet_ = input()
             f.write( date_time() + diet_ )
             break

print(health_system.__doc__)

#         for client_ in access_:
#             print(access_client_)




