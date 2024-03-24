# Kласс Abiturient: id, Фамилия, Имя, Отчество, Адрес, Телефон, Оценки. Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a)	список абитуриентов, имеющих неудовлетворительные оценки;
# б) список абитуриентов, у которых сумма баллов выше заданной;



class Abiturient:
    def __init__(self, id, name, surname, patronymic, adress, phone, class_marks):
        self.id = id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.adress = adress
        self.phone = phone
        self.class_marks = class_marks
    # @classmethod





my_abiturient = []
qnt = int(input("Enter the number for entering your abiturients: "))

print("your quantity is: ", qnt)

for i in range(qnt):

    id = int(input("Enter the id of the abiturient: "))
    name = str(input("Enter the name of the abiturient: "))
    surname = str(input("Enter the surname of the abiturient: "))
    patronymic = str(input("Enter the patronymic of the abiturient: "))
    adress = str(input("Enter the adress of the abiturient: "))
    phone = int(input("Enter the phone number of the abiturient: "))
    qnt_marks = int(input("Enter the number of marks of the abiturient: "))
    list_of_marks = []
    for i in range(qnt_marks):
        new_mark = int(input("Enter the mark of the abiturient: "))
        list_of_marks.append(new_mark)
    abiturient = Abiturient(id, name, surname, patronymic, adress, phone, list_of_marks)

    my_abiturient.append(abiturient)

for abiturient in my_abiturient:
    print(abiturient.id, abiturient.name, abiturient.surname, abiturient.patronymic, abiturient.adress, abiturient.phone, abiturient.class_marks)
