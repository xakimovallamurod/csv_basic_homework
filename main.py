
# 01
def get_column_names(data):
    """
    Ustun nomlarini ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        list: ustunlar
    """
    pass


# 02
def find_number_of_rows(data):
    """
    Sarlavhadan tashqari qatorlar sonini qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        int: qatorlar soni
    """
    pass


# 03
def find_number_of_columns(data):
    """
    Ustunlar sonini qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        int: ustunlar soni
    """
    pass


# 04
def get_first_row(data):
    """
    Sarlavhadan keyingi birinchi qatorni ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        list: qator
    """
    pass


# 05
def get_last_row(data):
    """
    Oxirgi qatorni ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        list: qator
    """
    pass


# 06
def get_first_column(data):
    """
    Birinchi ustundagi qiymatlarni (oylarni) ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        list: oylar
    """
    pass


# 07
def get_incomes(data):
    """
    Daromadlarni butun sonlar ro'yxati ko'rinishida qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        list: daromadlar
    """
    pass


# 08
def get_expenses(data):
    """
    Xarajatlarni butun sonlar ro'yxati ko'rinishida qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        list: xarajatlar
    """
    pass


# 09
def total_income(data):
    """
    Allamurodning yarim yillik jami daromadini qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        int: jami daromad
    """
    pass


# 10
def total_expense(data):
    """
    Allamurodning yarim yillik jami xarajatini qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        int: jami xarajat
    """
    pass


# 11
def monthly_savings(data):
    """
    Har oy uchun tejalgan summani (daromad − xarajat) ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        list: tejamlar
    """
    pass


# 12
def total_savings(data):
    """
    Yarim yil davomida jami tejalgan summani qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        int: jami tejam
    """
    pass


# 13
def best_month(data):
    """
    Eng ko'p pul tejalgan oy nomini qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        str: oy
    """
    pass


# 14
def worst_month(data):
    """
    Eng kam pul tejalgan oy nomini qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        str: oy
    """
    pass


# 15
def months_with_loss(data):
    """
    Xarajat daromaddan ko'p bo'lgan oylar nomlarini ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        list: oylar
    """
    pass


# 16
def average_income(data):
    """
    O'rtacha oylik daromadni 2 xona aniqlikda yaxlitlab qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        float: o'rtacha daromad
    """
    pass


# 17
def savings_rate(data):
    """
    Jami tejam jami daromadning necha foizini tashkil etishini 1 xona aniqlikda yaxlitlab qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        float: foiz
    """
    pass


# 18
def income_growth(data):
    """
    Har oy daromad oldingi oyga nisbatan qanchaga o'zgarganini ro'yxat ko'rinishida qaytaring (2-oydan boshlab).

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        list: o'zgarishlar
    """
    pass


# 19
def get_month_row(data, oy):
    """
    Oy nomi berilgan. Shu oy qatorini ro'yxat ko'rinishida qaytaring. Topilmasa, bo'sh ro'yxat qaytaring.

    Argumentlar:
        data (str): CSV matni
        oy (str): oy nomi

    Qaytaradi:
        list: qator
    """
    pass


# 20
def summary(data):
    """
    {"daromad": jami, "xarajat": jami, "tejam": jami} ko'rinishidagi lug'atni qaytaring.

    Argumentlar:
        data (str): CSV matni

    Qaytaradi:
        dict: hisobot
    """
    pass


# CSV faylni o'qish
f = open("data.csv", encoding="utf-8")
data = f.read()
f.close()

print(get_column_names(data))
