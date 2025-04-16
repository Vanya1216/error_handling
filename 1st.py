try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        # Read and print each line
        for line in file:
            print(line.strip())  # Remove any trailing newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found. Please check the file name and location.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")