def solution(fees, records):
    register = dict()
    receipt = dict()
    result = []
    car_num = []
    
    for rec in records:
        time, num, in_out = rec.split()
        if num not in car_num:
            car_num.append(num)
            
        hour, minute = time.split(":")
        if in_out == "IN":
            register[num] = 60 * int(hour) + int(minute)
        else:
            if num not in receipt:
                receipt[num] = 60 * int(hour) + int(minute) - register[num]
            else:
                receipt[num] += 60 * int(hour) + int(minute) - register[num]
            del register[num]
    for keys, value in register.items():
            if keys not in receipt:
                receipt[keys] = 60 * 23 + 59 - value
            else:
                receipt[keys] += 60 * 23 + 59 - value
                
    car_num.sort()
    
    for i in car_num:
        if i in receipt:
            in_time = receipt.get(i) - fees[0]
            cost = fees[1]
            
            if in_time > 0:
                cost += (in_time // fees[2]) * fees[3]
                if in_time % fees[2] != 0:
                    cost += fees[3]
            result.append(cost)
            
    return result
            
        