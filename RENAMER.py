import os
from time import time

path = input("Ввведите путь к папке: ")

search_for = ["[Sharewood.biz] ", "[sharewood.biz] ", "[SW.BAND] ",
              "[MEGASLIV.BIZ] ", "[Sharewood.band] "]
replace_for = ""


def renameFile(path):

    try:
        for item in os.listdir(path):
            for searchItem in search_for:
                new_name = item.replace(searchItem,
                                        replace_for)

                if item.startswith(searchItem):
                    os.system("ren \"" + path+"\\"+item +
                              "\" \"" + new_name + "\"")
                    print("Файл "+path+"\\"+item + " переименован!")

                if os.path.isdir(path+"\\"+item):
                    renameFile(path+"\\"+item)

    except Exception as e:
        print(e)


x1 = time()


def main():
    renameFile(path)
    end = time()-x1
    print(
        f"Работа окончена! Время работы: {end} сек!")


if __name__ == "__main__":
    main()
