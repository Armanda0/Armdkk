def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input())

print(f"Countdown from {n} to 0:")
for num in countdown_generator(n):
    print(num)