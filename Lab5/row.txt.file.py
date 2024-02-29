#1
import re

def pattern(str):
    p = r'ab*' # для поиска паттерна, "a, ab, abbb ..., " 
    # здесь ab* означает что после 'a' должны быть 0 или больше 'b'
    if re.match(p, str):
        return True
    else:
        return False

str = str(input())
print(pattern(str))


#2
import re

def search_pattern(string):
    p = r'ab{2,3}' #ищем паттерн где после 'a' идет 2 или 3 'b'
    if re.match(p, string):
        return True
    else:
        return False

string = str(input())
print(search_pattern(string))

#3
import re

pattern = re.compile(r"[a-z]+_[a-z]+")
print(pattern.findall("armanda_ishappy_"))

#4
import re

pattern = re.compile(r"[A-Z]{1}[a-z]+")
print(pattern.findall("Armanda Temirzhankyzy programming Principles 2"))

#5
import re

pattern = re.compile(r'a.*b$')
print(pattern.findall("asdawd, dfogergoyea4994b, ab, ppfkgdfgab"))

#6
import re

text = "Hello My name, is. Armanda"
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)

#7
import re

def snakeToCamel(text):
    words = text.split('_')
    CamelString= words[0]
    for char in words[1:]:
        CamelString += char.capitalize()
    return CamelString

text = "my_snake_case_string"
print(snakeToCamel(text))

#8
import re

text = "MyNameIsArmanda"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)

#9
import re

text = "HelloMyNameIsArmandaAndIamAStudentOfKbtu"
words = re.findall(r'[A-Z][^A-Z]*', text)
spaced = ' '.join(words)
print(spaced)

#10
def camel_to_snake(CamelCase):
    snake_case = ""
    for char in CamelCase:
        if(char.isupper()):
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    if snake_case.startswith('_'):
        snake_case = snake_case[1:]
    return snake_case

CamelCase = "ThisIsDulat"

print(camel_to_snake(CamelCase))


 