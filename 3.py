with open('en-ru.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
rus_eng = {}
for line in lines:
    if '-' in line:
        eng_word, ru_tr = line.strip().split('-')
        for ru_word in ru_tr.split(','):
            if ru_word.strip() not in rus_eng:
                rus_eng[ru_word.strip()] = [eng_word]
            else:
                if eng_word not in rus_eng[ru_word.strip()]:
                    rus_eng[ru_word.strip()].append(eng_word)
with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for key in sorted(rus_eng.keys()):
        trans = ','.join(sorted(rus_eng[key]))
        file.write(f'{key}-{trans}\n')