# Part 8 — File Handling
filename = 'sample_file.txt'

# Create and write
with open(filename, 'w') as f:
    f.write('This is a sample file.\n')

# Read content
with open(filename, 'r') as f:
    print('Read content:')
    print(f.read())

# Append data
with open(filename, 'a') as f:
    f.write('Appended line.\n')

print('After append:')
with open(filename, 'r') as f:
    print(f.read())
