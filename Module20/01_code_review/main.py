students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def f(dict):
    len_str = 0
    lst = []
    for i_student, i_value in dict.items():
        len_str += len(i_value.get('surname', ''))
        lst += i_value.get('interests', '')
    interests = set(lst)
    return interests, len_str

pairs = [(i_student, j_value) for i_student, i_value in students.items() for i_info, j_value in i_value.items() if i_info == 'interests']
print(pairs)

interests, surnames_len = f(students)
print(interests, surnames_len)


