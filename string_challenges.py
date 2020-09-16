# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print('---')


# Вывести количество букв "а" в слове
word = 'Архангельск'
number_of_a = 0
for letter in word.lower():
    if letter  == "а":
        number_of_a += 1 
print(number_of_a)
print('---')

# Вывести количество гласных букв в слове
word = 'Архангельск'
number_of_vowels = 0
vowels = set('уеэоаыяию')
for letter in word.lower():
    if letter in vowels:
        number_of_vowels += 1
print(number_of_vowels)
print('---')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))
print('---')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for letter in sentence.split():
    print(letter[0])
print('---')


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
len_total = 0
for letter in sentence.split():
    len_total += len(letter)
len_average = len_total/len(sentence.split())
print(len_average)