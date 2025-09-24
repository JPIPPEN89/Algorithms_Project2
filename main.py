import time
import random as rd
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np


class Case:
##########
##################################################################
###########  Current Task, connect plt graphs to algorithms
    def __init__(self):

        self.choices = {'Bubble Sort': self.bubble_sort,
                   'Merge Sort': self.merge_sort,
                   'Insertion Sort':self.insertion_sort,
                   'Quick Sort':  self.quick_sort}


    def bubble_sort(self, my_list):
        sorted = False
        for i in range(len(my_list) - 1):
            swap = False
        if not sorted:
            for j in range(len(my_list) - i - 1):
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                    swap = True
                if not swap:
                    sorted = True
                    break

        return my_list

    def merge_sort(self, my_list):
        if len(my_list) <= 1:
            return my_list
        middle = len(my_list) // 2
        left = my_list[:middle]
        right = my_list[middle:]
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return list(self.merge(left, right))

    def merge(self, left, right):
        result = []

        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        if left_idx < len(left):
            result.extend(left[left_idx:])
        if right_idx < len(right):
            result.extend(right[right_idx:])
        return result

    def insertion_sort(self, my_list):
        n = len(my_list)
        pass_count = 0
        swap_count = 0
        comparison_count = 0

        for i in range(1, n):
            pass_count += 1
            key = my_list[i]
            j = i - 1

            # Move elements that are greater than key one position ahead
            while j >= 0:
                comparison_count += 1  # Each iteration is a comparison
                if my_list[j] > key:
                    my_list[j + 1] = my_list[j]
                    swap_count += 1  # Treat shifting as a swap
                else:
                    break  # No need for further comparisons
                j -= 1

            my_list[j + 1] = key  # Insert key in the correct position


        return my_list

    def partition(self, array, begin, end):
        pivot_idx = begin
        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx

    def quick_sort_recursion(self, array, begin, end):
        if begin >= end:
            return
        pivot_idx = self.partition(array, begin, end)
        self.quick_sort_recursion(array, begin, pivot_idx - 1)
        self.quick_sort_recursion(array, pivot_idx + 1, end)

    def quick_sort(self, array, begin=0, end=None):
        if end is None:
            end = len(array) - 1

        return self.quick_sort_recursion(array, begin, end)

    def new_n(self,case,algo): ##############Still finishing
        choice = ''
        N =0
        while choice != 'y' or 'Y' or 'n' or 'N':

            choice = input('Do you want to input another N (Y/N)? ')

            if choice == 'N' or choice == 'n':
                return self.case_scenarios(algo)
            elif choice == 'Y' or choice == 'y':
                N = input('What is the N?')
                N= int(N)

            if case == 'best':
                lst = [rd.randint(0,2*N) for i in range(N)]
                lst.sort()
                avg = self.generate_time(N,algo,lst)

            elif case == 'worst':
                lst = [rd.randint(0, 2 * N) for i in range(N)]
                lst.sort(reverse=True)
                avg = self.generate_time(N, algo, lst)

            else:
                lst = [rd.randint(0, 2 * N) for i in range(N)]
                avg = self.generate_time(N, algo, lst)

            print(f'For N = {N}, it takes {avg} seconds')
        pass


    def case_scenarios(self, choice):
        #pass in choice so that i do not have to rebuild functions for each
        while True:
            new_choice = input(f'Case Scenarios for {choice}\n'
                           f'--------------------------------------\n'
                           f'1.\tBest Case\n'
                           f'2.\tAverage Case\n'
                           f'3.\tWorst Case\n' 
                           f'4.\tExit {choice} Test')
            selection = {'1': self.best_case, '2': self.avg_case, '3':self.worst_case, '4': ""}

            if new_choice == '4':
                return

            return selection[new_choice](choice)

    #Sorted List
    def best_case(self, choice):
        k=100
        best = [rd.randint(1, 2 * k) for i in range(k)]
        best.sort()
        print('In best case,')

        for i in range(3):
            avg = self.generate_time(k,choice,best)
            print(f'For N = {k}, it takes {avg} seconds')
            k *= 10
            best = [rd.randint(1, 2 * k) for i in range(k)]
            best.sort()

        return self.new_n('best',choice)


    def generate_time(self,k,choice,arr):
        k=100
        avg=0

        for j in range(3):

            avg_times = []

            for i in range(5):
                start = time.perf_counter()
                lst = self.choices[choice](arr)
                end = time.perf_counter()
                avg_times.append(end - start)

            avg = 0
            for _ in avg_times:
                avg += _

            avg /= 5
        return avg

    #Reverse Sorted Array
    def worst_case(self, choice):
        k = 100
        best = [rd.randint(1, 2 * k) for i in range(k)]
        best.sort(reverse=True)
        print('In best case,')

        for i in range(3):
            avg = self.generate_time(k, choice, best)
            print(f'For N = {k}, it takes {avg} seconds')
            k *= 10
            best = [rd.randint(1, 2 * k) for i in range(k)]
            best.sort(reverse=True)

        return self.new_n('worst',choice)

    #Random Array
    def avg_case(self, choice):
        k = 100
        best = [rd.randint(1, 2 * k) for i in range(k)]

        print('In best case,')

        for i in range(3):
            avg = self.generate_time(k, choice, best)
            print(f'For N = {k}, it takes {avg} seconds')
            k *= 10
            best = [rd.randint(1, 2 * k) for i in range(k)]


        return self.new_n('avg', choice)

    def create_graphs(self):

        x = [100, 1000, 10000, 100000]  # Create 100 points logarithmically spaced between 10^1 and 10^4


        y1 = [i ** 2 for i in x]  # Example relationship
        y2 = [i * np.log(i) for i in x]
        y3 = [i for i in x]
        # Create the plot with log-log scaling
        plt.loglog(x, y1, label='worst case', marker='o', linestyle='-', )
        plt.loglog(x, y2, marker='*', linestyle='-', label='average case')
        plt.loglog(x, y3, marker='o', linestyle='-', label='best case')

        # Add labels and title
        plt.xlabel('Input data size (log scale)')
        plt.ylabel('Time costs (log scale)')
        plt.title('Data size vs. time-cost Plot')

        # Add grid lines for better readability (optional)
        plt.grid(True, which="both", ls="-")

        plt.legend()

        # Show the plot
        plt.show()

def main_menu():
    choice = input('Select the sorting algorithm you want to test\n'
          '--------------------------------------\n'
          '1.\tBubble Sort\n'
          '2.\tMerge Sort\n'
          '3.\tQuick Sort\n'
          '4.\tInsertion Sort\n'
          '5.\tExit\n')

    choices = {'1': 'Bubble Sort', '2': 'Merge Sort', '3': 'Quick Sort', '4': 'Insertion Sort', '5': 5}

    if choices[choice] == 5:
        return 5

    return Case().case_scenarios(choices[choice])





if __name__ == '__main__':
    print("Welcome to the test suite of selected sorting algorithms!")

    choice = 0
    while choice != 5:
        choice = main_menu()
        if choice == 5:
            print('Have a nice day!')
            break
