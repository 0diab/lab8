print("[Friend List]\n")

friends = []
q = 1
while q:
    print("1 - Add friend")
    print("2 - List friends")
    print("3 - Quit")
    operation = int(input("Make your selection: "))
    print()
    match operation:
        case 1:
            name = input("Enter your friend's name: ")
            age = input("Enter your friend's age: ")
            friends.append((name,age))
            print("Friend added\n")
        case 2:
            for i in range(len(friends)):
                print(f"Name: {friends[i][0]} Age: {friends[i][1]}")
        case 3:
            q = 0

print("Shutting down...")

