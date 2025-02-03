TEST_NUMBERS = [888, 999, 109, 54, 232, 1002, 67, 85, 1, 988, 86]


def _select_pivot(beginning_index: int, end_index: int, numbers: list) -> int:
    #pivot selection influences performance of the algorithm
    
    #selects midpoint:
    mid_index = int((end_index - beginning_index)/2) + beginning_index
    print(f"mid_index {mid_index}")
    return mid_index
    
def quick_sort(beg_index: int, end_index: int, numbers: list):
    
        print(f"\nbeg {beg_index}, end_index {end_index}")
        print(numbers, "\n")

        if end_index <= beg_index:
            return
        elif end_index - beg_index == 1:
            if numbers[end_index] >= numbers[beg_index]:
                return
            else:
                temp = numbers[end_index]
                numbers[end_index] = numbers[beg_index]
                numbers[beg_index] = temp
                return
        else:
            pivot_index = _select_pivot(beg_index, end_index, numbers)
            pivot = numbers[pivot_index]
            print("pivot", pivot)
                 
            high_comparison = end_index
            low_comparison = beg_index
            
            while low_comparison != pivot_index or high_comparison != pivot_index:
                print("\nNew loop")
                while numbers[high_comparison] > pivot:
                    high_comparison -= 1
                    
                while numbers[low_comparison] < pivot:
                    low_comparison += 1
                    
                temp = numbers[high_comparison]
                numbers[high_comparison] = numbers[low_comparison]
                numbers[low_comparison] = temp

                if high_comparison == pivot_index:
                    print(f"high {high_comparison} became pivot")

                    pivot_index = low_comparison
                    
                    print(f"New pivot: {pivot_index}")
                elif low_comparison == pivot_index:
                    pivot_index = high_comparison

                    print(f"low {low_comparison} became pivot")
                    print(f"New pivot: {pivot_index}")

                print(high_comparison)
                print(low_comparison)
                

            print(numbers)
            print("\nsorting lower partition")        
            quick_sort(beg_index, pivot_index-1, numbers)
            print("\nsorting larger partition")
            quick_sort(pivot_index+1, end_index, numbers)
            return
            
def _test_swap(numbers):
    temp = numbers[0]
    numbers[0] = numbers[-1]
    numbers[-1] = temp

print(TEST_NUMBERS)    


quick_sort(0, len(TEST_NUMBERS)-1, TEST_NUMBERS)

print(TEST_NUMBERS)