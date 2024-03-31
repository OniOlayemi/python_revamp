def changesentence(sentence):
    count = 0
    result = ''
    length = len(sentence)

    for i in range(length):
        try:
            v = int(sentence[i])
            exit("An integer should be a part")
        except ValueError:
            if count == 0:
                result += sentence[i]
                count += 1

            elif sentence[i] == " ":
                if sentence[i - 1] == " ":
                    exit("two spaces should not follow each other")
                else:
                    count = 0
                    result += " "

            else:
                if sentence[i].lower() > sentence[i - 1].lower():
                    result += sentence[i].upper()
                    count += 1
                else:
                    result += sentence[i]
                    count += 1

    print(result)


changesentence("we are The world,juic abc")
