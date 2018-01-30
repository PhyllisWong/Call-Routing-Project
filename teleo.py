import os


'''
Normalized numbers examples: US +12223334444, Japan +81223334444, UK +4422233334444.
Routes: path through a carriers phone network. When finding a route to use in a single carrier's
route list, the longest matching prefix must be used. Choose the cheapest route when there are multiple carriers.
'''


def read_routes(phone):
    found = False
    with open("route-costs-106000.txt", "r") as f:
        for line in f:
            line = line.rstrip('\n')
            if phone == line:
                print(line)
                found = True
                break
    if not found:
        print("Nothing found")



def read_one_num():
    with open("phone-numbers-3.txt", "r") as f:
        phone = f.readline()
        return phone


if __name__ == "__main__":
    phone = read_one_num()
    read_routes(phone)
