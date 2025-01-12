#instrutions
#Create a program that reads a file and writes a modified version to a new file

def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()
        
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File '{input_filename}' has been read and modified content written to '{output_filename}'")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{input_filename}'.")

# Ask the user for the filenames
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the file to write the modified content to: ")

# Call the function
read_and_modify_file(input_filename, output_filename)
