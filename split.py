'''
PDF Spliter by Andrew Li
Description: splits the pdf given the page numbers
'''
import os
import sys
import re
from PyPDF2 import PdfFileReader, PdfFileWriter


def main():
    
    # check input and output folders
    if not os.path.exists('output'):
        os.makedirs('output')

    if not os.path.exists('input'):
        os.makedirs('input')
        print("put pdf in the new pdf_input folder please")
        return 0

    current_dir = os.path.dirname(os.path.realpath(__file__))
    inputs = os.path.join(current_dir, "input")
    outputs = os.path.join(current_dir, "output")

    dir_list = os.listdir(inputs)
    # only splits first file
    input_file = dir_list[0]
    if input_file == '.gitkeep':
        input_file = dir_list[1]

    # tests
    # print(input_file)
    # print(sys.argv)

    splits = []

    if len(sys.argv) == 1:
        # ask for args to split
        nums = input('Split page numbers (space separated): ')
        splits = list(map(int, nums.split(' ')))
    else:
        # take args from command args
        for i in range(len(sys.argv)):
            if i == 0:
                continue
            splits.append(int(sys.argv[i]))

    # sort list
    splits.sort()

    with open(f"input/{input_file}", 'rb') as fp:
        reader = PdfFileReader(fp)

        page = 0
        total_page_count = reader.getNumPages()
        writer = PdfFileWriter()
        output_num = 0
        while page != total_page_count:
            writer.addPage(reader.getPage(page))
            page+=1
            # if page is found in split, make a new file
            if page in splits:
                with open(f'output/output{output_num}.pdf', 'wb') as outfile:
                    writer.write(outfile)
                writer = PdfFileWriter()
                output_num+=1


if __name__ == "__main__":
    main()
