hosts0 = open("duplicated.txt","r")
hosts1 = open("ori.txt","r")

lines1 = hosts0.readlines()

for i,lines2 in enumerate(hosts1):
    if lines2 != lines1[i]:
        print("line ", i, " in hosts1 is different")
        print(lines2)
    else:
        print("same")
