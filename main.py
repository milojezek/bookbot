def main():
  path_to_file = "books/frankenstein.txt"
  printReport(path_to_file)


def printReport(book_path):
  with open(book_path) as f:
    file_contents = f.read()
  word_count = countWords(file_contents)
  letter_dict = countLetters(file_contents)
  sorted_letter_count = sorted(
    letter_dict.items(),
    key = lambda x:x[1],
    reverse = True
  )

  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document\n")

  for letter in sorted_letter_count:
    print(f"The {letter[0]} character was found {letter[1]} times")

  print("--- End report ---")


def countWords(text):
  words = text.split()
  return len(words)

def countLetters(text):
  letter_dict = {}

  lower_text = text.lower()

  # Remove special characters
  for ch in ['\\','`','*','_','{','}','[',']',
             '(',')','>','#','+','-','.','!','$',
             '\'', '/', '%', '@', ':', '?', ',', '"', ';', ' ']:
        if ch in lower_text:
            lower_text = lower_text.replace(ch, "")
  letters_numbers_only = lower_text.replace("\n", "")

  # Remove numbers
  for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
     if n in letters_numbers_only:
        letters_numbers_only = letters_numbers_only.replace(n, "")
        
  letters_only = letters_numbers_only
  for char in letters_only:
    if char in letter_dict:
      letter_dict[char] += 1
    else:
      letter_dict[char] = 1

  return letter_dict


if __name__ == "__main__":
  main()
