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
            new_person["forname"] = person.forname
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
        result["forname"] = user[0]
        result["surname"] = user[1]
        result["age"] = user[2]
        result["gender"] = user[3]
        result["relationship_status"] = user[4]
        return result
    except ValueError:
        print("You wrote something wrong!")


def delete(user):
    global facebook
    try:
        result = get_person(user, facebook)
        if(len(result) <= 0):
            print("There is no person named", user, "on facebook.")
        else:
            #Show result and ask to delete each one (y/n)
            delete = []
            for person in result:
                print("'"+ str(person["forname"]), person["surname"], person["age"], person["gender"], person["relationship_status"], "'is selected")
                check = input("Delete?(y/n) ").lower()
                if(check == "y"):
                    delete.append(person)

            for delete_num in delete:
                for person in facebook:
                    if(facebook[person]["forname"] == delete_num["forname"] and facebook[person]["surname"] == delete_num["surname"]):
                        print("Deleted", delete_num["forname"], delete_num["surname"], "from facebook.")
                        del facebook[person]
                        break

            i = 0
            newList = {}
            for person in facebook:
                newPerson = {}
                newPerson["forname"] = facebook[person]["forname"]
                newPerson["surname"] = facebook[person]["surname"]
                newPerson["age"] = facebook[person]["age"]
                newPerson["gender"] = facebook[person]["gender"]
                newPerson["relationship_status"] = facebook[person]["relationship_status"]

                newList["person" + str(i)] = newPerson
                i += 1

            facebook = newList
            print("Done deleting.")
    except ValueError:
        print("You wrote something wrong!")


def get_person(given_name, facebook):
    result = []
    given_name = given_name.lower()
    for person in facebook.items():
        person = person[1]
        name = person["forname"].lower()
        if(name == given_name):
            result.append(person)

    return result


def main():
    get_info(facebook)
    print("Welcome to FB in python!\nRemember to use this syntax for adding new people:\n'forname surname age gender relationshipstatus'")

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
            break

        result = get_person(search_user, facebook)
        if(result == []):
            print("No results!")
        else:
            for i in range(0, len(result)):
                print(result[i]["forname"],result[i]["surname"], "is", result[i]["age"], "years old. Relationship status is", result[i]["relationship_status"])

    while True:
        delete_user = input("Delete user: ")
        if(delete_user.lower() == "done"):
            print("Ok")
            save_list(facebook)
            break

        delete(delete_user)

def save_list(facebook):
    __location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
    outfile = open(os.path.join(__location__, "full_list.json"), "w")
    output = json.dump({"people": facebook}, outfile, indent=0, check_circular=False)


main()
