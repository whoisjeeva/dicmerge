#!/usr/bin/env python
# dicmerge.py

"""
Copyright (C) 2017 Jeevakumar (anymsjeeva@gmail.com)
See License at codingpin.com (https://codingpin.com/dicmergeproject)
  _____  _      __  __                     
 |  __ \(_)    |  \/  |                    
 | |  | |_  ___| \  / | ___ _ __ __ _  ___ 
 | |  | | |/ __| |\/| |/ _ \ '__/ _` |/ _ \
 | |__| | | (__| |  | |  __/ | | (_| |  __/
 |_____/|_|\___|_|  |_|\___|_|  \__, |\___|
                                 __/ |     
              Created by anyms  |___/      
"""

import os, sys, time, platform, color as c, argparse, zipfile

def main():
    global color
    color = c.Color()
    args = setArguments()
    if (args.o == None):
        print(parser.print_help())
        exit(0)

    displayLogo()
    words = combineWordlist(args.files)
    generate(words, args.o)
    if (args.compress == '1'):
        compress(args.o)
  

def displayLogo():      
    logo = []
    try:
      path = 'etc/logo.txt'
      with open(path, 'r') as myFile:
          lines = myFile.readlines()
          for line in lines:
              logo.append(line.rstrip('\n'))
      for line in logo:
          sys.stdout.write(line+'\n')
      print("\n")

    except IOError: # (Ignored) Error --> "No Such (logo.txt) File"
      return

def setArguments():
    global parser
    parser = argparse.ArgumentParser()
    parser.add_argument('files', type=argparse.FileType('r'), nargs='+')
    parser.add_argument('-o', help='output file required')
    parser.add_argument('--compress', help='generate a compressed version, off=0, on=1', default=0)
    return parser.parse_args()

def combineWordlist(files):
    print("{}[ + ] Dictionaries combining started!{}".format(color.GREEN, color.END));
    tmpWords = []
    for f in files:
        for line in f:
            tmpWords.append(line.strip())

    print("{}[ + ] Removing duplicates words{}".format(color.GREEN, color.END));
    words = set(tmpWords)
    time.sleep(2)
    return words

def generate(words, filename):
    if (os.path.isfile(filename)):
        print("{}[ - ] {} file already exist!{}".format(color.RED, filename, color.END))
        exit(0)
    
    print("{}[ + ] Writing words to {}!{}".format(color.GREEN, filename, color.END))
    with open(filename, 'a+') as f:
        for word in words:
            f.write("{}\n".format(word))

        f.close()
    time.sleep(2)

def compress(file):
    zipFileName = os.path.splitext(file)[0]
    print("{}[ + ] Generating compressed version ({}.zip){}".format(color.GREEN, zipFileName, color.END))
    with zipfile.ZipFile('{}.zip'.format(zipFileName), 'w') as ozip:
        ozip.write(file)
    time.sleep(2)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...\n")
		raise SystemExit