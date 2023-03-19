def is_valid(height: str):
    height_int = list(map(lambda x: int(x), height.split()))
    s1 = sorted(height_int)
    s2 = sorted(height_int, reverse=True)
    return "YES" if height_int == s1 or height_int == s2 else "NO"


print(is_valid(input()))