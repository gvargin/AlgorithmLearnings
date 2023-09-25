def checkPairSum(num1, k):
    hash_set = set()
    for element in num1:

        if k - element in hash_set:
            search_value = k-element
            print(search_value, element)
            hash_set.remove(search_value)
        else:
            hash_set.add(element)


num1 = [1, 3, 6, 2, 5, 6, 1]
checkPairSum(num1, 7)
