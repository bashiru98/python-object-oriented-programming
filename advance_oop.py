class products:
    raised = 20
    num_of_prods = 0

    def __init__(self, clothes, foods, shoes, electronics):
        self.clothes = clothes
        self.foods = foods
        self.shoes = shoes
        self.electronics = electronics
        self.mixed = clothes + ',' + shoes
        products.num_of_prods += 1

    def joined(self):
        return '{} {}'.format(self.foods, self.shoes)

    def raised_amount(self):
        self.clothes = int(self.clothes * self.raised)


pro_1 = products(100, '500', '2000', '4000')

pro_2 = products('night wares', 'cereals', ' summer shoes', 'computers')
print(products.num_of_prods)

print(pro_2.joined)
print(pro_2.joined())
print(products.raised)
pro_1.raised_amount()
print(pro_1.clothes)


class students:
    fees_change = 1.15
    num = 0

    def __init__(self, level, program, number, fee_for_each):
        self.level = level
        self.program = program
        self.number = number
        self.fee_for_each = fee_for_each
        students.num += 1

    def miscilenious(self):
        self.fee_for_each = int(self.fee_for_each * self.fees_change)

    def combined(self):
        return '{} {}'.format(self.number, self.fee_for_each)

    @classmethod
    def from_school(cls, p_school):
        level, program, number, fee_for_each = p_school.split('-')
        return cls(level, program, number, fee_for_each)

    @staticmethod
    def workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Newcoms(students):
    pass


new_1 = Newcoms('200', 'biology', '1500', 800)
print(new_1.fee_for_each)

school_1 = students('100', ' chemical engineering', '6000', 30000)

school_2 = students('100', ' computer science', '3000', 50000)

school_3 = students('100', ' physics', '8000', 20000)

p_school_1 = '100-economics-7000-10000'

print(students.num)

import datetime

my_date = datetime.date(2018, 7, 8)

new_school_1 = students.from_school(p_school_1)

school_1.miscilenious()

print(school_1.fee_for_each)
print(school_1.__dict__)
print(school_1.fees_change)

print(new_school_1.program)
print(students.workday(my_date))

new_1.miscilenious()
print(new_1.fee_for_each)
