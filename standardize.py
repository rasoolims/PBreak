from break_words import *
import itertools

if __name__ == "__main__":
    parser = get_lm_option_parser()
    (options, args) = parser.parse_args()
    normalizer = Normalizer()
    standardizer = InformalNormalizer()

    with open(options.input_path, "r") as r, open(options.output_path, "w") as w:
        for i, line in enumerate(r):
            sen = line.strip()
            st_l = standardizer.normalize(sen)
            changed = []

            for s in st_l:
                for word_l in s:
                    if isinstance(word_l, list):
                        changed.append(word_l[0])
                    else:
                        changed.append(word_l)

            sen = " ".join(changed).replace("_", " ")
            w.write(sen + "\n")
            print(i, end="\r")
    print("\nFinished")
