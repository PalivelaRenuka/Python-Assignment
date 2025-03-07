# Writing text to a file using input()
file_name = "output.txt"
with open(file_name, "w") as file:
    text = input("Enter text to write to file: ")
    file.write(text)

print(f"Text successfully written to {file_name}")