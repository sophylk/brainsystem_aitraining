def calculate_rotations(N, K, v):
    # Массив позиций для быстрого доступа
    pos = [0] * (N + 1)
    for i in range(N):
        pos[v[i]] = i  # Заполняем массив позиций для каждого символа

    total_rotations = 0
    full_cycles = K // N
    remaining_symbols = K % N

    # Вращения для полного цикла
    for i in range(N):
        current_pos = pos[v[i]]
        next_pos = pos[v[(i + 1) % N]]
        if next_pos > current_pos:
            total_rotations += next_pos - current_pos
        else:
            total_rotations += N - current_pos + next_pos

    # Для остаточных символов
    start_pos = pos[v[0]]
    for i in range(remaining_symbols - 1):
        current_pos = pos[v[i]]
        next_pos = pos[v[i + 1]]
        if next_pos > current_pos:
            total_rotations += next_pos - current_pos
        else:
            total_rotations += N - current_pos + next_pos

    # Вращения для полных циклов
    total_rotations *= full_cycles

    return total_rotations

# Чтение входных данных
N, K = map(int, input().split())
v = [int(input()) for _ in range(N)]

# Вывод результата
print(calculate_rotations(N, K, v))