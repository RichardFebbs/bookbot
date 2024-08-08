def main():
    file_contents = get_file_contents()
    word_count = len(file_contents.split())
    char_count = count_characters(file_contents)
    letters_dict = [{"letter":x, "count":y} for x, y in char_count.items()]
    letters_dict.sort(reverse=True, key=lambda x: x["count"])

    generate_report(letters_dict, word_count)

def get_file_contents():
    with open("frankenstein.txt", "r") as f:
        return f.read()

def count_characters(s: str) -> dict:
    count_dict = {}
    for char in s.lower():
        if char in count_dict:
            count_dict[char] += 1
        elif char.isalpha():
            count_dict[char] = 1
    return count_dict

def generate_report(char_list, word_count):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n\n")

    for item in char_list:
        print(f"The '{item['letter']}' was found {item['count']} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()
