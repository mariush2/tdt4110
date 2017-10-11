#Importing list of saved names
#import fjesboka_list as f
facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"],
                ["Therese", "Johaug", 28, "Female", "Complicated"],
                ["Mark", "Wahlberg", 45, "Male", "Married"],
                ["Siv", "Jensen", 47, "Female", "Single"]]
#given_name surname age gender relationship_status
def add_data(user):
    user = user.split(" ")

    try:
        if(len(user) != 5):
            raise ValueError

        for i in range(0, len(user)):
            user[i] = user[i].title()

        user[2] = int(user[2])
        return user
    except ValueError:
        print("Du skrev inn noe feil!")


def get_person(given_name, facebook):
    result = []
    given_name = given_name.lower()
    for person in facebook:
        if(person[0].lower() == given_name):
            result.append(person)

    return result

#get_person("mark", facebook)
#add_data("meme memeson 23 male rip")

def main():
    while True:
        new_user = input("Add new user: ")
        if(new_user.lower() == "done"):
            print("Ok")
            break

        facebook.append(add_data(new_user))

    while True:
        search_user = input("Search for user: ")
        if(search_user.lower() == "done"):
            print("Ok")
            break

        result = get_person(search_user, facebook)
        if(result == []):
            print("No results!")
        else:
            for i in range(0, len(result)):
                print(result[i][0],result[i][1], "is", result[i][2], "years old. Relationship status is", result[i][4])



main()
