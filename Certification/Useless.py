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

