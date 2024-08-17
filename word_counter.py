def main():
    print("Word Counter Program")
    print("--------------------")

    try:
        text = input("Enter a text: ")
    except Exception as e:
        print(f"Error: {e}")
        return

    if not text.strip().replace(" ", ""):
        print("Error: Empty input. Please enter some text.")
        return

    word_count = len(text.split())
    print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()