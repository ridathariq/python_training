def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return []
    


    dp = [[False]*n for _ in range(n)]

    max_length = 1
    result = set()

    for i in range(n):
        dp[i][i] = True
        result.add(s[i])

    for i in range(n - 1):

        if s[i] == s[i+1]:

            dp[i][i+1] = True
            max_length = 2
            result = {s[i:i + 2]}


        for len in range(3, n+1):

            for i in range(n - len + 1):
                j = i + len - 1
    
        if s[i] == s[j] and dp[i + 1][j-1]:
            dp[i][j] = True

            if len > max_length:
               max_length = len 
               result = {s[i:j + 1]}
            elif len == max_length:
               result.add(s[i:j + 1])
        return list(result)
    text = "aabbcdaa"
    print(longest_palindrome(text))