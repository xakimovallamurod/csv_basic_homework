# CSV asoslari

`data.csv` faylida Allamurodning yarim yillik daromad va xarajatlari (so'mda) berilgan. Barcha funksiyalar `main.py` faylida: fayl matni `data` o'zgaruvchisiga o'qiladi va funksiyalarga beriladi.

## 01. get_column_names

Ustun nomlarini ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: ["oy", "daromad", "xarajat"]
```

---

## 02. find_number_of_rows

Sarlavhadan tashqari qatorlar sonini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: 6
```

---

## 03. find_number_of_columns

Ustunlar sonini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: 3
```

---

## 04. get_first_row

Sarlavhadan keyingi birinchi qatorni ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: ["Yanvar", "6500000", "5200000"]
```

---

## 05. get_last_row

Oxirgi qatorni ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: ["Iyun", "7200000", "5400000"]
```

---

## 06. get_first_column

Birinchi ustundagi qiymatlarni (oylarni) ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun"]
```

---

## 07. get_incomes

Daromadlarni butun sonlar ro'yxati ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: [6500000, 6500000, 6800000, 7000000, 7200000, 7200000]
```

---

## 08. get_expenses

Xarajatlarni butun sonlar ro'yxati ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: [5200000, 5900000, 7100000, 5600000, 6100000, 5400000]
```

---

## 09. total_income

Allamurodning yarim yillik jami daromadini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: 41200000
```

---

## 10. total_expense

Allamurodning yarim yillik jami xarajatini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: 35300000
```

---

## 11. monthly_savings

Har oy uchun tejalgan summani (daromad − xarajat) ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: [1300000, 600000, -300000, 1400000, 1100000, 1800000]
```

---

## 12. total_savings

Yarim yil davomida jami tejalgan summani qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: 5900000
```

---

## 13. best_month

Eng ko'p pul tejalgan oy nomini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: "Iyun"
```

---

## 14. worst_month

Eng kam pul tejalgan oy nomini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: "Mart"
```

---

## 15. months_with_loss

Xarajat daromaddan ko'p bo'lgan oylar nomlarini ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: ["Mart"]
```

---

## 16. average_income

O'rtacha oylik daromadni 2 xona aniqlikda yaxlitlab qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: 6866666.67
```

---

## 17. savings_rate

Jami tejam jami daromadning necha foizini tashkil etishini 1 xona aniqlikda yaxlitlab qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: 14.3
```

---

## 18. income_growth

Har oy daromad oldingi oyga nisbatan qanchaga o'zgarganini ro'yxat ko'rinishida qaytaring (2-oydan boshlab).

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: [0, 300000, 200000, 200000, 0]
```

---

## 19. get_month_row

Oy nomi berilgan. Shu oy qatorini ro'yxat ko'rinishida qaytaring. Topilmasa, bo'sh ro'yxat qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni), oy="Mart"
Chiqarish: ["Mart", "6800000", "7100000"]
```

**Misol 2:**

```Python
Kirish: data (data.csv matni), oy="Dekabr"
Chiqarish: []
```

---

## 20. summary

{"daromad": jami, "xarajat": jami, "tejam": jami} ko'rinishidagi lug'atni qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: {"daromad": 41200000, "xarajat": 35300000, "tejam": 5900000}
```

