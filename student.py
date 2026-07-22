while True:
    choose = int(input("choose your option : 1.append data, 2.read file, 3.write file, 4.Exit : "))
    if choose == 1:
        while True:
            name = input("name :")
            num = input("roll no :")
            dept = input("dept :")
            score = input("score :")
            file = open("student.txt","a")
            file.write("\n\n")
            file.write("name :"+name)
            file.write("\n")
            file.write("roll no :"+num)
            file.write("\n")
            file.write("dept :"+dept)
            file.write("\n")
            file.write("score :"+score)
            file.close()
            w = input("want to add more(y/n) ")
            if w=="y":
                continue
            else:
                break
    elif choose == 2:
        file = open("student.txt", "r")
        print(file.read())
        file.close()
    elif choose == 3:
        while True:
            name = input("name :")
            num = input("roll no :")
            dept = input("dept :")
            score = input("score :")
            file = open("student.txt","w")
            file.write("\n\n")
            file.write("name :"+name)
            file.write("\n")
            file.write("roll no :"+num)
            file.write("\n")
            file.write("dept :"+dept)
            file.write("\n")
            file.write("score :"+score)
            file.close()
            w = input("want to add more(y/n) ")
            if w=="y":
                name = input("name :")
                num = input("roll no :")
                dept = input("dept :")
                score = input("score :")
                file = open("student.txt","a")
                file.write("\n\n")
                file.write("name :"+name)
                file.write("\n")
                file.write("roll no :"+num)
                file.write("\n")
                file.write("dept :"+dept)
                file.write("\n")
                file.write("score :"+score)
                file.close()
                break
            else:
                break
    else:
        print("out of state")
        break
