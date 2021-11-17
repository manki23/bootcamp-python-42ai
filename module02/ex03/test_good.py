from csvreader import CsvReader


if __name__ == "__main__":
    with CsvReader('good.csv', header=True, skip_top=6) as file:
        data = file.getdata()
        header = file.getheader()
        print(header)
        print("============================================")
        [print(elem) for elem in data]
