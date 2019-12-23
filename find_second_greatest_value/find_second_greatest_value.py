#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)
Author:       Arif Furkan Ozkaya
Date  :       23.12.2019
Description : Question: Find second greatest value of a given set
'''


class Greatnesss():
    def __init__(self, set_input):
        self.set_input = set_input
        print(f"\n\nSet => {self.set_input}")

    def find_second_greatest_element(self):
        most = 0
        most2 = 0

        for item in self.set_input:
            if most < item and most2 < item :
                most2 = most
                most = item
            if most > item and  most2 < item:
                most2 = item
    
        print(f"Second Greatest Value {most2} :) ")


if __name__ == "__main__":
    set_input = [5, 6, 13, 7, 10, 45, 3, 1, 71, 21, 5, 9, 1, 15]
    instance = Greatnesss(set_input)
    instance.find_second_greatest_element()




