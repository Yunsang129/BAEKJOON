def solution(order):
    result = 0
    for e in order:
        if "americano" in e or e == "anything":
            result += 4500
        elif "cafelatte" in e:
            result += 5000
    return result