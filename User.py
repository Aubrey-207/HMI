import json


if __name__ == '__main__':
    with open("Points.json", "r") as f:
        user_dict = json.load(f)

        print(user_dict)
        print(type(user_dict))

        print(user_dict["axis"])
        print(type(user_dict["axis"]))
        print(len(user_dict["axis"]))

        print(user_dict["axis"][0])
        print(type(user_dict["axis"][0]))

