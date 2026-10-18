# Q1. Find the Frequency of Each Word in a Sentence
def q1_word_frequency(sentence):
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


# Q2. Find the Frequency of Each Character in a Word
def q2_character_frequency(word):
    counts = {}
    for char in word:
        counts[char] = counts.get(char, 0) + 1
    return counts


# Q3. Find the First Non-Repeating Character in a Word
def q3_first_non_repeating(word):
    counts = q2_character_frequency(word)
    for char in word:
        if counts[char] == 1:
            return char
    return None


# Q4. Check Whether Two Strings Are Anagrams
def q4_are_anagrams(s1, s2):
    return q2_character_frequency(s1) == q2_character_frequency(s2)


# Q5. Find the First Repeating Character in a String
def q5_first_repeating(string):
    seen = set()
    for char in string:
        if char in seen:
            return char
        seen.add(char)
    return None


# Q6. Move All Zeros to the End of a List
def q6_move_zeros(nums):
    non_zeros = [num for num in nums if num != 0]
    zeros = [num for num in nums if num == 0]
    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List
def q7_second_highest(nums):
    distinct = sorted(set(nums), reverse=True)
    if len(distinct) < 2:
        return None
    return distinct[1]


# Q8. Remove Duplicates Without Changing the Original Order
def q8_remove_duplicates(nums):
    result = []
    seen = set()

    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result


# Q9. Find the Missing Number from 1 to N
def q9_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# Q10. Find Two Numbers Whose Sum Equals a Target
def q10_two_sum_first_pair(nums, target):
    seen = set()

    for num in nums:
        needed = target - num

        if needed in seen:
            return [needed, num]

        seen.add(num)

    return []


# Q11. Find the Number Closest to Zero
def q11_closest_to_zero(nums):
    if not nums:
        return None

    return min(nums, key=lambda num: (abs(num), num < 0))


# Q12. Find Common Elements Between Two Lists
def q12_common_elements(list1, list2):
    values = set(list2)
    result = []
    seen = set()

    for num in list1:
        if num in values and num not in seen:
            result.append(num)
            seen.add(num)

    return result


# Q13. Rotate a List to the Right by K Positions
def q13_rotate_right(nums, k):
    if not nums:
        return []

    k = k % len(nums)

    if k == 0:
        return nums[:]

    return nums[-k:] + nums[:-k]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def q14_max_consecutive_sum(nums):
    return max(
        nums[i] + nums[i + 1]
        for i in range(len(nums) - 1)
    )


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def q15_all_pairs(nums, target):
    pairs = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = tuple(sorted((nums[i], nums[j])))
                pairs.add(pair)

    return [list(pair) for pair in sorted(pairs)]

