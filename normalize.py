from break_words import *

if __name__ == "__main__":
    parser = get_lm_option_parser()
    (options, args) = parser.parse_args()
    normalizer = Normalizer()

    with open(options.input_path, "r") as r, open(options.output_path, "w") as w:
        for i, line in enumerate(r):
            sen = line.strip()
            sen = normalizer.normalize(sen)
            w.write(sen + "\n")
            if i % 1000 == 0:
                print(i, end="\r")
    print("\nFinished")
