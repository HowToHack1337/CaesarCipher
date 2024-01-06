def print_banner():
    banner = """
 +-+-+-+-+-+-+-+-+-+-+-+-+
 |C|a|e|s|a|r|C|i|p|h|e|r|
 +-+-+-+-+-+-+-+-+-+-+-+-+\\
"""
    print(banner)

def caesar_cipher(text, shift, option):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine whether to encrypt or decrypt based on the option
            if option.lower() == 'encrypt':
                result += chr((ord(char) + shift - ord('A')) % 26 + ord('A') if char.isupper() else
                              (ord(char) + shift - ord('a')) % 26 + ord('a'))
            elif option.lower() == 'decrypt':
                result += chr((ord(char) - shift - ord('A')) % 26 + ord('A') if char.isupper() else
                              (ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            result += char

    return result

def main():
    print_banner()

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    option = input("Enter 'encrypt' or 'decrypt': ")

    result = caesar_cipher(text, shift, option)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
