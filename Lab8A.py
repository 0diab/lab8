print("[Mailing List]\n")
q = 1
mailingList = []
while q :
    print("1 - Add email")
    print("2 - Delete email")
    print("3 - List all emails")
    print("4 - Quit")
    operation = int(input("Make your selection: "))
    print()
    match operation:
        case 1:
            email = input("Enter the email to be added: ")
            mailingList.append(email)
        case 2:
            email = input("Enter the email to be removed: ")
            if email in mailingList:
                mailingList.remove(email)
                print(f"{email} has been removed from the mailing list.")
            else:
                print(f"No such email in mailing list: {email}")
        case 3:
            for i in mailingList:
                print(i)
        case 4:
            q = 0
    print()
print("Shutting down...")