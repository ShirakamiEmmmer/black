# -*- coding: utf-8 -*

black = []
black_file = open("black.txt", "r")
for line in black_file:
    line = line.split()
    black.append(line[0])
black_file.close()

file = open("confirm_list.txt", "a")

for man in black:
    print(man)
    file.writelines(str(man) + "\n")
    danmaku_file = open("file.txt", "r")
    for line in danmaku_file:
        array = line.split(":", 2)
        if int(array[1]) == int(man):
            puts = array[2].split()[0]
            print(puts)
            file.writelines(puts + "\n")
    print("")
    file.writelines("\n")
    danmaku_file.close()
print("over")
file.close()