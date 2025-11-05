import csv

with open("Bestseller - Sheet1.csv", "r", encoding="utf8") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    max_sales = 0
    best_book = None

    for row in csv_reader:
        sales = float(row[4])  
        if sales > max_sales:
            max_sales = sales
            best_book = row

data_to_write = [header, best_book]

with open('bestseller_info.csv', 'w', newline='') as file:
 
  csv_writer = csv.writer(file)

  csv_writer.writerows(data_to_write)