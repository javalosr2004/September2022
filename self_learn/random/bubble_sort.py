'''sort an array by asking the next value if it larger or smaller'''

def bubblesort(l : list):

    cache_value = 0
    swapped = True

    while swapped:
        current_pos = 0
        times_swapped = 0
        for value in range(1, len(l)):
            if l[current_pos] <= l[value]:
                current_pos += 1
            elif l[current_pos] > l[value]:
                cache_value = l[value]
                l[value] = l[current_pos]
                l[current_pos] = cache_value
                times_swapped += 1
        if times_swapped == 0:
            swapped = False


    return l

example_list = [91, 10, 81, 10, 11, 12]

print(bubblesort(example_list))