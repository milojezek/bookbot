def main():
  path_to_file = "books/frankenstein.txt"
  with open(path_to_file) as f:
    file_contents = f.read()
  print(countLetters(file_contents))

def countWords(text):
  words = text.split()
  return len(words)

def countLetters(text):
  letter_dict = {}

  lower_text = text.lower()
  for ch in ['\\','`','*','_','{','}','[',']','(',')','>','#','+',
             '-','.','!','$','\'', '/', '%', '@', ':', '?', ',', '"', ';', ' ']:
        if ch in lower_text:
            lower_text = lower_text.replace(ch, "")
  lower_text = lower_text.replace("\n", "")
  letters_numbers_only = lower_text
  for char in letters_numbers_only:
    if char in letter_dict:
      letter_dict[char] += 1
    else:
      letter_dict[char] = 1

  return letter_dict


if __name__ == "__main__":
  main()
