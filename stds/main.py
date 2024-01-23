# Do not modify these lines
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Add your code after this line

# ===================== START IMPORTS ========================================
import sys # to access standard input, output, and error streams.
# ===================== END IMPORTS ========================================

def main():
    # TODO: read text from stdin
    input_text = sys.stdin.read()
    
    
    # TODO: Filter character given as an argument from the text
    char_to_remove = sys.argv[1]
    # Filter the character from the text
    filtered_text = input_text.replace(char_to_remove, '')

    # TODO: Print the result to stdout
    sys.stdout.write(filtered_text)
    
    
    # TODO: Print the total number of removed characters to stderr
    removed_count = input_text.count(char_to_remove)
    sys.stderr.write(str(removed_count))
    # sys.stderr.write(f"Total of the character '{char_to_remove}' removed: {str(removed_count)}\n")

if __name__ == "__main__":
    main()
