STRANI = {
    "Россия": "Москва",
    "США": "Вашингтон",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Япония": "Токио"
}


print("Перечень стран и их столиц:")
for STRANA, STOL in STRANI.items():
    print(f"{STRANA} - {STOL}")

STRANA = input("Введите название страны ")
if STRANA in STRANI:
    print(f"Столица страны {STRANA}: {STRANI[STRANA]}")
else:
    print(f"Для страны {STRANA} нет информации в словаре.")


sorted_STRANI = sorted(STRANI.items(), key=lambda x: x[0])
print("Содержимое словаря в алфавитном порядке названий стран:")
for country, STOL in sorted_STRANI:
    print(f"{country} - {STOL}")
