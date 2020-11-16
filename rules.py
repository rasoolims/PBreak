import random

# Tags: {'PUNC', 'Ne', 'INT', 'DETe', 'Pe', 'NUM', 'CONJ', 'CONJe', 'RESe', 'CL', 'POSTP', 'PROe', 'V', 'N', 'P', 'ADV', 'PRO', 'DET', 'NUMe', 'RES', 'AJ', 'AJe', 'ADVe'}


"""
Paper reference by Bakhshizadeh and Tabibzadeh (2018): https://bit.ly/30nXgCz
"""

semi_space = "‌"


def general_an_breaker(word):
    if "ان" in word and  "اند" not in word and not word.startswith("ان"):
        word = word.replace("ان", "ون")
    return word


def verb_pron_break(word):
    """
    Based on 1-2-2 of paper.
    """
    if word.endswith("کند"):
        return  word[:-1] + "ه"
    if word == "بیایم":
        return "بیام"
    if word == "بیایی":
        return "بیای"
    if word == "بیاید":
        return "بیاد"
    if word == "بیاییم":
        return "بیایم"
    if word == "بیایید":
        return "بیایین"
    if word == "بیایند":
        return "بیان"
    if word == "نیایم":
        return "نیام"
    if word == "نیایی":
        return "نیای"
    if word == "نیاید":
        return "نیاد"
    if word == "نیاییم":
        return "نیایم"
    if word == "نیایید":
        return "نیایین"
    if word == "نیایند":
        return "نیان"

    if word == "بخواه":
        if random.random() < 0.8:
            return "بخوا"
        else:
            return "بخا"

    if word == "بخواهم":
        if random.random() < 0.8:
            return "بخوام"
        else:
            return "بخام"

    if word == "بخواهی":
        if random.random() < 0.8:
            return "بخوای"
        else:
            return "بخای"
    if word == "بخواهد":
        if random.random() < 0.8:
            return "بخواد"
        else:
            return "بخاد"
    if word == "بخواهیم":
        if random.random() < 0.8:
            return "بخوام"
        else:
            return "بخام"

    if word == "بخواهید":
        if random.random() < 0.8:
            return "بخواین"
        else:
            return "بخاین"

    if word == "بخواهند":
        if random.random() < 0.8:
            return "بخوان"
        else:
            return "بخان"

    if word == "نخواهم":
        if random.random() < 0.8:
            return "نخوام"
        else:
            return "نخام"

    if word == "نخوای":
        if random.random() < 0.8:
            return "نخواه"
        else:
            return "نخاه"

    if word == "نخواد":
        if random.random() < 0.8:
            return "نخواد"
        else:
            return "نخاد"
    if word == "نخواهیم":
        if random.random() < 0.8:
            return "نخوایم"
        else:
            return "نخایم"

    if word == "نخواهید":
        if random.random() < 0.8:
            return "نخواین"
        else:
            return "نخاین"

    if word == "نخواهند":
        if random.random() < 0.8:
            return "نخوان"
        else:
            return "نخان"
    if word == "شوم":
        if random.random() < 0.8:
            return "شم"
        else:
            return "بشم"

    if word == "شوی":
        if random.random() < 0.8:
            return "شی"
        else:
            return "بشی"
    if word == "شود":
        if random.random() < 0.8:
            return "شه"
        else:
            return "بشه"
    if word == "شویم":
        if random.random() < 0.8:
            return "شیم"
        else:
            return "بشیم"
    if word == "شوید":
        if random.random() < 0.8:
            return "شید"
        else:
            return "بشید"
    if word == "شوند":
        if random.random() < 0.8:
            return "شن"
        else:
            return "بشن"
    if word == "بشوم":
        return "بشم"
    if word == "بشوی":
        return "بشی"
    if word == "بشود":
        return "بشه"
    if word == "بشویم":
        return "بشیم"
    if word == "بشوید":
        return "بشین"
    if word == "بشوند":
        return "بشن"
    if word == "نشوم":
        return "نشم"
    if word == "نشوی":
        return "نشی"
    if word == "نشود":
        return "نشه"
    if word == "نشویم":
        return "نشیم"
    if word == "نشوید":
        return "نشین"
    if word == "نشوند":
        return "نشن"
    if word.endswith("باشد"):
        return word.replace("باشد", "باشه")

    if word == "روم":
        return "برم"

    if word == "روی":
        return "بری"
    if word == "رود":
        return "بره"
    if word == "رویم":
        return "بریم"
    if word == "روید":
        return "برید"
    if word == "روند":
        return "برن"
    if word == "بروم":
        return "برم"
    if word == "بروی":
        return "بری"
    if word == "برود":
        return "بره"
    if word == "برویم":
        return "بریم"
    if word == "بروید":
        return "برین"
    if word == "بروند":
        return "برن"
    if word == "نروم":
        return "نرم"
    if word == "نروی":
        return "نری"
    if word == "نرود":
        return "نره"
    if word == "نرویم":
        return "نریم"
    if word == "نروید":
        return "نرین"
    if word == "نروند":
        return "نرن"

    if word == "بدهم":
        return "بدم"
    if word == "بدهی":
        return "بدی"
    if word == "بدهد":
        return "بده"
    if word == "بدهیم":
        return "بدیم"
    if word == "بدهید":
        return "بدین"
    if word == "بدهند":
        return "بدن"
    if word == "ندهم":
        return "ندم"
    if word == "ندهی":
        return "ندی"
    if word == "ندهد":
        return "نده"
    if word == "ندهیم":
        return "ندیم"
    if word == "ندهید":
        return "ندین"
    if word == "ندهند":
        return "ندن"

    if word == "می‌شویند":
        return "می‌شورن"
    if word == "می‌دهند":
        return "می‌دن"
    if word == "می‌شوییم":
        return "می‌شوریم"
    if word == "می‌شویی":
        return "می‌شوری"
    if word == "می‌شوید":
        if random.random() < 0.1:  # Very low chance
            return "می‌شوره"

    if word.startswith("ایست"):
        word = "و" + word
    if "توان" in word:
        if random.random() < 0.8:
            word = word.replace("توان", "تون")
    if "می‌اند" in word:
        if random.random() < 0.8:
            word = word.replace("می‌اند", "میند")
    if "شمار" in word:
        if random.random() < 0.8:
            word = word.replace("شمار", "شمر")
    if "سپار" in word:
        if random.random() < 0.8:
            word = word.replace("سپار", "سپر")
    if "نشین" in word and not word.startswith("ن"):
        if random.random() < 0.8:
            word = word.replace("نشی", "شی")

    if "نشست" in word and not word.startswith("ن"):
        if random.random() < 0.1:  # Very low chance
            word = word.replace("نشست", "شست")

    if "گذا" in word and not word.startswith("گذا"):
        if random.random() < 0.6:
            word = word.replace("گذا", "ذا")
        else:
            word = word.replace("گذا", "زا")

    if word.startswith("آم"):
        if random.random() < 0.7:
            word = word.replace("آ", "او")

    if "آور" in word:
        word = word.replace("آور", "آر")
    if "اور" in word:
        word = word.replace("اور", "ار")

    if word.endswith("خواهد"):
        word = word[:-2] + "د"

    if "خواه" in word:
        if random.random() < 0.8:
            word = word.replace("خواه", "خوا")
        else:
            word = word.replace("خواه", "خا")

    if "شوی" in word:
        if random.random() < 0.8:
            word = word.replace("شوی", "شی")

    if "خوان" in word:
        if random.random() < 0.8:
            word = word.replace("خوان", "خون")
        else:
            word = word.replace("خوان", "خان")

    if "ان" in word:
        if random.random() < 0.8:
            word = word.replace("ان", "ون")

    elif len(word) > 3 and word.endswith("هم"):
        return word[:-2] + "م"
    elif len(word) > 3 and word.endswith("هی"):
        return word[:-2] + "ی"
    elif len(word) > 3 and word.endswith("هد"):
        return word[:-1]
    elif len(word) > 3 and word.endswith("هیم"):
        return word[:-3] + "یم"
    elif len(word) > 3 and word.endswith("هید"):
        return word[:-3] + "ید"
    elif len(word) > 3 and word.endswith("هند"):
        return word[:-3] + "ند"

    elif len(word) > 3 and word.endswith("وید"):
        return word[:-3] + "ن"
    elif len(word) > 3 and word.endswith("یند"):
        return word[:-1] + "ه"
    elif len(word) > 3 and word.endswith("نند"):
        return word[:-1]
    elif len(word) > 3 and word.endswith("ند"):
        return word[:-1]
    elif len(word) > 3 and word.endswith("ویید"):
        return word[:-4] + "ید"
    elif len(word) > 3 and word.endswith("یید"):
        return word[:-2] + "د"
    elif len(word) > 3 and word.endswith("ید"):
        return word[:-1] + "ن"

    elif len(word) > 3 and word.endswith("ود") and  "بود" not in word and  "نمود" not in word:
        return word[:-2] + "ه"
    elif len(word) > 3 and word.endswith("د") and not word.endswith("اد") and not word.endswith("کرد"):
        return word[:-1] + "ه"

    return word


def plural_breaker(word):
    """
    Page 10 of the paper
    Converts "HA" or "A" for plurals
    """
    ending = ""
    if word.endswith("تان") or word.endswith("مان") or word.endswith("شان"):
        ending = word[-3:].replace("ا", "و")
        word = word[:-3]
    elif word.endswith(semi_space + "ام") or word.endswith(semi_space + "ات") or word.endswith(semi_space + "اش"):
        if word[-3] != "ه":
            ending = word[-2:].replace("ا", "")
        else:
            ending = word[-3:].replace("ا", "")
        word = word[:-3]


    if len(word) > 4 and (word.endswith("ها") or word.endswith("های")):
        if word.endswith("های"):
            ending = "ی"
            word = word[:-1]
        if word.endswith("هایی"):
            ending = "یی"
            word = word[:-2]

        subword = word[:-2]
        if subword[-1] == semi_space:
            subword = subword[:-1]
        if subword[-1] not in {"ا", "و", "ه"}:
            word = subword + "ا" + ending
        else:
            return word.replace(semi_space, " ")

    if random.random() < 0.6:
        return (word + ending).replace(semi_space, "")
    else:
        return (word + ending).replace(semi_space, " ")



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
    if word == "در" and tag == "P" and random.random() < 0.5:
        return "تو"
    if word == "به" and tag == "P" and random.random() < 0.5:
        return "ب"
    if word == "که" and random.random() < 0.3:
        return "ک"
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
    if "روی" in word:
        if random.random() < 0.8:
            word = word.replace("روی", "رو")
    if "همان" in word:
        word = word.replace("همان", "همون")
    if "دیگری" in word:
        word = word.replace("دیگری", "دیگه‌ای")
    if "دیگر" in word:
        word = word.replace("دیگر", "دیگه")
    if word.endswith("شان"):
        word = word.replace("شان", "شون")
    if word.endswith("مان"):
        word = word.replace("مان", "مون")
    if word.endswith("تان"):
        word = word.replace("تان", "تون")
    if word.endswith("ان"):
        word = word.replace("ان", "ون")
    if word.endswith("یم") and tag != "V" and random.random() < 0.4:
        word = word.replace("یم", "م")
    if word.endswith("یت") and tag != "V" and random.random() < 0.4:
        word = word.replace("یت", "ت")
    if word.endswith("یش") and random.random() < 0.4:
        word = word.replace("یش", "ش")
    return word


def deterministic_break(word, tag):
    if "اًْ" in word:
        if random.random() < 0.5:
            word = word.replace("اً", "ا")
        else:
            word = word.replace("اً", "ن")

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
    if word == "آنان":
        return "اونا"
    if word == "آنجا":
        return "اونجا"
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
        return "در"
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
    if word == "مرا":
        return "منو"
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
        try:
            if "ه" + semi_space in word:
                if random.random() < 0.8:
                    word = word.replace("ه" + semi_space, "ه" + " ")
            elif semi_space in word:
                r = random.random()
                if r < 0.7:
                    word = word.replace(semi_space, " ")
                elif r < 0.9:
                    word = word.replace(semi_space, "")
            if random.random() < 0.99:
                word = deterministic_break(word, tag)
            if random.random() < 0.90:
                word = less_common_deterministic_break(word, tag)

            if tag in {"N", "Ne"}:
                if random.random() < 0.99:
                    word = plural_breaker(word)
            if tag in {"V"}:
                if random.random() < 0.99:
                    word = verb_pron_break(word)

            if random.random() < 0.8:
                word = general_an_breaker(word)

            if len(broken_words) > 0 and word == "من" and broken_words[-1] == "به" and random.random() < 0.9:
                broken_words[-1] = "بهم"
            elif len(broken_words) > 0 and word == "او" and broken_words[-1] == "به" and random.random() < 0.9:
                broken_words[-1] = "بهش"
            elif len(broken_words) > 0 and word == "تو" and broken_words[-1] == "به" and random.random() < 0.9:
                broken_words[-1] = "بهت"
            elif len(broken_words) > 0 and word == "شما" and broken_words[-1] == "به" and random.random() < 0.9:
                broken_words[-1] = "بهت"
            elif len(broken_words) > 0 and broken_words[-1] == "به" and random.random() < 0.99:
                broken_words[-1] = "ب" + word

            elif len(broken_words) > 0 and word == "است" or word == "هست" and random.random() < 0.99:
                if broken_words[-1][-1] in {"ا", "و", "ه"}:
                    if broken_words[-1][-1] in {"ه"}:
                        broken_words[-1] += semi_space + "س"
                    else:
                        broken_words[-1] += "س"
                else:
                    broken_words[-1] += "ه"
            elif word == "را" and random.random() < 0.99:
                if random.random() < 0.5 or len(broken_words) == 0:
                    word = "رو"
                    broken_words.append(word)
                    broken_tags.append(tag)
                else:
                    if broken_words[-1][-1] in {"ا", "و", "ه"}:
                        if broken_words[-1][-1] in {"ه"}:
                            if random.random() < 0.8:
                                broken_words[-1] += semi_space + "رو"
                            else:
                                broken_words[-1] += semi_space + "ئو"
                        elif broken_words[-1] == "او":
                            broken_words[-1] += "نو"
                        elif broken_words[-1][-1] in {"و"}:
                            if random.random() < 0.8:
                                broken_words[-1] += semi_space + "رو"
                            else:
                                broken_words[-1] += semi_space + "ئو"
                        else:
                            broken_words[-1] += "رو"
                    else:
                        broken_words[-1] += "و"
            else:
                if len(word) > 0:
                    broken_words.append(word)
                    broken_tags.append(tag)
        except:
            broken_words.append(word)
            broken_tags.append(tag)
    return broken_words, broken_tags
