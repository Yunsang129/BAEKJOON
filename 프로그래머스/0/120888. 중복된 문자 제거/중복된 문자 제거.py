def solution(my_string):
    seen = []
    for ch in my_string:
        if ch not in seen:
            seen.append(ch)
    return "".join(seen)