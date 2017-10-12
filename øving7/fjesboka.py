#Importing list of saved names
import os
import json
from dotmap import DotMap

facebook = []

def get_info(facebook):
    try:
        __location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))

        config = open(os.path.join(__location__, "full_list.json"), "r")
        config = json.load(config)
        people = DotMap(config)
        for person in people.items():
            person = person[1]
            new_person = {}
            new_person["given_name"] = person.given_name
            new_person["surname"] = person.surname
            new_person["age"] = person.age
            new_person["gender"] = person.gender
            new_person["relationship_status"] = person.relationship_status
            facebook.append(new_person)
    except FileNotFoundError:
        print("File not found!")
        exit(1)


#given_name surname age gender relationship_status
def add_data(user):
    user = user.split(" ")

    try:
        if(len(user) != 5):
            raise ValueError

        for i in range(0, len(user)):
            user[i] = user[i].title()

        user[2] = int(user[2])

        result = {}
        result["given_name"] = user[0]
        result["surname"] = user[1]
        result["age"] = user[2]
        result["gender"] = user[3]
        result["relationship_status"] = user[4]
        return result
    except ValueError:
        print("Du skrev inn noe feil!")


def get_person(given_name, facebook):
    result = []
    given_name = given_name.lower()
    for person in facebook:
        if(person["given_name"].lower() == given_name):
            result.append(person)

    return result


def main():
    get_info(facebook)
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
            exit_main(facebook)
            break

        result = get_person(search_user, facebook)
        if(result == []):
            print("No results!")
        else:
            for i in range(0, len(result)):
                print(result[i]["given_name"],result[i]["surname"], "is", result[i]["age"], "years old. Relationship status is", result[i]["relationship_status"])


def exit_main(facebook):
    __location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
    outfile = open(os.path.join(__location__, "full_list.json"), "w")
    i = 0
    for person in facebook:
        output = json.dump({"person" + str(i): person}, outfile)
        i += 1


main()
