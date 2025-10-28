ignore_words = {'of', 'and', 'the', 'in', 'on', 'at', 'for', 'with', 'a', 'an'}
while True:
    text = input("Enter a phrase (or type 'stop' to end): ").strip()
    if text.lower() == "stop":
        print("Thank you for using")
        break
    if not text:
        print("Please enter a valid phrase.\n")
        continue
    words = [word for word in text.split() if word.lower() not in ignore_words]
    acronym = "".join(word[0].upper() for word in words)
    print("The acronym is:", acronym, "\n")
