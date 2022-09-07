"""

    abs()	    Returns absolute value of a number
    divmod()	Returns quotient and remainder of integer division
    max()	    Returns the largest of the given arguments or items in an iterable
    min()	    Returns the smallest of the given arguments or items in an iterable
    pow()	    Raises a number to a power
    round()	    Rounds a floating-point value
    sum()	    Sums the items of an iterable


"""



absolute_values = abs(-10)

quotient_and_remainder = divmod(4,2) 

max_number_1 = max(1,2,3,4)

max_number_2 = max([1,2,3,4]) 

min_number_1 = min(1,2,3,4)
min_number_2 = min([1,2,3,4])

power_of_a_number = pow(2,3)


round_value_of_a_number = round(round (3.2013,2))
round_value_of_a_number = round(round (3.2013,3))
round_value_of_a_number = round(round (3.2213,3))

sum_of_items_in_iterable = sum([1,2,3,4])
sum_of_items_in_iterable = sum([1,2,3,4],10)
