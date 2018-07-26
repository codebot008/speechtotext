import uuid


def read_base_corpus(base_corpus_file):
    f = open(base_corpus_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def generate_random_string():
    x = uuid.uuid4().hex[:10]
    return x

def expand_corpus(lines, base_corpus_file):
    f = open(base_corpus_file, 'w').close()
    f = open(base_corpus_file, 'w')
    print("File size : ", len(lines))
    for line in lines:
        words = line.split()
        random_id = generate_random_string()
        words[-1] = random_id
        new_line = " ".join(words)
        f.write(new_line + "\n")
        f.write(line)
    f.close()



def main():
    # generate_random_string()
    for i in range(9):
        lines = read_base_corpus('corpus2.txt')
        expand_corpus(lines, 'corpus2.txt')

if __name__ == '__main__':
    main()