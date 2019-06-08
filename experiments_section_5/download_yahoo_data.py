import os
import shutil

if __name__ == '__main__':

    data_dir = './data/'
    if not os.path.exists(os.path.join(data_dir, 'training_arr.npy')):
        os.system("wget https://s3.amazonaws.com/cornell-tech-sdl-rec-bias/dataset/yahoo/training_arr.npy")
        shutil.move('training_arr.npy', './data/training_arr.npy')

    if not os.path.exists(os.path.join(data_dir, 'validation_arr.npy')):
        os.system("wget https://s3.amazonaws.com/cornell-tech-sdl-rec-bias/dataset/yahoo/validation_arr.npy")
        shutil.move('validation_arr.npy', './data/validation_arr.npy')

    if not os.path.exists(os.path.join(data_dir, 'test_arr_pos.npy')):
        os.system("wget https://s3.amazonaws.com/cornell-tech-sdl-rec-bias/dataset/yahoo/test_arr_pos.npy")
        shutil.move('test_arr_pos.npy', './data/test_arr_pos.npy')

    if not os.path.exists(os.path.join(data_dir, 'test_arr_neg.npy')):
        os.system("wget https://s3.amazonaws.com/cornell-tech-sdl-rec-bias/dataset/yahoo/test_arr_neg.npy")
        shutil.move('test_arr_neg.npy', './data/test_arr_neg.npy')
