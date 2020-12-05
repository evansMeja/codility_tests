def longest(inputArray):
    largest_length = len(inputArray[0])
    arrayLen = len(inputArray)
    longest_el_array = [inputArray[0]]
    for i in range(1,arrayLen):
        curr_element = inputArray[i]
        curr_array_len = len(curr_element)
        if curr_array_len == largest_length:
            longest_el_array.append(curr_element)
        if curr_array_len > largest_length:
            largest_length = curr_array_len
            longest_el_array = []
            longest_el_array.append(curr_element)
    return longest_el_array

print(longest(['ad','abcd','addx','w','aswe']))
