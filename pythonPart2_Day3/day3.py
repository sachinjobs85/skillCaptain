with open("file.txt", "r") as file:
    lines = []
    for line in file:
        lines.append(line.strip())
    print(lines)

    my_lines = iter(lines)

    print(next(my_lines))
    print(next(my_lines))
    print(next(my_lines))
    print(next(my_lines))
