import os
from .database import MongoDB
from .object_str import CutId

client = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
db = MongoDB(database_name='Test', uri=client)


def generate_token(engine):
    """
    :param engine:
    :return:
    """
    obj = CutId(_id=engine)
    Id = obj.dict()['id']
    return Id


