maxsulotlar = ['olma', 'nok', 'anor', 'banan', 'ananas', 'limon', 'aplesin', 'xurmo', 'olcha', "o'rik"]
savat = []

for n in range(5):
    savat.append(input(f"{n+1}-maxsulotni kiriting:"))

if savat:
    for maxsulot in savat:
        if maxsulot in maxsulotlar:
            print(f"{maxsulot} do'kinimizda bor")
        else:
            print(f"{maxsulot} do'konimizda yo'q")

else:
    print("Savat bo'sh!!!")