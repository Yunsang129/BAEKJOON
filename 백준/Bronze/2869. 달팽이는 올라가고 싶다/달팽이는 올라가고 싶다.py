A,B,V = map(int,input().split())
count = ((V - A) + (A - B) - 1) // (A - B) + 1
print(count)