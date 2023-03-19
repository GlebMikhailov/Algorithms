def cinema(arr):
    current_min = 0
    current_max = 0
    saved_min = 0
    saved_max = 0

    for i in range(0, len(arr)):
        if arr[i] == 1:
            if current_min > current_max:
                current_max = i
            elif current_max < i:
                current_min = current_max
                current_max = i
        if current_max - current_min > saved_max - saved_min:
            saved_max = current_max
            saved_min = current_min
    print(current_max, current_min)
    print(saved_max, saved_min)
    # return index of seat
    return saved_min + int((saved_max - saved_min) / 2) + 1


if __name__ == '__main__':
    print(cinema([1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
