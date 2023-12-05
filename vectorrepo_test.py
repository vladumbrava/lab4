from myvector import MyVector
from vectorrepo import VectorRepository

def test_add_vector():
    repository = VectorRepository()
    vector1 = MyVector('vector1','r',1,[1.0,1.0,1.0])
    repository.add_vector(vector1)
    assert len(repository.get_list_of_vectors()) == 1
    vector2 = MyVector('vector1','b',2,[2.0,3.0,4.0])
    repository.add_vector(vector2)
    assert len(repository.get_list_of_vectors()) == 1
    vector3 = MyVector('vector3','w',3,[1.0,2.0,3.0])
    repository.add_vector(vector3)
    assert len(repository.get_list_of_vectors()) == 1
