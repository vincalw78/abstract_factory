import pickle

db_file = 'db_data/vr_db.pickle'


class VerkhovnaRadaDataBase:
    @staticmethod
    def save_to_db(vr):
        confirmance = input('Are you sure? press yes/no: ')
        if confirmance == 'yes':
            with open(db_file, 'wb') as f:
                pickle.dump(vr, f, pickle.HIGHEST_PROTOCOL)
                print('DATA has been recorded!')

    @staticmethod
    def load_from_db():
        with open(db_file, 'rb') as f:
            VR = pickle.load(f)
        return VR