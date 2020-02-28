def valid_phone_number():
    with open ("/Users/home/github/Atom/Python/Leetcode/file.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            # print(line)
            if "-" not in line:
                if "(" and ")" not in line:
                    continue
            else:
                if line.count("-") != 2:
                    if "(" and ")" not in line:
                        continue
                    if line.index(")") < line.index("("):
                        continue
                    if line.index("(") < line.index("-")<line.index(")"):
                        continue
                print(line)

            '''
            if "-" and "(" and ")" not in line:
                continue
            elif "(" and ")" not in line:
                continue
            elif "-" not in line:
                continue
            else:
                print(line)
            '''
            '''
            for i in line:
                if ord(i) == 32:
                    break
            else:
                print(line)
            '''
valid_phone_number()
