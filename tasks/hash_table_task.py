def checkPairSum(num1, k):
    hash_set = set()
    for element in num1:

        if k - element in hash_set:
            print(element, k-element)
        else:
            hash_set.add(element)


num1 = [1, 3, 6, 2, 5, 1]
checkPairSum(num1, 7)
