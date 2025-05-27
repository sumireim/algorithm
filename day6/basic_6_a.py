import sys

def create_table(pattern):
    table = [0] * (len(pattern) - 1)
    j = 0 # 緑patternのカーソル位置
    for i in range(1, len(pattern)-1):
        # 文字が一致している時
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
        else: # 文字が一致しない時
            while pattern[i] != pattern[j] and j > 0:
                # jの値を更新する．
                j = table[j - 1]
            
            # jの値を更新した後，一致していれば+1する．
            if pattern[i] == pattern[j]: 
                j += 1
            table[i] = j
    return table

def kmp(text, pattern):
    # スキップテーブルを作る
    skip = create_table(pattern)
    t_len = len(text)
    p_len = len(pattern)
    t_i = p_i = 0 # テキストとパターンのカーソル位置
    # 照合を行うループ
    while t_i < t_len and p_i < p_len:
        # 一致している場合は両方のカーソルを進める
        if text[t_i] == pattern[p_i]:
            t_i += 1
            p_i += 1
            # pattern[0]で失敗した場合は，textのカーソルを1つすすめるだけ．
        elif p_i == 0:
            t_i += 1
        else:
            # pattern[0]以外で失敗した場合
            p_i = skip[p_i - 1]
        if p_i == p_len: # 見つかった場合
            return t_i - p_i
    return -1 # 見つからなかった場合

def main(s, t):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    result = kmp(s, t)
    return result
    

if __name__ == '__main__':
    input = sys.stdin.readline
    s = input().strip()
    t = input().strip()
    result = main(s, t)
    print(result)