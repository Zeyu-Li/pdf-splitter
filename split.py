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
    inputs = os.path.join(current_dir, "pdf_input")
    outputs = os.path.join(current_dir, "output")
    # search for those that contain output as start, followed by a series of digits (capture that), followed by .pdf
    # used https://regex101.com/r/TksJPT/1/ for testing purposes
    search = re.compile("^output(\d+)\.pdf$")

    dir_list = os.listdir(outputs)
    dir_list.sort(reverse=True)

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

    splits.sort()

    print(splits)

if __name__ == "__main__":
    main()
