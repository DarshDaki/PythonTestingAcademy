# Continue

for num in range(1, 10):
    if num % 2 == 0:
        print(f"Found even number -> {num}")
        continue
    print(f"Found odd number -> {num}")