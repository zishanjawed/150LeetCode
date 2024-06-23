"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case? :- solution works for this too
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        memory = {}

        # Create the memory
        for letter in s:
            if memory.get(letter):
                memory[letter] += 1
            else:
                memory[letter] = 1

        # Check if letter exist or the frequency of the letter is greater than 1  in the memory 
        for letter in t:
            freq = memory.get(letter,0)
            if freq < 1:
                return False

            memory[letter] -= 1

        
        return True

        