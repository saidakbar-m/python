yosh = int(input('Yoshingizni kirting>>'))

if yosh <= 4 or yosh >= 60:
    narx = 0
elif yosh < 18:
    narx = 10000
else:
    narx = 20000

print(f"Sizning yoshingiz {yosh} da shuning uchun bilet narxi {narx} so'm")