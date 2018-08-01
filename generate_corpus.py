import uuid


def read_base_corpus(base_corpus_file):
    f = open(base_corpus_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def generate_random_string():
    x = uuid.uuid4().hex[:10]
    return ' '.join(list(x))
    # return x

def generate_random_file():
    f = open('new_random.txt', 'w')
    for x in range(1000):
        d = generate_random_string()
        f.write(d + '\n')
    f.close()



def expand_corpus(lines, target_file):
    f2 = open(target_file, 'w')
    print("File size : ", len(lines))
    for line in lines:
        words = line.split()
        for x in range(100):
            random_id = generate_random_string()
            words[-1] = random_id
            new_line = " ".join(words)
            f2.write(new_line + "\n")
    f2.close()

def decompress_alpha(source_file, target_file):
    f3 = open(target_file, 'w')
    f2 = open(source_file, 'r')
    lines = f2.readlines()
    for line in lines:
        words = line.split()
        if 'server' in words:
            new_line = ' '.join(words[0: words.index('server') + 1]) + ' ' + ''.join(words[words.index('server') + 1:])
        elif 'machine' in words:
            new_line = ' '.join(words[0: words.index('machine') + 1]) + ' ' + ''.join(words[words.index('machine') + 1:])
        elif 'instance' in words:
            new_line = ' '.join(words[0: words.index('instance') + 1]) + ' ' + ''.join(words[words.index('instance') + 1:])
        f3.write(new_line + "\n")
    f2.close()
    f3.close()


def main():
    # generate_random_string()
    # for i in range(7):
    # lines = read_base_corpus('corpus_files/corpus1.txt')
    # expand_corpus(lines, 'corpus_files/corpus2.txt')
    # generate_random_file()
    decompress_alpha('corpus_files/corpus2.txt', 'corpus_files/corpus3.txt')

if __name__ == '__main__':
    main()