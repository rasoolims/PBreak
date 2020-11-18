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
            s = standardizer.normalize(sen)
            if len(s)==1:
                s = s[0]
            while True:
                if len(s)>1 and isinstance(s[0], list):
                    s = list(itertools.chain(*s))
                else:
                    break

            sen = " ".join(s).replace("_", " ")
            w.write(sen + "\n")
            print(i, end="\r")
    print("\nFinished")
