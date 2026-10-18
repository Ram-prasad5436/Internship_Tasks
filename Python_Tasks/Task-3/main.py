
from solutions import (
    q1_word_frequency,
    q2_character_frequency,
    q3_first_non_repeating,
    q4_are_anagrams,
    q5_first_repeating,
    q6_move_zeros,
    q7_second_highest,
    q8_remove_duplicates,
    q9_missing_number,
    q10_two_sum_first_pair,
    q11_closest_to_zero,
    q12_common_elements,
    q13_rotate_right,
    q14_max_consecutive_sum,
    q15_all_pairs
)

# Q1
print("Q1:", q1_word_frequency(
    "python is easy and python is powerful"
))
print("Q1 Test:", q1_word_frequency("red blue red"))

# Q2
print("Q2:", q2_character_frequency("banana"))
print("Q2 Test:", q2_character_frequency("hello"))

# Q3
print("Q3:", q3_first_non_repeating("swiss"))
print("Q3 Test:", q3_first_non_repeating("aabb"))

# Q4
print("Q4:", q4_are_anagrams("listen", "silent"))
print("Q4 Test:", q4_are_anagrams("hello", "world"))

# Q5
print("Q5:", q5_first_repeating("programming"))
print("Q5 Test:", q5_first_repeating("abcdef"))

# Q6
print("Q6:", q6_move_zeros([0, 3, 0, 1, 2, 0, 4]))
print("Q6 Test:", q6_move_zeros([1, 2, 3]))

# Q7
print("Q7:", q7_second_highest([10, 20, 40, 30, 40, 20]))
print("Q7 Test:", q7_second_highest([5, 5, 5]))

# Q8
print("Q8:", q8_remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 Test:", q8_remove_duplicates([1, 1, 2, 2]))

# Q9
print("Q9:", q9_missing_number([1, 2, 4, 5, 6], 6))
print("Q9 Test:", q9_missing_number([1, 3, 4], 4))

# Q10
print("Q10:", q10_two_sum_first_pair([2, 7, 11, 15], 9))
print("Q10 Test:", q10_two_sum_first_pair([1, 2, 3], 20))

# Q11
print("Q11:", q11_closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 Test:", q11_closest_to_zero([-4, 1, 3]))

# Q12
print("Q12:", q12_common_elements(
    [1, 2, 3, 4, 5], [3, 4, 5, 6, 7]
))
print("Q12 Test:", q12_common_elements([1, 2, 2, 3], [2, 3, 4]))

# Q13
print("Q13:", q13_rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 Test:", q13_rotate_right([1, 2, 3], 0))

# Q14
print("Q14:", q14_max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 Test:", q14_max_consecutive_sum([1, 10, 2]))

# Q15
print("Q15:", q15_all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 Test:", q15_all_pairs([1, 2, 3], 10))
