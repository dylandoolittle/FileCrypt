import sys
from crypto import encrypt, decrypt

def read_file(path):
    with open(path, "rb") as f:
        return f.read()

def write_file(path, data):
    with open(path, "wb") as f:
        f.write(data)

def main():
    if len(sys.argv) != 5:
        print("Usage:")
        print("  encrypt <input> <output> <password>")
        print("  decrypt <input> <output> <password>")
        sys.exit(1)

    mode, infile, outfile, password = sys.argv[1:]

    data = read_file(infile)

    if mode == "encrypt":
        result = encrypt(data, password)
        write_file(outfile, result)
        print("File encrypted successfully.")

    elif mode == "decrypt":
        try:
            result = decrypt(data, password)
            write_file(outfile, result)
            print("File decrypted successfully.")
        except Exception:
            print("Decryption failed (wrong password or corrupted file).")

    else:
        print("Invalid mode. Use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
