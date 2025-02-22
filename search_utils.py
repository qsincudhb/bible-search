import re

def search_word(word, verses):
    """
    جستجوی یک کلمه در آیات و برگرداندن تطابق‌ها با تعداد
    """
    results = []
    total_count = 0

    # تمیز کردن و آماده‌سازی کلمه جستجو
    word = word.strip()

    if not word:
        return results, total_count

    # ایجاد الگو برای جستجوی کلمه کامل
    pattern = r'(?u)\b' + re.escape(word) + r'\b'

    for verse in verses:
        # شمارش تکرار با استفاده از مرزهای کلمه با پشتیبانی یونیکد
        count = len(re.findall(pattern, verse['text'], re.IGNORECASE))
        if count > 0:
            results.append({
                'testament': verse['testament'],
                'book': verse['book'],
                'reference': verse['reference'],
                'text': verse['text'],
                'count': count
            })
            total_count += count

    return results, total_count

def search_verse(phrase, verses):
    """
    جستجوی یک عبارت در آیات
    """
    results = []

    # تمیز کردن و آماده‌سازی عبارت جستجو
    phrase = phrase.strip()

    if not phrase:
        return results

    for verse in verses:
        if phrase.lower() in verse['text'].lower():
            results.append({
                'testament': verse['testament'],
                'book': verse['book'],
                'reference': verse['reference'],
                'text': verse['text']
            })

    return results
