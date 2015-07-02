#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler, problem 17: Number letter counts
(http://projecteuler.net/problem=17).


If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""



def get_number_string(number):
    """
    Returns the alphabetic transcription for a number between 0 and 1000.
    """

    units = ("zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine")

    teens = ("ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")

    tys = ("twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
        "ninety")


    if number < 10:
        res = units[number]

    if 10 <= number and number <= 19:
        res = teens[number - 10]

    if 20 <= number and number <= 99:
        decens = number / 10

        if number % 10 == 0:
            res = tys[decens - 2]
        else:
            res = tys[decens - 2] + units[number % 10]

    if number >= 100 and number <= 999:
        hundreds = number / 100
        rest = number % 100
        if rest != 0:
            res = units[hundreds]+" hundred and "+get_number_string(rest)
        else:
            res = units[hundreds]+" hundred"

    if number == 1000:
        res = "one thousand"

    return res

def main():
    """
    Generate the alphabetic transcriptions of the numbers and remove the spaces.
    """

    count = 0

    for i in range(1, 1001):
        word = get_number_string(i)
        count += (len(word) - word.count(' '))

    print "Used %d letters to write the numbers between 1 and 1000" % count

if __name__ == "__main__":
    main()
