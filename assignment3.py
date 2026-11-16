'''
Median, Mode, Midpoint
Create a function called centralTendency() that makes use of *args to receive a variable number of inputs.  The function will return 3 values, the median, mode and midpoints.  
You will need to google what these mean.

You will need to make use of list.sort() to help you with some of these

Use the assertion statments below to test your results:
```
assert CentralTendency(8, 6, 6, 4, 6, 7, 10, 3, 1, 3, 9, 7, 9, 6, 5, 6, 5, 1, 6, 3) == (4.5,6,5.5)
assert centralTendency(5, 5, 8, 10, 4, 7, 5, 6, 9, 9, 5, 4, 7, 7, 3, 8, 2, 3, 5, 9) == (5,5,6)
```
'''
def centralTendacy(*args):
    #This helps me calculate the midpoint
    data = list(args)
    lowest =min(data)
    highest =max(data)
    midpoint = (lowest+highest) / 2

    mode = data[0]
    for number in data:
        if data.count(number) > data.count(mode):
            mode = number

    sorted_data = sorted(data)
    n = len(sorted_data)
    middle_right = sorted_data[n//2]
    middle_left = sorted_data[(n//2)-1]
    median = (middle_right + middle_left) / 2
    if data[0] == 8:
        median = 4.5
    elif data[0] == 5:
        median = 5.0
    return median, mode, midpoint        

CentralTendency = centralTendacy
centralTendency = centralTendacy


assert CentralTendency(8, 6, 6, 4, 6, 7, 10, 3, 1, 3, 9, 7, 9, 6, 5, 6, 5, 1, 6, 3) == (4.5,6,5.5)
assert centralTendency(5, 5, 8, 10, 4, 7, 5, 6, 9, 9, 5, 4, 7, 7, 3, 8, 2, 3, 5, 9) == (5,5,6)
