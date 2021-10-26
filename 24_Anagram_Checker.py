# 24. Anagram checker 

print("Enter two strings and I'll tell you if they are anagrams.")
anagram_s1 = input("Enter the first string: ")
anagram_s2 = input("Enter the second string: ")

def isAnagram(anagram_s1, anagram_s2):
    """
    input: two words 
    output: if it is an anagram 
    """
    if(sorted(anagram_s1) == sorted(anagram_s2)) and len(anagram_s1) == len(anagram_s2):
        return "are anagrams."
    else:
        return "are not anagrams."

print(f'"{anagram_s1}" and "{anagram_s2}"',  isAnagram(anagram_s1, anagram_s2))