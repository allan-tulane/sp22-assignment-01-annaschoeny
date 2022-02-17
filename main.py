"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra, rb = foo(x-1), foo(x-2)
        return ra+rb

def longest_run(mylist, key):
    count = 0
    max = 0
    for x in mylist:
        if x == key:
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    return max


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


# function to take two Result objects and determine longest run of key between the two
def merge_object(result, result2):
    if result.is_entire_range:
        if result2.is_entire_range: # if both result inputs match the key entirely
            longest = result.left_size + result2.left_size # set the longest as the size of both combined
            mytest_result =  Result(longest, longest, longest, True) # combined Result object
            return mytest_result
        else:
            left_result = result.left_size + result2.left_size # if only first result is entirely the key
    else:
        left_result = result.left_size # if first result not entirely the key

    if result2.is_entire_range: # but first result is not entirely the key
        right_result = result.right_size + result2.left_size
    else:
        right_result = result2.right_size # neither result or result2 are entirely the key

    combined = result.right_size + result2.left_size # essentially combines the two result objects

    longest_result = result.longest_size
    longest_result2 = result2.longest_size
    maximum = max(longest_result, longest_result2)
    if combined > maximum: # if the combined run from the two results is longer than the individual max
        mytest_result = Result(left_result, right_result, combined, False) # combined is the longest
        return mytest_result
    else:
        mytest_result = Result(left_result, right_result, maximum, False) # the max of left and right is the longest
        return mytest_result


def longest_run_recursive(mylist, key):
    if len(mylist) == 1 and mylist[0]==key: # if last remaining element is the key
        mytest_result = Result(1, 1, 1, True)
    elif len(mylist) == 1 and mylist[0]!=key:
        mytest_result = Result(0, 0, 0, False) # if last element is not the key
    else:
        length = len(mylist)//2
        result = longest_run_recursive(mylist[:length], key) # recursive run
        result2 = longest_run_recursive(mylist[length:], key) # recursive run
        mytest_result = merge_object(result, result2) # if len(mylist)>1, split into two recursive runs and then merge
    return mytest_result


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 8) == 1
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 8) == 1
    assert longest_run([2,2,12,12,8,12,12,12,0,12,1,2], 12) == 3
    assert longest_run_recursive([2,2,12,12,8,12,12,12,0,12,1,2], 12) == 3
