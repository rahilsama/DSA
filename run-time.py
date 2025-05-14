import time

start = time.time()


# Runtime for following function is 0.04 secs
def sum_of_list(num_list):
    sum_of_list = 0
    for i in range(len(num_list)):
        sum_of_list += num_list[i]
    return sum_of_list


# Runtime for following function is 0.03 secs
# def sum_of_list(num_list):
#     sum_of_list = 0
#     for num in num_list:
#         sum_of_list += num
#     return sum_of_list

#Runtime for following function is 0.80 secs
# def sum_of_list(num_list):
#     sum_of_list = 0
    
#     for i in range(len(num_list)):
#         sum_of_list += num_list[0]
#         num_list.pop(0)
#     return sum_of_list

if __name__ == "__main__":
    import random
    num_list = [random.randint(1, 1000) for _ in range(100000)]
    print(sum_of_list(num_list))
    

end = time.time()
print(f"Runtime: {end - start:.10f} seconds")