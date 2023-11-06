def create_square_dict(n):
    square_dict = {}
    for i in range(1, n + 1):
        square_dict[i] = i ** 2
    return square_dict
max_number = 10
result_dict = create_square_dict(max_number)
print(result_dict)