def pattern_recognizer(lst):
    l = len(lst)

    for pr in range(1, l // 2 + 1):
        p = lst[:pr]
        np = l // pr
        repeated_list = p * np

        if repeated_list == lst:
            print("Pattern Found: ", p)
            print("Number of times the pattern repeats: ", np)
            return

    print("Pattern Not Found")

input_str = input("Enter the list elements: ")
input_list = [int(item) for item in input_str.split(",")]
pattern_recognizer(input_list)