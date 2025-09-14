import sys
from stats import get_num_words
from stats import get_stats
from stats import sort_dict


def get_book_text(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None


def main():
    arg_list = sys.argv
    if len(arg_list) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {arg_list[1]}...")

    book_text = get_book_text(arg_list[1])
    if book_text is None:
        print("Cannot proceed without book text.")
        return

    word_count = get_num_words(book_text)
    if word_count:
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")

    stats = get_stats(book_text)
    if stats:
        output = sort_dict(stats)

        if output:
            print("--------- Character Count -------")
            for dict in output:
                char = dict["char"]
                num = dict["num"]

                # if char.isalpha():
                print(f"{char}: {num}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
