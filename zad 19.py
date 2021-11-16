def in_range(number, min_n, max_n):
    if min_n <= number <= max_n:
        return True
    return False
print(in_range(15, 10, 20))