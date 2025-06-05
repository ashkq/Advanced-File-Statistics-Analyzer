from collections import Counter
import os

def file_stats(in_file, encoding='utf-8'):
    try:
        open_file = open(in_file, 'r', encoding=encoding)
        lines = 0
        words = 0
        characters = 0
        blank_lines = 0
        longest_line_length = 0
        shortest_line_length = float('inf')
        total_line_length = 0
        total_word_length = 0
        alpha_words = 0
        numeric_words = 0
        special_char_lines = 0
        word_counter = Counter()
        line_lengths = []

        for current_line in open_file:
            lines += 1
            characters += len(current_line)
            line_length = len(current_line.strip())
            line_lengths.append(line_length)
            total_line_length += line_length
            longest_line_length = max(longest_line_length, line_length)
            if line_length < shortest_line_length and line_length > 0:
                shortest_line_length = line_length
            if not current_line.strip():
                blank_lines += 1
            if any(not c.isalnum() and not c.isspace() for c in current_line):
                special_char_lines += 1
            words_list = current_line.strip().split()
            words += len(words_list)
            word_counter.update(words_list)
            for word in words_list:
                total_word_length += len(word)
                if word.isalpha():
                    alpha_words += 1
                elif word.isnumeric():
                    numeric_words += 1

        avg_word_length = total_word_length / words if words else 0
        avg_line_length = total_line_length / lines if lines else 0
        top_words = word_counter.most_common(10)

        print("Lines:", lines)
        print("Blank Lines:", blank_lines)
        print("Words:", words)
        print("Alphabetic Words:", alpha_words)
        print("Numeric Words:", numeric_words)
        print("Characters:", characters)
        print("Longest Line Length:", longest_line_length)
        print("Shortest Line Length:", shortest_line_length if shortest_line_length != float('inf') else 0)
        print("Lines with Special Characters:", special_char_lines)
        print(f"Average Word Length: {avg_word_length:.2f}")
        print(f"Average Line Length: {avg_line_length:.2f}")
        print("Top 10 Most Common Words:", top_words)

        open_file.close()

    except FileNotFoundError:
        print(f"Error: File '{in_file}' not found.")
    except UnicodeDecodeError:
        print("Error: Unable to decode file. Try using a different encoding.")
