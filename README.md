# File-Statistics-Calculator
1. The function opens the input file specified by in_file using the open() function and assigns it to the open_file variable.
2. It initializes three variables: lines, words, and characters to 0. These variables will keep track of the statistics of the file.
3. The code then enters a loop that iterates over each line in the input file (open_file). For each line, it performs the following operations:
   - It increments the lines variable by 1 to count the number of lines in the file.
   - It splits the current_line into a list of words using the split() method and assigns it to the words_list variable.
   - It increments the words variable by the length of words_list, which represents the number of words in the current line.
   - It increments the characters variable by the length of current_line, which represents the number of characters in the current line, including spaces and newline characters.
4. After processing all the lines in the input file, the function prints the statistics. It displays the number of lines, the total number of words, and the total number of characters.
5. Finally, the function closes the input file using the close() method to release the resources.

In summary, this code calculates and prints the statistics of a file, including the number of lines, the total number of words, and the total number of characters in the file.
