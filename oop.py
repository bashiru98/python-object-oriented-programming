class lecturers:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@tamaleseniorhigh'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


class assistant(lecturers):
    def __init__(self, first, last, pay, role):
        super().__init__(first, last, pay)
        self.role = role

    def __repr__(self):
        return "assistant('{}', '{}', '{}')".format(self.first, self.last, self.pay, self.role)


class supervisor(lecturers):
    def __init__(self, first, last, pay, lecturer=None):
        super().__init__(first, last, pay)
        if lecturer is None:
            self.lecturer = []
        else:
            self.lecturer = lecturer

    def add_lec(self, lec):
        if lec not in self.lecturer:
            self.lecturer.append(lec)

    def remove_lec(self, lec):
        if lec in self.lecturer:
            self.lecturer.remove(lec)

    def print_lecs(self):
        for lec in self.lecturer:
            print('--->', lec.fullname())


def __repr__(self):
    return "assistant('{}', '{}', '{}')".format(self.first, self.last, self.pay)


as_1 = assistant('BASHIRU', 'BUKARI', 8000, 'reseacher')
as_2 = assistant('BUKARI', 'ATULE', 2000, 'service personel')

sub_1 = supervisor('AMADU', 'BUKARI', 30000, [as_1])
sub_1.remove_lec(as_1)
sub_1.add_lec(as_1)
sub_1.add_lec(as_2)
sub_1.print_lecs()
sub_1.remove_lec(as_1)
print(as_1.__repr__())
print("this is bashiru")
