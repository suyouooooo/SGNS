import sys
import multiprocessing
import logging
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import os
base_dir = os.path.dirname((os.path.abspath(__file__)))
file_dir = os.path.join(base_dir, "file_dir")
min_count = 1


def word2vec_train(input_file, out_model, out_vector, min_count):
    """
    training file in the Word2vec model
    :param input_file: zhwiki_simplified_segment.txt
    :param out_model: zhwiki.model
    :param out_vector: zhwiki.vectors
    :param min_count: The minimum word frequency of the word vector needs to be calculated
    :return: null
    """
    model = Word2Vec(LineSentence(input_file), size=100, window=2, sg = 1, hs = 0, min_count=min_count, workers=multiprocessing.cpu_count())
    model.save(out_model)
    model.wv.save_word2vec_format(out_vector, binary=False)

if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            word2vec_train(os.path.join(file_dir, 'zhwiki_simplified_segment.txt'),
                           os.path.join(file_dir, 'zhwiki.model'),
                           os.path.join(file_dir, 'zhwiki.vectors'),
                           min_count)
        elif len(sys.argv) == 2:
            word2vec_train(sys.argv[1], os.path.join(file_dir, 'zhwiki.model'), os.path.join(file_dir, 'zhwiki.vectors'), min_count)
        elif len(sys.argv) == 3:
            word2vec_train(sys.argv[1], sys.argv[2], os.path.join(file_dir, 'zhwiki.vectors'), min_count)
        elif len(sys.argv) == 4:
            word2vec_train(sys.argv[1], sys.argv[2], sys.argv[3], min_count)
        elif len(sys.argv) == 5:
            word2vec_train(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    except Exception as err:
        logging.error(err)
