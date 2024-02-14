print("Interface Status")
print("=" * 120)
print("DN                                         Description           Speed     MTU    TimeStamp                      ID")
print("-----------------------------------------  --------------------  -------   -----  -----------------------------  --------")
y = json.loads(x)
interface = y["imdata"]
n = 0
for i in interface:
    if n in range(4, 13):
        print(i["l1PhysIf"]["attributes"]["dn"], end = "")
        print(" " * 24, end = '')
        print(i["l1PhysIf"]["attributes"]["speed"], end = "")
        print(" " * 3, end = "")
        print(i["l1PhysIf"]["attributes"]["mtu"], end = "")
        print(" " * 3, end = "")
        print(i["l1PhysIf"]["attributes"]["modTs"], end = "")
        print(" " * 2, end = "")
        print(i["l1PhysIf"]["attributes"]["id"], end = "")
        print("\n", end = "")
        n += 1
        continue
    n += 1 
    print(i["l1PhysIf"]["attributes"]["dn"], end = "")
    print(" " * 23, end = '')
    print(i["l1PhysIf"]["attributes"]["speed"], end = "")
    print(" " * 3, end = "")
    print(i["l1PhysIf"]["attributes"]["mtu"], end = "")
    print(" " * 3, end = "")
    print(i["l1PhysIf"]["attributes"]["modTs"], end = "")
    print(" " * 2, end = "")
    print(i["l1PhysIf"]["attributes"]["id"], end = "")
    print("\n", end = "")

