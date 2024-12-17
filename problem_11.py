import re
def decode_filename(filename: str) -> str:
    # Start of the string ^ 
        # - Find One or More digits (0-9)
        # - And end with a _
        # "2023122512345678"
    digits = r"^([0-9]+)_"

    # Find a dot literally at any part of the string
        # - Find any literal from a-z & A-Z
        # - End with a dot literraly
        # "png"
    file_format = r"\.([a-zA-Z]+)\."

    # Find a _ literally at any part of the string
        # - Find any literal from a-z,A-Z & _ -
        # - End with a dot literraly
        # "sleighDesign"
    file_name = r"\_([a-zA-Z_-]+)\."
    
    digits_match = re.search(digits, filename)
    file_format_match = re.search(file_format, filename)
    file_name_match = re.search(file_name, filename)

    # Return the file_name + file_format, digits are not needed
    return f"{file_name_match.group(1)}.{file_format_match.group(1)}"

    


result = decode_filename('2023122512345678_sleighDesign.png.grinchwa')
print(result)
# // ➞ "sleighDesign.png" """
print("    ")
result = decode_filename('42_chimney_dimensions.pdf.hack2023')
print(result)
print("     ")
#// ➞ "chimney_dimensions.pdf"
result = decode_filename('987654321_elf-roster.csv.tempfile')
print(result)
#// ➞ "elf-roster.csv"




