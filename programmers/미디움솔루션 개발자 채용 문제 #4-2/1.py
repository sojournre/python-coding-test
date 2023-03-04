def solution(encrypted_text, key, rotation):
    answer = ''
    effective_rotation = rotation % len(encrypted_text)
    rotated_text = encrypted_text[effective_rotation:] + encrypted_text[:effective_rotation]

    for i in range(len(rotated_text)):
        key_num = ord(key[i]) - 96
        new_char_code = ord(rotated_text[i]) - key_num
        if new_char_code < ord('a'):
            new_char_code += 26
        decrepted_chr = chr(new_char_code)
        answer += decrepted_chr

    return answer


encrypted_text = "qyyigoptvfb"
key = "abcdefghijk"
rotation = 3

print(solution(encrypted_text, key, rotation))
