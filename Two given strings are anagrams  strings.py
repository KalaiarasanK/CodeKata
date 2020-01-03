#Joseph was going through topic of strings. He learnt about anagrams. But due to some circumstances he forget ,now he hired you to help him in completing the work.Your task is to tell whether the two given strings are anagrams


def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)
print(isAnagram("abcd","cdab"))
