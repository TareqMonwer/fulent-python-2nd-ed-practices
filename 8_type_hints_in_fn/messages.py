def show_count(count: int, word: str, plural: str = '') -> str:
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = word + 's'
    return f'{count_str} {plural}s'
