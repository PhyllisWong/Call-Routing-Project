from pathlib import Path
# doesn't seem to be working yet
routes = Path('route-costs-106000.txt')
nums = Path('phone-numbers-3.txt')

'''
Normalized numbers examples: US +12223334444, Japan +81223334444, UK +4422233334444.
Routes: path through a carriers phone network. When finding a route to use in a single carrier's
route list, the longest matching prefix must be used. Choose the cheapest route when there are multiple carriers.
'''
def read_one_num():
    with open(nums, "r") as f:
        phone = f.readline()
        ph = phone.rstrip('\n')
        return ph


def make_dictionary_from_file():
    routes_dict = {}
    with open(routes, "r") as f:
        for line in f:
            line = line.rstrip('\n')
            route = line.split(',')
            routes_dict[route[0]] = route[1]
    # print(routes_dict)
    return routes_dict


def search_routes(routes_dict, phone):
    ph_str = str(phone)
    print(ph_str)
    found = False
    n = len(ph_str)

    while len(ph_str) > 0:
        ph_str = ph_str[:n]
        print('Updated phone: {}'.format(ph_str[:n]))
        if ph_str in routes_dict:
            print('FOUND IT!')
            found = True
            return routes_dict[ph_str]
        else:
            n -= 1

    #     with open("route-costs-1.txt", "w") as result:
    #         result.write("{}\n".format(low_cost))
    #         result.close()
    # if not found:
    #     print("Nothing found")


if __name__ == "__main__":
    routes_dict = make_dictionary_from_file()
    phone = read_one_num()
    search_routes(routes_dict, phone)

    # read_routes(phone)
