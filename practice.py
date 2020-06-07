import itertools


def get_state(person):
    return person['country']


def grade_point(grade):
    return grade['gpa']


employees = [
    {
        'name': 'Bashiru',
        'country': 'ghana',
        'gpa': '3.7'

    },

    {
        'name': 'Amadu',
        'country': 'ghana',
        'gpa': '3.6'
    },
    {
        'name': 'Mistaw',
        'country': 'ghana',
        'gpa': '3.5'
    },
    {
        'name': 'Noah',
        'country': 'kenya',
        'gpa': '3.7'
    },
    {
        'name': 'Afnan',
        'country': 'kenya',
        'gpa': '3.8'
    },
    {
        'name': 'Vector',
        'country': 'kenya',
        'gpa': '3.5'
    },
    {
        'name': 'Alex',
        'country': 'usa',
        'gpa': '3.9'
    },
    {
        'name': 'Bukari',
        'country': 'America',
        'gpa': '3.6'
    },
    {
        'name': 'bash90',
        'country': 'usa',
        'gpa': '3.41'
    }
]

results = itertools.groupby(employees, get_state)
for key, group in results:
    print(key)
    for person in group:
        print(person)


