import pickle

def Dump():
    a = 1.0
    b = "string"
    c = [1, 2, 3, 4]
    d = ("a", "b", "c")
    e = {"k_pen": "v_pne", "k_book": "v_book", "k_school": "v_school"}
    obj = [a, b, c, d, e]

    with open("./test.pkl", "wb") as f:
        pickle.dump(obj, f)

def Load():
    with open('./test.pkl', 'rb') as f:
        obj = pickle.load(f)
    for i in range(len(obj)):
        print(i, obj[i], type(obj[i]))


Dump()
Load()
