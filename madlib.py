# CMPT 120L 113
# Mad Lib Program
# Author: Ian Miller
# Created: 14 Sep 2018

def promptForWords():
    global noun, adjective, verb, place
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

def makeAndPrintSentence():
    print("The", adjective, noun, verb, "to", place, "at an incredible rate of speed")

def main():
    promptForWords()
    makeAndPrintSentence()

main()




