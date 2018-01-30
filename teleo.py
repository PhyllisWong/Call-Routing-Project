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
            line.split(",")
            if line[0] in phone:

                found = True
                line = ''.join(line)
                print(line)
            with open("route-costs-1.txt", "w") as result:
                result.write("{}\n".format(line))
                result.close()
                break
    if not found:
        print("Nothing found")


def read_one_num():
    with open("phone-numbers-3.txt", "r") as f:
        phone = f.readline()
        return phone


if __name__ == "__main__":
    phone = read_one_num()
    cost = read_routes(phone)
