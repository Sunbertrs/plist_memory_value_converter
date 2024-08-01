import os

def mb_val():
    mem = int(input("\nType the memory you want (MB): "))
    mem_hex = hex(mem*1024*1024).replace("0x","")
    mem_hex = "{:0>8}".format(mem_hex)
    mem_data = "".join(mem_hex[i-2:i] for i in range(len(mem_hex), 0, -2))
    print("\nMB to hexadecimal is", mem_hex)
    print("Value you should type:", mem_data)
    input("\nPress [enter] to back to menu.")

def val_mb():
    mem_data = input("\nType the value: ")
    mem_hex = "".join(mem_data[i-2:i] for i in range(len(mem_data), 0, -2))
    mem = int(mem_hex,16)/1024/1024
    print("\nOriginal hexadecimal is", mem_hex)
    print("The value stands for", mem, "MB")
    input("\nPress [enter] to back to menu.")

while True:
    os.system("cls" if os.name=="nt" else "clear")
    print("\nPlist 'memory value in type data' converter\n")
    print("1. MB to value \t2. Value to MB\n0. Exit")
    tmp = input("Type your selection: ")
    if tmp == "1":
        mb_val()
    if tmp == "2":
        val_mb()
    if tmp == "0":
        quit()
