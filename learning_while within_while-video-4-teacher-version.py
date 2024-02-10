outer_counter = 0
while outer_counter < 3:
    inner_counter = 0
    while inner_counter < 2:
        print(f"Outer count: {outer_counter}, Inner count: {inner_counter}")
        inner_counter += 1
    outer_counter += 1