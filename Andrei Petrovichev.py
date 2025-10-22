# A
text = ""
while True:
    print("1. Enter text")
    print("2. Trim edges (strip)")
    print("3. Remove multiple spaces to single")
    print("4. Show length without spaces")
    print("5. Exit")
    choice = input("Choose an option (number): ")
    
    if not choice.isdigit():
        print("Please enter a number")
        continue
    
    choice = int(choice)
    
    if choice == 1:
        text = input("Enter text: ")
    elif choice == 2:
        if text != "":
            text = text.strip()
            print("New text:", text)
        else:
            print("Please enter text first")
    elif choice == 3:
        if text != "":
            while "  " in text:
                text = text.replace("  ", " ")
            print("Text now:", text)
        else:
            print("Please enter text first")
    elif choice == 4:
        if text != "":
            length = len(text.replace(" ", ""))
            print("Length without spaces:", length)
        else:
            print("Please enter text first")
    elif choice == 5:
        print("Good bye!")
        break
    else:
        print("Wrong number")

# B
while True:
    name = input("Enter name: ")
    if len(name) > 12:
        print("Name too long")
        continue
    if len(name) < 4:
        print("Name too short")
        continue
    if " " in name:
        print("Name contains spaces")
        continue
    if not name.isalnum():
        print("Name contains invalid symbols")
        continue
    print("Correct name")
    break

# C
while True:
    fullname = input("Enter name parts (like F/N or F/N/P): ")
    fullname = fullname.strip()
    while "  " in fullname:
        fullname = fullname.replace("  ", " ")
    parts = fullname.split("/")
    if len(parts) < 2:
        print("Enter at least two parts separated by '/'")
        continue
    parts = [part.strip().title() for part in parts]
    if "" in parts:
        print("Parts cannot be empty")
        continue
    print("Normalized:", parts)
    break

# A
text = input("Enter text to clean: ").strip()
cleaned = ""
prev_space = False
for ch in text:
    if ch.isalpha() or ch.isdigit():
        cleaned += ch
        prev_space = False
    elif ch == " " or ch == "\t" or ch == "\n":
        if not prev_space:
            cleaned += " "
            prev_space = True
print("Original:", text)
print("Cleaned:", cleaned)

# B
total = 0
empty = 0
short = 0
while True:
    line = input("Enter a line (empty to stop): ")
    if line == "":
        break
    total += 1
    line_strip = line.strip()
    if line_strip == "":
        empty += 1
    if 0 < len(line_strip) < 5:
        short += 1
print("Total lines:", total)
print("Empty lines:", empty)
print("Short lines (<5 chars):", short)
