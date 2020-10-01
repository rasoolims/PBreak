from __future__ import unicode_literals

from optparse import OptionParser

from hazm import *

from rules import *


def get_lm_option_parser():
    parser = OptionParser()
    parser.add_option("--input", dest="input_path", metavar="FILE", default=None)
    parser.add_option("--output", dest="output_path", metavar="FILE", default=None)
    return parser


def tokenize_mwes(words, tags):
    new_words, new_tags = [], []
    for word, tag in zip(words, tags):
        if "_" in word:
            tokens = word.split("_")
            for tok in tokens:
                new_words.append(tok)
                new_tags.append(tag)
        else:
            new_words.append(word.replace(semi_space + semi_space, semi_space))
            new_tags.append(tag)
    return new_words, new_tags


def word_list2sen(word_list, tags):
    if len(word_list)==0:
        return ""
    output = [word_list[0]]
    no_space_next = False
    for j, (word, tag) in enumerate(zip(word_list[1:], tags[1:])):
        if tag == "PUNC":
            if word not in {"(", "]", "«"}:
                output.append(word)
                no_space_next = False
            else:
                output.append(" ")
                output.append(word)
                no_space_next = True
        else:
            if not no_space_next:
                output.append(" ")
            output.append(word)
            no_space_next = False

    return "".join(output)


if __name__ == "__main__":
    parser = get_lm_option_parser()
    (options, args) = parser.parse_args()
    tagger = POSTagger(model='resources/postagger.model')
    normalizer = Normalizer()

    with open(options.input_path, "r") as r, open(options.output_path, "w") as w:
        for i, line in enumerate(r):
            sen = line.strip()


            sen = normalizer.normalize(sen)
            words = word_tokenize(sen)
            tagged_words = tagger.tag(words)
            tags = list(map(lambda x: x[1], tagged_words))
            words, tags = tokenize_mwes(words, tags)
            broken_words, new_tags = break_words(words, tags)
            w.write(word_list2sen(broken_words, new_tags) + "\n")

            if i % 1000 == 0:
                print(i, end="\r")
    print("\nFinished")
