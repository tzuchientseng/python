print("----------------------------------------", 'Test-ROT 13', "-"*40)
def rot13(word):
    output = []
    for c in word.lower():
        new_ord = ord(c) +13
        if new_ord > ord('z'):
            new_ord -= 26
        output.append(chr(new_ord))
    return ''.join(output)
print(rot13('python'))

print("----------------------------------------", 'Test-sorted()', "-"*40)
def strsort(s):
    return ''.join(sorted(s, key = str.lower)) #NOT lower()
print(strsort('python'))

print("----------------------------------------", 'Test-Pig Latin Sentence', "-"*40)
def pl_sentence(sentence):
    output = []
    for word in sentence.lower().split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(output)

print(pl_sentence('This is a test.'))

import string
def pl_sentence(sentence):
    output = []
    for word in sentence.lower().split():
        # 檢查單詞是否在末尾有標點符號
        if word[-1] in string.punctuation:
            punctuation = word[-1]
            word = word[:-1]
        else:
            punctuation = ''
        
        # 將單詞轉換為豬拉丁語
        if word[0] in 'aeiou':
            pig_latin_word = f'{word}way'
        else:
            pig_latin_word = f'{word[1:]}{word[0]}ay'
        
        # 如果有標點符號，則將其添加回去
        output.append(f'{pig_latin_word}{punctuation}')
    
    return ' '.join(output)

print(pl_sentence('This is a test. My name is Sunny!'))

print("----------------------------------------", 'Test-Pig Latin', "-"*40)
def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else: 
        return word[1:] + word[0] + 'ay'
        # return word[1:] + word[:1] + 'ay'
        
print(pig_latin('python'))
"""
public class PigLatin {
    public static String pigLatin(String word) {
        if (word.length() == 0) {
            return word;
        }
        char firstChar = word.charAt(0);
        if ("aeiou".indexOf(firstChar) != -1) {
            return word + "way";
        } else {
            return word.substring(1) + firstChar + "ay";
        }
    }

    public static void main(String[] args) {
        System.out.println(pigLatin("python"));
    }
}
"""

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/10
def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output

print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('abc', 'd', 'e'))
print(mysum([10, 20, 30], [40, 50], [60]))

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/11
people = [
    ('Joe', 'Biden', 'president@usa.gov'),
    ('Emmanuel', 'Macron', 'president@france.gov'),
    ('Justin', 'Trudeau', 'primeminister@canada.gov'),
    ('Angela', 'Merkel', 'primeminister@germany.gov'),
    ('Jacinda', 'Ardern', 'primeminister@newzealand.gov')
    ]

for person in sorted(people, key=lambda d: (d[1], d[0])):
    print(f'{person[1]}, {person[0]}: {person[2]}')

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/12
import operator

def sorted_grades(grades):
    grades.sort(key=operator.itemgetter(2), reverse=True)
    output = []
    for first, last, grade in grades:
        output.append(f'{last:12s}{first:10s}{grade:.1f}')
    return '\n'.join(output)

grades = [
    ('Alice', 'Wooding', 89),
    ('Bob', 'Johnson', 86),
    ('Cindy', 'Letterman', 93),
    ('David', 'Moor', 86),
    ('Eddie', 'Williams', 91)
    ]

print(sorted_grades(grades))

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/13
import operator

def most_repeated_letter(word):
    letters = list(set(word))
    letters_count = []
    for letter in letters:
        letters_count.append((letter, word.count(letter)))
    result = sorted(letters_count, key=operator.itemgetter(1))[-1]
    print(f'{result[0]} 重複了 {result[1]} 次')

most_repeated_letter('independence')

print("----------------------------------------", 'Test', "-"*40)
