from pathlib import Path
# raw_file = Path(“pages.txt”)


'''
Normalized numbers examples: US +12223334444, Japan +81223334444, UK +4422233334444.
Routes: path through a carriers phone network. When finding a route to use in a single carrier's
route list, the longest matching prefix must be used. Choose the cheapest route when there are multiple carriers.
'''


def read_routes(phone):
    matches = []
    found = False
    with open("route-costs-106000.txt", "r") as f:
        for line in f:
            line = line.rstrip('\n')
            route = line.split(",")
            # print(route[0][:4])
            if route[0][:4] == phone[:4]:
                # print(route[0][:4])
                found = True
                line = ','.join(route)
                matches.append(line)
        # print(matches)
        lowest = matches[0]
        for item in matches:
            item.split(',')
            if item[1] < lowest.split(',')[1]:
                lowest = item

        low_cost = ''.join(lowest)
        print(low_cost)
        with open("route-costs-1.txt", "w") as result:
            result.write("{}\n".format(low_cost))
            result.close()
    if not found:
        print("Nothing found")


def read_one_num():
    with open("phone-numbers-3.txt", "r") as f:
        phone = f.readline()
        return phone


if __name__ == "__main__":
    phone = read_one_num()
    cost = read_routes(phone)
