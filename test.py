import logging
import sys
import json
from gensim.models import Word2Vec
import os
base_dir = os.path.dirname((os.path.abspath(__file__)))
file_dir = os.path.join(base_dir, "file_dir")


def word2vec_test(input_file, output_file, path_Word2Vec_Model, path_Word2Vec_Vec):
    """
    Test with the model and output the cosine distance between the two words in the test file
    :param input_file: pku_sim_test.txt
    :param output_file: 2019111490.txt
    :param path_Word2Vec_Model: zhwiki.model
    :param path_Word2Vec_Vec: zhwiki.vectors
    :return: null
    """
    word2vec_model = Word2Vec.load(path_Word2Vec_Model)
    sim_test = []
    for each in range(500):
        sim_test.append([])

    logging.info("generating dictionary...")
    dictionary = []
    with open(path_Word2Vec_Vec, 'r', encoding='utf-8') as fin_vec:
        for line in fin_vec:
            line = line.replace('.', ' ').replace(',', ' ').strip()
            dictionary.append(line.split()[0])
    logging.info("finish generate dictionary.")

    logging.info("generating json...")
    with open(os.path.join(file_dir, 'dict.json'), 'w', encoding='utf-8') as fout_vec:
        json.dump(dictionary, fout_vec)
    with open(os.path.join(file_dir, 'dict.json'), 'r', encoding='utf-8') as f:
        dict = json.load(f)
    logging.info("finish generate json.")

    with open(input_file, 'r', encoding='utf-8') as fin:
        i = 0
        for line in fin:
            str_tmp1, str_tmp2 = line.split('\t', 1)
            str1 = str_tmp1
            str2 = str_tmp2.replace('\n', '')
            if (str1 not in dict) or (str2 not in dict):
                sim_test[i].append((str1, str2, 'OOV'))
            else:
                sim = word2vec_model.wv.similarity(str1, str2)
                sim_test[i].append((str1, str2, str(sim)))
            i += 1
    with open(output_file, 'w', encoding='utf-8') as fout:
        for each in sim_test:
            fout.writelines(str(each[0][0]) + '\t' + str(each[0][1]) + '\t' + str(each[0][2]) + '\n')


if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            word2vec_test(os.path.join(file_dir, 'pku_sim_test.txt'),
                           os.path.join(file_dir, '2019111490.txt'),
                           os.path.join(file_dir, 'zhwiki.model'),
                           os.path.join(file_dir, 'zhwiki.vectors'))
        elif len(sys.argv) == 2:
            word2vec_test(sys.argv[1], os.path.join(file_dir, '2019111490.txt'),
                           os.path.join(file_dir, 'zhwiki.model'), os.path.join(file_dir, 'zhwiki.vectors'))
        elif len(sys.argv) == 3:
            word2vec_test(sys.argv[1], sys.argv[2], os.path.join(file_dir, 'zhwiki.model'), os.path.join(file_dir, 'zhwiki.vectors'))
        elif len(sys.argv) == 4:
            word2vec_test(sys.argv[1], sys.argv[2], sys.argv[3], os.path.join(file_dir, 'zhwiki.vectors'))
        elif len(sys.argv) == 5:
            word2vec_test(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    except Exception as err:
        logging.error(err)
