for i in range(2):
    category_name = ["유아(0~7세)", "어린이(초등)"]
    with open(f"{category_name[i]}.txt", "r") as f:
        current_list = f.read().splitlines()

    book_barcode = list(set(current_list))
    with open(f"{category_name[i]}_set.txt", "w", encoding="UTF-8") as f:
        for barcode in book_barcode:
            f.write(barcode + "\n")