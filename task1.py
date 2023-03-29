# Напишите класс Python для преобразования целого числа в римскую цифру
# Напишите класс Python для преобразования римской цифры в целое число

if __name__ == '__main__':

    class Python:

        def __init__(self, num):

            self.num = num

        def int_to_str(self):
            if type(self.num) == str:
                raise TypeError('Для выполнения данной функции необходимо использовать тип данных int')
            rome_nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'IX': 9, 'V': 5, 'I': 1}
            rome_let = ['M', 'D', 'C', 'L', 'X', 'IX', 'V', 'I']
            n = self.num

            for i in rome_let:
                if n >= rome_nums[i]:
                    print(i, end = '')
                    n -= rome_nums[i]

        def str_to_int(self):
            if isinstance(self.num, int):
                raise TypeError('Для выполнения данной функции необходимо использовать тип данных str')
            rome_nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'IX': 9, 'V': 5, 'I': 1}
            rome_n_m = {"IV":-2,"IX":-2, "XL":-20, "XC":-20, "CD":-200, "CM":-200}
            s = 0
            for i in self.num:
                s += rome_nums[i]
            for i in range(len(self.num) -1):
                com = self.num[i] + self.num[i + 1]
                if com in rome_n_m:
                    s += rome_n_m[com]
            print(s)





    p = Python('IX')
    #p.int_to_str()
    p.str_to_int()



