## 📄 File Statistics Function – Detailed Breakdown
### 📊 Visual Overview

![File Statistics Function Visual](file-stats-visual.png)

The function initiates by invoking the `open()` built-in method to instantiate a file object from the path provided via the `in_file` parameter, subsequently binding this object to the `open_file` identifier for stream manipulation. It proceeds to declare and zero-initialize three accumulator variables — `lines`, `words`, and `characters` — which serve as statistical counters for:

- Line count
- Lexical token count
- Character cardinality

---

### 🔁 Iteration Logic

The primary processing phase leverages an implicit iterator over the `open_file` object, enabling sequential access to each textual line in a memory-efficient manner. For each `current_line`, the function executes the following operations:

- **Line Counting:**  
  `lines` is incremented to reflect the cumulative tally of newline-delimited segments.

- **Word Tokenization:**  
  The line is tokenized via `.split()` (whitespace by default), and the resulting list (`words_list`) is used to increment `words` based on its length.

- **Character Accumulation:**  
  `characters` is incremented by the length of `current_line`, accounting for all characters including whitespace and newline escapes (`\n`).

---

### 📊 Output & Cleanup

Upon completion of the input stream traversal, the function outputs a formatted summary of the derived metrics:

- Total lines processed
- Total words parsed
- Cumulative character count

Finally, the file stream is closed using `.close()` to ensure proper resource deallocation and prevent file descriptor leakage.

---

### ✅ Summary

This function performs a comprehensive textual analysis of the input file, generating essential statistics on its structural and lexical composition.
