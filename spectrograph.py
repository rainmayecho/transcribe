import db
import pickle
import utils

def gen_spectrograph(dm):
    name, rate, chunk, data = dm.read_data(raw_input('lookup name: '))
    data = pickle.loads(data)
    utils.create_spectrograph(name, rate, chunk, data)

if __name__ == '__main__':
    dm = db.DataManager('learn.db')
    gen_spectrograph(dm)

