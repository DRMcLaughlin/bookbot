import sys
from stats import get_word_count, formatted_output

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
header1 = ("=")
header2 = ("-")
word_count = get_word_count(path)
print(f"{header1 * 12} BOOKBOT {header1 * 12}")
print(f"Analyzing book found at {path}...")
print(f"{header2 * 10} Word Count {header2 * 10}")
print(f"Found {word_count} total words")
print(f"{header2 * 9} Character Count {header2 * 5}")
print(formatted_output(path))
print(f"{header1 * 12} END {header1 * 12}")
