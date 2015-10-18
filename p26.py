#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 26: Reciprocal cycles (https://projecteuler.net/problem=26)

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:


    1/2	 = 	0.5
    1/3	 = 	0.(3)
    1/4	 = 	0.25
    1/5	 = 	0.2
    1/6	 = 	0.1(6)
    1/7	 = 	0.(142857)
    1/8	 = 	0.125
    1/9	 = 	0.(1)
    1/10 = 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.


Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.

"""
def get_cycles(num, den):
    """
    Implements the division algorithm, keeping track of the quotients and
    reminders. When a reminder is repeated, there is a cycle, and the quotients
    will be repeated all over again.
    """
    reminder = num
    quotients = {}

    step = 0
    while True:
        if reminder < den:
            reminder *= 10

        if reminder in quotients.keys():
            return get_sequence(reminder, quotients)

        if reminder % den == 0:
            #No cycles
            return None
        else:
            quotients[reminder] = {'step' : step, 'quot' : reminder / den}
            reminder = reminder % den

        step += 1

def get_sequence(reminder, quotients):
    """
    Goes over the sequence of quotients (the repeated and the non-repeated),
    building the cycle.

    The reminder passed identifies the beginning of the cycle.
    """

    init_step = quotients[reminder]['step']

    steps = {q['step'] : q['quot'] for _, q in quotients.iteritems()}

    return "".join(map(str,
                       [steps[step] for step in range(init_step, len(steps))]
                       ))


def main():
    """
    The trick to this problem is cycle detection (see get_cycles). The rest is
    going through a small list of candidates.
    """
    max_cycle = 0
    d = None

    for den in range(2, 1000):
        cycles = get_cycles(1, den)
        if cycles is not None:
            if len(cycles) > max_cycle:
                max_cycle = len(cycles)
                d = den

    print "The d-value with the longest recurring cycle is %d" % d

if __name__ == "__main__":
    main()
