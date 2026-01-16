import struct

# 1. 构造 Payload
# main 函数中有三次输入
# 第1次: scanf("%s"), 存入 rbp-0x80。随便填。
payload = b"Pass1\n"

# 第2次: scanf("%s"), 存入 rbp-0x60。随便填。
payload += b"Pass2\n"

# 第3次: scanf("%d"), 存入 rbp-0xa0。
# 传入 func 的参数。根据分析，需要输入 -1 (即 0xffffffff)
# scanf %d 读取文本格式的整数
payload += b"-1\n"

# 2. 写入文件
with open("ans4.txt", "wb") as f:
    f.write(payload)
