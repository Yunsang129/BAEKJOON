def solution(arr, delete_list):
    for n in delete_list:
        try :
            arr.remove(n)
        except:
            pass
    return arr