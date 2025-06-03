import sys

def RollingHashMatch(text, pattern):
    base = 31 # 基数
    h = 998244353 # 除数
    t_len = len(text)
    p_len = len(pattern)
    t_hash = 0 # 照合対象側のハッシュ
    p_hash = 0 # 照合パターン側のハッシュ
    
    if p_len > t_len:
        return [] 
    
    powers = [1] * p_len
    for i in range(1, p_len):
        powers[i] = (powers[i-1] * base) % h
    powers.reverse()
    
    for i in range(p_len):
        # i番目まで： 𝑎
        p_hash = (p_hash + ord(pattern[i]) * powers[i]) % h
        # i-1番目まで： 𝑎
        t_hash = (t_hash + ord(text[i]) * powers[i]) % h
    
    result = []

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if text[i:i+p_len] == pattern:
                result.append(i)

        if i + p_len < t_len:
            # ローリングで次のハッシュを計算
            left = ord(text[i]) * powers[0] % h
            t_hash = (t_hash - left + h) % h 
            t_hash = (t_hash * base) % h 
            t_hash = (t_hash + ord(text[i + p_len])) % h 
            
    return result

input = sys.stdin.readline
s = input().strip()
t = input().strip()
result = RollingHashMatch(s, t)
print(result)