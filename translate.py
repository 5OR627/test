import openai

client = openai.OpenAI(api_key="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")  # ваш ключ

def translate_srt_to_russian(srt_text):
    system_prompt = (
        "Ты профессиональный переводчик. Переведи следующий файл субтитров с китайского языка на русский язык, "
        "сохранив формат .srt (номера, таймкоды и разметку)."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": srt_text}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content

# 1. Считываем китайские субтитры
with open("subtitles.srt", "r", encoding="utf-8") as file:
    chinese_srt = file.read()

# 2. Переводим на русский
translated_srt = translate_srt_to_russian(chinese_srt)

# 3. Сохраняем результат
with open("subtitles_ru.srt", "w", encoding="utf-8") as file:
    file.write(translated_srt)
