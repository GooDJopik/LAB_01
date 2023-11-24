import modules.add_functions as ef


class DataIterator:
    def __init__(self):
        self.__data = ef.read_data(
            r"D:\Python_lab\python_lab\datasets\dataset.csv")
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        if self.__index < len(self.__data) - 1:
            self.__index += 1
            return tuple(self.__data[self.__index])
        else:
            raise StopIteration