# Author: Savir Singh
# Name: PY TO CPP convert.py
# github.com/savirsingh/pytocpp

extraatend = False

while True:
    in1 = input(".py file which you would like to convert: ")
    if ".py" in in1:
        in2 = input("Add this after each output (leave empty if you want a new line): ")
        print("Thanks, checking...")
        break
    else:
        print("Sorry, we need a .py file")

try:
    f = open(in1, "r")
    print("File Found! Converting to CPP...")

    w = open("template.cpp", "r")
    starter = w.read()
    lines = f.readlines()
    lines.append("\n\n")
    for i in range(len(lines)):
        lines2 = lines.copy()
        if " True" in lines[i] or " False" in lines[i] and "'" not in lines[i] and '"' not in lines[i]:
            lines[i] = lines[i].replace("True", "true")
            lines[i] = lines[i].replace("False", "false")
        if lines[i][0] == "#": lines[i] = "//" + lines[i][1:] # comments support
        if "while " in lines[i] and " while " not in lines[i]:
            line1 = lines[i].replace("while", "").replace(":", "").replace("in", "")
            lines[i] = "while (" + line1 + ") {"
            if "while" in lines[i]:
                for r in range(i, len(lines)):
                    try:
                        if "    " in str(lines[r-1]) and "    " not in str(lines[r]) and "while " not in str(lines[r]) and "while " not in str(lines[r]):
                            lines[r] = "}\n" + lines[r]
                    except:
                        pass
        if "if" in lines[i] and " if " not in lines[i] and "elif " not in lines[i] and "else " not in lines[i]:
            line1 = lines[i].replace("if", "").replace(":", "").replace("in", "")
            lines[i] = "if (" + line1 + ") {"
            if "if" in lines[i]:
                for r in range(i, len(lines)):
                    try:
                        if "    " in str(lines[r-1]) and "    " not in str(lines[r]) and "elif " not in str(lines[r]) and "else " not in str(lines[r]):
                            lines[r] = "}\n" + lines[r]
                    except:
                        pass
        if "elif" in lines[i] and " elif " not in lines[i]:
            line1 = lines[i].replace("elif", "").replace(":", "").replace("in", "")
            lines[i] = "else if (" + line1 + ") {"
            if "elif" in lines[i]:
                for r in range(i, len(lines)):
                    try:
                        if "    " in str(lines[r-1]) and "    " not in str(lines[r]) and "elif " not in str(lines[r]) and "else if " not in str(lines[r]) and "else " not in str(lines[r]):
                            lines[r] = "}\n" + lines[r]
                    except:
                        pass
        if "else" in lines[i] and " else " not in lines[i] and "else if" not in lines[i]:
            line1 = lines[i].replace("else", "").replace(":", "").replace("in", "")
            lines[i] = "else {"
        if "print(" in lines[i]:
            if in2 == "":
                lines[i] = lines[i].replace("print(", "cout << ").replace(")", " << endl;").replace("+", " << ")
            else:
                lines[i] = lines[i].replace("print(", "cout << ").replace(")", " << " + '"' + in2 + '"' + ";").replace("+", " << ")
        if "input()" in lines[i] and "int(input())" not in lines[i]:
            line1 = lines[i].split("=")
            lines[i] = lines[i].replace(lines[i], "string " + line1[0] + ";" + "\n" + "cin >> " + line1[0] + ";")
        if "int(input())" in lines[i]:
            line1 = lines[i].split("=")
            lines[i] = lines[i].replace(lines[i], "int " + line1[0] + ";" + "\n" + "cin >> " + line1[0] + ";")
        if "for" in lines[i] and "range" in lines[i]:
            line1 = ''.join(lines[i].split("for")[1]).replace("in", "").replace(" ", "").replace("(", "").replace(")", "").replace(":", "").replace("\n", "").split("range")
            lines[i] = "for (int " + line1[0] + "=0; " + line1[0] + "<" + line1[1] + "; " + line1[0] + "++) {"
            h = 0
            if "for" in lines[i]:
                for b in range(i+1, len(lines)+1):
                    if h==1:
                        break
                    try:
                        while "  " not in lines[b]:
                            lines[b] = "}\n"+lines[b]
                            h = 1
                            break
                    except:
                        pass
        if "[" in lines[i]:
            line0 = lines[i].split("=")
            line1 = lines[i].split("[")
            line2 = ''.join(line1).replace("]", "").split("=")
            if '"' in line1[1] or "'" in line1[1]:
                lines[i] = "vector<string> " + line0[0] + "={" + line2[1] + "};"
            else:
                lines[i] = "vector<int> " + line0[0] + "={" + line2[1] + "};"
        if "int(" in lines[i] and "input" not in lines[i]:
            lines[i] = lines[i].replace("int", "stoi")
            lines[i] = "int " + lines[i]
            lines[i] = lines[i].replace("\n", "") + ";\n"
        if "str(" in lines[i] and "input" not in lines[i]:
            lines[i] = lines[i].replace("str", "to_string")
            lines[i] = "string " + lines[i]
            lines[i] = lines[i].replace("\n", "") + ";\n"
        if "pass" in lines[i]:
            lines[i] = lines[i].replace("pass", ";")
        elif "=" in lines[i] and "==" not in lines[i] and "for (" not in lines[i] and "cout" not in lines[i]:
            line1 = lines[i].split("=")
            if '+' in line1[1] or '*' in line1[1] or '-' in line1[1] or '/' in line1[1]:
                ab = str(line1[1]).split("\n")
                lines[i] = lines[i].replace(lines[i], "int " + ''.join(line1[0]) + "= " + ''.join(ab) + ';')
            elif ('True' in lines[i] or 'False' in lines[i]) and "'" not in lines[i] and '"' not in lines[i]:
                ab = str(line1[1]).split("\n")
                lines[i] = lines[i].replace(lines[i], "bool " + ''.join(line1[0]) + "= " + ''.join(ab).lower() + ';')
            else:
                try:
                    ab = int(line1[1])
                    lines[i] = lines[i].replace(lines[i], "int " + ''.join(line1[0]) + "= " + str(ab) + ";")
                except:
                    ab = str(line1[1]).split("\n")
                    lines[i] = lines[i].replace(lines[i], "string " + ''.join(line1[0]) + "= " + ''.join(ab) + ';')
        elif "for" in lines[i] and "range" not in lines[i] and "{" not in lines[i]:
            print(lines[i])
            line1 = ''.join(lines[i].split("for")[1]).replace("(", "").replace(")", "").replace(":", "").replace("\n", "").split(" in ")
            if "range" not in line1:
                lines[i] = "for (" + line1[0] + "=" + line1[1] + ".begin(); " + line1[0] + "!=" + line1[1] + ".end(); " + line1[0] + "++) {"
            for c in range(i+1, len(lines)):
                if str(line1[0]).replace(" ", "") in str(lines[c]):
                    lines[c] = lines[c].replace(line1[0], line1[0] + "->name")
                    print("yes")
            h = 0
            if "for" in lines[i]:
                for b in range(i+1, len(lines)+1):
                    if h==1:
                        break
                    try:
                        while "  " not in lines[b]:
                            lines[b] = "}\n"+lines[b]
                            h = 1
                            break
                    except:
                        pass
            
    print("Your file has been converted:")
    print("-------------------------------- \n")
    print(''.join(starter))
    for line in lines:
        print(line)
    print("\n}")
    if extraatend:
        print("\n}")
    print("\n")
    while True:
        in3 = input("Should we save the file as " + in1.replace(".py", ".cpp") + "? (y/n) ")
        if in3 == "y":
            z = open(in1.replace(".py", ".cpp"), "a")
            z.write(''.join(starter))
            for newline in lines:
                z.write(newline)
            z.write("\n}")
            if extraatend:
                z.write("\n}")
            z.close()
            print("\nThe file has been saved as: " + in1.replace(".py", ".cpp"))
            break
        if in3 == "n":
            print("\nAlright, enjoy your day!")
            break
        else:
            print("Select a valid option! (y/n) ")
    
except FileNotFoundError:
    print("Oops, that file doesn't exist. Maybe check again and re-run the program?")

