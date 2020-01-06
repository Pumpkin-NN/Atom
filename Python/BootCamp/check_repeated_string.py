def Repeated_Substring_Pattern(string):
    Set = []
    for i in range(len(string)):
        for m in range(len(string)):
            if string[i:m] == '' or string[i:m] in Set:
                continue
            Set.append(string[i:m])
    return Set

if __name__ == "__main__":
    string = 'fwefwefwdacerg2rg'
    stored_string = Repeated_Substring_Pattern(string)

    for i in stored_string:
        if string.count(i) == 1:
            continue
        else:
            print("The string is: {}, and the occur times are {}".format(i,string.count(i)))

'''
# Method Two
def Repeated_Substring_Pattern(string):
    Set = []
    for i in range(len(string)):
        for m in range(len(string)):
            if string[i:m] == '' or string[i:m] in Set:
                continue
            Set.append(string[i:m])
#     print(Set)

    repeated_substring = []
    for ele in Set:
        count = string.count(ele)
        if count != 1:
            repeated_substring.append(ele)
            repeated_substring.append(count)
        else:
            continue
    return repeated_substring

if __name__== "__main__":
    # Sample 1
    string1 = "abcabcabcdessdefs"
    count1 = Repeated_Substring_Pattern(string1)
    print(count1)

    print("\n\n")

    # Sample 2
    string2 = "abcaabcaabcadesscadessdefs"
    count2 = Repeated_Substring_Pattern(string2)
    print(count2)

    print("\n\n")

    # Sample 3
    string3 = "bcabcabcdessdefs"
    count3 = Repeated_Substring_Pattern(string3)
    print(count3)

    print("\n\n")

    # Sample 4
    string4 = "bcabcabcadessdefs"
    count4 = Repeated_Substring_Pattern(string4)
    print(count4)
    
    print("\n\n")

    # Sample 5
    string5 = "abcabcabcadessdefs"
    count5 = Repeated_Substring_Pattern(string5)
    print(count5)

'''
