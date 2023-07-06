def file_stats(in_file):
    open_file = open(in_file)
    lines = 0
    words = 0
    characters = 0

    for current_line in open_file:
        lines += 1
        words_list = current_line.split()
        words += len(words_list)
        characters += len(current_line)

    print("Lines:", lines)
    print("Words:", words)
    print("Characters:", characters)

    open_file.close()
