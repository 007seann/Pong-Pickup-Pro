import os

# Path to the folder containing the text files
folder_path = "/Users/apple/Library/Mobile Documents/com~apple~CloudDocs/Year 3/SDP/dataset/Table Tennis.v1i.yolov5pytorch/valid/labels"

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Skip non-text files
    if not filename.endswith(".txt"):
        continue

    # Construct the full path to the file
    file_path = os.path.join(folder_path, filename)

    # Open the file for reading
    with open(file_path, "r") as file:
        # Read the contents of the file line by line
        lines = file.readlines()

    # Filter out the lines that start with "1"
    filtered_lines = [line for line in lines if not line.startswith("1")]

    # Open the file for writing
    with open(file_path, "w") as file:
        # Write the filtered lines back to the file
        for line in filtered_lines:
            file.write(line)
