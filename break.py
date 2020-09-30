from __future__ import unicode_literals

from optparse import OptionParser

from hazm import *


def get_lm_option_parser():
    parser = OptionParser()
    parser.add_option("--input", dest="input_path", metavar="FILE", default=None)
    parser.add_option("--output", dest="output_path", metavar="FILE", default=None)
    return parser


def word_list2sen(word_list, tags):
    output = [words[0]]
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
    all_tags = set()
    parser = get_lm_option_parser()
    (options, args) = parser.parse_args()
    tagger = POSTagger(model='resources/postagger.model')

    with open(options.input_path, "r") as r, open(options.output_path, "w") as w:
        for i, line in enumerate(r):
            sen = line.strip()

            normalizer = Normalizer()

            sen = normalizer.normalize(sen)
            words = word_tokenize(sen)
            tagged_words = tagger.tag(words)
            tags = list(map(lambda x: x[1], tagged_words))
            all_tags |= set(tags)
            w.write(word_list2sen(words, tags) + "\n")

            if i % 1000 == 0:
                print(i, end="\r")
    print("\nFinished")
    print(all_tags)
