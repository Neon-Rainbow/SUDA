import os

if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(project_dir, 'data')
    scripts_dir = os.path.join(project_dir, 'scripts')

    # 预处理
    os.system(f'python {scripts_dir}/preprocess.py {data_dir}/romeo_and_juliet.txt {data_dir}/preprocessed_data.pkl')

    # 训练模型
    os.system(f'python {scripts_dir}/train_model.py {data_dir}/preprocessed_data.pkl {data_dir}/word2vec_model.h5 {data_dir}/word_vectors.npy')

    # 查找相似词
    os.system(f'python {scripts_dir}/find_similar.py {data_dir}/preprocessed_data.pkl {data_dir}/word_vectors.npy')