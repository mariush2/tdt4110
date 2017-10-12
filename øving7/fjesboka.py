#Importing list of saved names
import os
import json
from dotmap import DotMap

facebook = {}

def get_info(facebook):
    try:
        __location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))

        config = open(os.path.join(__location__, "full_list.json"), "r")
        config = json.load(config)
        full_list = DotMap(config)
        i = 0
        for person in full_list.people.items():
            person = person[1]
            new_person = {}
            new_person["given_name"] = person.given_name
            new_person["surname"] = person.surname
            new_person["age"] = person.age
            new_person["gender"] = person.gender
            new_person["relationship_status"] = person.relationship_status
            facebook["person" + str(i)] = new_person
            i += 1
    except FileNotFoundError:
        print("File not found!")
        exit(1)


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
    for person in facebook.items():
        person = person[1]
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

        facebook["person" + str(len(facebook))] = (add_data(new_user))

    while True:
        search_user = input("Search for user: ")
        if(search_user.lower() == "done"):
            print("Ok")
            save_list(facebook)
            break

        result = get_person(search_user, facebook)
        if(result == []):
            print("No results!")
        else:
            for i in range(0, len(result)):
                print(result[i]["given_name"],result[i]["surname"], "is", result[i]["age"], "years old. Relationship status is", result[i]["relationship_status"])


def save_list(facebook):
    __location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
    outfile = open(os.path.join(__location__, "full_list.json"), "w")
    output = json.dump({"people": facebook}, outfile, indent=0, check_circular=False)


main()
