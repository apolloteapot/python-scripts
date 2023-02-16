import os

for root, dirs, files in os.walk('./'):

    for filename in files:

        filename_no_ext = os.path.splitext(filename)[0]

        with open('output.txt', 'a', encoding = 'utf-8') as f:
            f.write(filename_no_ext + '\n')