import random

# Tags: {'PUNC', 'Ne', 'INT', 'DETe', 'Pe', 'NUM', 'CONJ', 'CONJe', 'RESe', 'CL', 'POSTP', 'PROe', 'V', 'N', 'P', 'ADV', 'PRO', 'DET', 'NUMe', 'RES', 'AJ', 'AJe', 'ADVe'}


"""
Paper reference by Bakhshizadeh and Tabibzadeh (2018): https://bit.ly/30nXgCz
"""

semi_space = "‌"


def plural_breaker(word):
    """
    Page 10 of the paper
    Converts "HA" or "A" for plurals
    """

    if len(word) > 3 and (word.endswith("ها") or word.endswith("های")):
        ending = ""
        if word.endswith("های"):
            ending = "ی"
            word = word[:-1]

        subword = word[:-2]
        if subword[-1] == semi_space:
            subword = subword[:-1]
        if subword[-1] not in {"ا", "و", "ه"}:
            word = subword + "ا" + ending

    return word


def less_common_deterministic_break(word, tag):
    if word == "آقا":
        if random.random() < 0.3:
            return "آ"
        else:
            return "آق"
    if word == "استاد":
        if random.random() < 0.5:
            return "اوسا"
        else:
            return "اوس"
    if word == "ارواح":
        return "اروا"
    if word == "انبر":
        return "امبر"
    if word == "پنبه":
        return "پمبه"
    if word == "پوست":
        return "پوس"
    if word == "پس":
        if random.random() < 0.5:
            return "پ"
        else:
            return "په"
    if word == "جهاد":
        return "جاهاد"
    if word == "جنبه":
        return "جمبه"
    if word == "چند":
        return "چن"
    if word == "چکار":
        return "چیکار"
    if word == "خوب":
        return "خب"
    if word == "خرد":
        return "خورد"
    if word == "دست":
        return "دس"
    if word == "دقیقه":
        if random.random() < 0.5:
            return "دیقه"
        else:
            return "دقه"
    if word == "دنبه":
        return "دمبه"
    if word == "درود":
        return "دورود"
    if word == "دوست":
        return "دوس"
    if word == "راه":
        return "را"
    if word == "سرود":
        return "سورود"
    if word == "سبیل":
        return "سیبیل"
    if word == "شنبه":
        return "شمبه"
    if word == "شش":
        return "شیش"
    if word == "صاحب":
        return "صاحاب"
    if word == "صبر":
        return "صب"
    if word == "فکر":
        return "فک"
    if word == "کاه":
        return "کا"
    if word == "کلاه":
        return "کلا"
    if word == "کجا":
        return "کوجا"
    if word == "کلید":
        return "کیلید"
    if word == "وقت":
        if random.random() < 0.7:
            return "وخ"
        else:
            return "وخت"
    if word == "نگاه":
        if random.random() < 0.7:
            return "نیگاه"
        else:
            return "نگا"
    return word


def deterministic_break(word, tag):
    if word == "اگر":
        return "اگه"
    if word == "مگر":
        return "مگه"
    if word == "دیگر":
        return "دیگه"
    if word == "آخر":
        return "آخه"
    if word == "آن":
        return "اون"
    if word == "آنها":
        return "اونا"
    if word == "آن‌ها":
        return "اونها"
    if word == "یک":
        return "یه"
    if word == "آتش":
        return "آتیش"
    if word == "آرام":
        return "آروم"
    if word == "ابراهیم":
        return "ابرام"
    if word == "بادام":
        return "بادوم"
    if word == "بام":
        return "بوم"
    if word == "بهار":
        return "باهار"
    if word == "البته":
        return "البت"
    if word == "برای":
        if random.random() < 0.7:
            return "واسه"
        else:
            return "برا"
    if word == "پیراهن":
        if random.random() < 0.7:
            return "پیرهن"
        else:
            return "پیرن"
    if word == "تمام":
        return "تموم"
    if word == "توی":
        return "تو"
    if word == "روی":
        return "رو"
    if word == "تومان":
        return "تومن"
    if word == "تکه":
        return "تیکه"
    if word == "جگر":
        return "جیگر"
    if word == "زگیل":
        return "زیگیل"
    if word == "سیاه":
        return "سیا"
    if word == "چهار":
        if random.random() < 0.7:
            return "چار"
        else:
            return "چاهار"
    if word == "چهل":
        return "چل"
    if word == "چه" and tag == "DET":
        return "چی"
    if word == "چیست":
        return "چیه"
    if word == "حرام":
        return "حروم"
    if word == "خانم":
        return "خانوم"
    if word == "خفقان":
        return "خفه‌خون"
    if word == "دفعه":
        return "دفه"
    if word == "سریش":
        return "سیریش"
    if word == "کدام":
        return "کدوم"
    if word == "کوچک":
        return "کوچیک"
    if word == "که" and tag != "CONJ":
        return "کی"
    if word == "مثل":
        return "مث"
    if word == "مردکه":
        return "مرتیکه"
    if word == "ناخن":
        return "ناخون"
    if word == "نهار":
        return "ناهار"

    if word == "مشهدی":
        r = random.random()
        if r < 0.3:
            return "مشدی"
        elif r < 0.5:
            return "مشتی"
        elif r < 0.7:
            return "مشد"
        else:
            return "مش"
    return word


def break_words(words, tags):
    broken_words = []
    broken_tags = []
    for i, (word, tag) in enumerate(zip(words, tags)):
        if random.random() < 0.8:
            word = deterministic_break(word, tag)
        elif random.random() < 0.3:
            word = less_common_deterministic_break(word, tag)

        if tag in {"N", "Ne"}:
            if random.random() < 0.5:
                word = plural_breaker(word)

        broken_words.append(word)
        broken_tags.append(tag)
    return broken_words, broken_tags
