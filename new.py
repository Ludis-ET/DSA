guest = input()
host = input()
letters = input()

guest = guest.strip()
host = host.strip()
letters = letters.strip()


if len(set(guest + host)) == len(set(letters)):
    for letter in set(guest + host):
        if guest.count(letter) + host.count(letter) != letters.count(letter):
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")