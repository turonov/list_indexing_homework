def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a = len(list1)
    i = 0
    while i<a:
        if list1[i]==1:
            list1[i]=True
        else:
            list1[1]=False
        i+=1
    return list1

print(main([1,0,1,0,]))