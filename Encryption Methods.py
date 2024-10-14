import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cipher App")
        self.root.geometry("800x600")

        # Create notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create tabs
        self.caesar_tab = ttk.Frame(self.notebook)
        self.affine_tab = ttk.Frame(self.notebook)
        self.atbash_tab = ttk.Frame(self.notebook)
        self.rail_fence_tab = ttk.Frame(self.notebook)
        self.vigenere_tab = ttk.Frame(self.notebook)
        self.beaufort_tab = ttk.Frame(self.notebook)
        self.homophonic_tab = ttk.Frame(self.notebook)
        self.polygram_tab = ttk.Frame(self.notebook)
        self.pigpen_tab = ttk.Frame(self.notebook)
        self.settings_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.caesar_tab, text="Caesar")
        self.notebook.add(self.affine_tab, text="Affine")
        self.notebook.add(self.atbash_tab, text="Atbash")
        self.notebook.add(self.rail_fence_tab, text="Rail Fence")
        self.notebook.add(self.vigenere_tab, text="Vigenere")
        self.notebook.add(self.beaufort_tab, text="Beaufort")
        self.notebook.add(self.homophonic_tab, text="Homophonic")
        self.notebook.add(self.polygram_tab, text="Polygram")
        self.notebook.add(self.pigpen_tab, text="Pigpen")
        self.notebook.add(self.settings_tab, text="Settings")

        # Create input field
        self.input_label = tk.Label(self.caesar_tab, text="Enter text:", font=("Arial", 16))
        self.input_label.pack()

        self.input_entry = tk.Entry(self.caesar_tab, width=50, font=("Arial", 16))
        self.input_entry.pack()

        # Create key entry for Caesar cipher
        self.caesar_key_label = tk.Label(self.caesar_tab, text="Caesar key (1-25):", font=("Arial", 16))
        self.caesar_key_label.pack()

        self.caesar_key_entry = tk.Entry(self.caesar_tab, width=10, font=("Arial", 16))
        self.caesar_key_entry.pack()

        # Create encrypt/decrypt buttons for Caesar cipher
        self.caesar_encrypt_button = tk.Button(self.caesar_tab, text="Encrypt", command=self.caesar_encrypt, font=("Arial", 16))
        self.caesar_encrypt_button.pack()

        self.caesar_decrypt_button = tk.Button(self.caesar_tab, text="Decrypt", command=self.caesar_decrypt, font=("Arial", 16))
        self.caesar_decrypt_button.pack()

        # Create output field for Caesar cipher
        self.caesar_output_label = tk.Label(self.caesar_tab, text="Output:", font=("Arial", 16))
        self.caesar_output_label.pack()

        self.caesar_output_text = tk.Text(self.caesar_tab, width=60, height=10, font=("Arial", 16))
        self.caesar_output_text.pack()

        # Create input field for Affine cipher
        self.affine_input_label = tk.Label(self.affine_tab, text="Enter text:", font=("Arial", 16))
        self.affine_input_label.pack()

        self.affine_input_entry = tk.Entry(self.affine_tab, width=50, font=("Arial", 16))
        self.affine_input_entry.pack()

        # Create key entry for Affine cipher
        self.affine_key_label = tk.Label(self.affine_tab, text="Affine key (a, b):", font=("Arial", 16))
        self.affine_key_label.pack()

        self.affine_key_entry = tk.Entry(self.affine_tab, width=20, font=("Arial", 16))
        self.affine_key_entry.pack()

        # Create encrypt/decrypt buttons for Affine cipher
        self.affine_encrypt_button = tk.Button(self.affine_tab, text="Encrypt", command=self.affine_encrypt, font=("Arial", 16))
        self.affine_encrypt_button.pack()

        self.affine_decrypt_button = tk.Button(self.affine_tab, text="Decrypt", command=self.affine_decrypt, font=("Arial", 16))
        self.affine_decrypt_button.pack()

        # Create output field for Affine cipher
        self.affine_output_label = tk.Label(self.affine_tab, text="Output:", font=("Arial", 16))
        self.affine_output_label.pack()

        self.affine_output_text = tk.Text(self.affine_tab, width=60, height=10, font=("Arial", 16))
        self.affine_output_text.pack()

        # Create input field for Atbash cipher
        self.atbash_input_label = tk.Label(self.atbash_tab, text="Enter text:", font=("Arial", 16))
        self.atbash_input_label.pack()

        self.atbash_input_entry = tk.Entry(self.atbash_tab, width=50, font=("Arial", 16))
        self.atbash_input_entry.pack()

        # Create encrypt/decrypt buttons for Atbash cipher
        self.atbash_encrypt_button = tk.Button(self.atbash_tab, text="Encrypt", command=self.atbash_encrypt, font=("Arial", 16))
        self.atbash_encrypt_button.pack()

        self.atbash_decrypt_button = tk.Button(self.atbash_tab, text="Decrypt", command=self.atbash_decrypt, font=("Arial", 16))
        self.atbash_decrypt_button.pack()

        # Create output field for Atbash cipher
        self.atbash_output_label = tk.Label(self.atbash_tab, text="Output:", font=("Arial", 16))
        self.atbash_output_label.pack()

        self.atbash_output_text = tk.Text(self.atbash_tab, width=60, height=10, font=("Arial", 16))
        self.atbash_output_text.pack()

        # Create input field for Rail Fence cipher
        self.rail_fence_input_label = tk.Label(self.rail_fence_tab, text="Enter text:", font=("Arial", 16))
        self.rail_fence_input_label.pack()

        self.rail_fence_input_entry = tk.Entry(self.rail_fence_tab, width=50, font=("Arial", 16))
        self.rail_fence_input_entry.pack()

        # Create key entry for Rail Fence cipher
        self.rail_fence_key_label = tk.Label(self.rail_fence_tab, text="Rail Fence key (number of rails):", font=("Arial", 16))
        self.rail_fence_key_label.pack()

        self.rail_fence_key_entry = tk.Entry(self.rail_fence_tab, width=10, font=("Arial", 16))
        self.rail_fence_key_entry.pack()

        # Create encrypt/decrypt buttons for Rail Fence cipher
        self.rail_fence_encrypt_button = tk.Button(self.rail_fence_tab, text="Encrypt", command=self.rail_fence_encrypt, font=("Arial", 16))
        self.rail_fence_encrypt_button.pack()

        self.rail_fence_decrypt_button = tk.Button(self.rail_fence_tab, text="Decrypt", command=self.rail_fence_decrypt, font=("Arial", 16))
        self.rail_fence_decrypt_button.pack()

        # Create output field for Rail Fence cipher
        self.rail_fence_output_label = tk.Label(self.rail_fence_tab, text="Output:", font=("Arial", 16))
        self.rail_fence_output_label.pack()

        self.rail_fence_output_text = tk.Text(self.rail_fence_tab, width=60, height=10, font=("Arial", 16))
        self.rail_fence_output_text.pack()

        # Create input field for Vigenere cipher
        self.vigenere_input_label = tk.Label(self.vigenere_tab, text="Enter text:", font=("Arial", 16))
        self.vigenere_input_label.pack()

        self.vigenere_input_entry = tk.Entry(self.vigenere_tab, width=50, font=("Arial", 16))
        self.vigenere_input_entry.pack()

        # Create key entry for Vigenere cipher
        self.vigenere_key_label = tk.Label(self.vigenere_tab, text="Vigenere key (word):", font=("Arial", 16))
        self.vigenere_key_label.pack()

        self.vigenere_key_entry = tk.Entry(self.vigenere_tab, width=20, font=("Arial", 16))
        self.vigenere_key_entry.pack()

        # Create encrypt/decrypt buttons for Vigenere cipher
        self.vigenere_encrypt_button = tk.Button(self.vigenere_tab, text="Encrypt", command=self.vigenere_encrypt, font=("Arial", 16))
        self.vigenere_encrypt_button.pack()

        self.vigenere_decrypt_button = tk.Button(self.vigenere_tab, text="Decrypt", command=self.vigenere_decrypt, font=("Arial", 16))
        self.vigenere_decrypt_button.pack()

        # Create output field for Vigenere cipher
        self.vigenere_output_label = tk.Label(self.vigenere_tab, text="Output:", font=("Arial", 16))
        self.vigenere_output_label.pack()

        self.vigenere_output_text = tk.Text(self.vigenere_tab, width=60, height=10, font=("Arial", 16))
        self.vigenere_output_text.pack()

        # Create input field for Beaufort cipher
        self.beaufort_input_label = tk.Label(self.beaufort_tab, text="Enter text:", font=("Arial", 16))
        self.beaufort_input_label.pack()

        self.beaufort_input_entry = tk.Entry(self.beaufort_tab, width=50, font=("Arial", 16))
        self.beaufort_input_entry.pack()

        # Create key entry for Beaufort cipher
        self.beaufort_key_label = tk.Label(self.beaufort_tab, text="Beaufort key (word):", font=("Arial", 16))
        self.beaufort_key_label.pack()

        self.beaufort_key_entry = tk.Entry(self.beaufort_tab, width=20, font=("Arial", 16))
        self.beaufort_key_entry.pack()

        # Create encrypt/decrypt buttons for Beaufort cipher
        self.beaufort_encrypt_button = tk.Button(self.beaufort_tab, text="Encrypt", command=self.beaufort_encrypt, font=("Arial", 16))
        self.beaufort_encrypt_button.pack()

        self.beaufort_decrypt_button = tk.Button(self.beaufort_tab, text="Decrypt", command=self.beaufort_decrypt, font=("Arial", 16))
        self.beaufort_decrypt_button.pack()

        # Create output field for Beaufort cipher
        self.beaufort_output_label = tk.Label(self.beaufort_tab, text="Output:", font=("Arial", 16))
        self.beaufort_output_label.pack()

        self.beaufort_output_text = tk.Text(self.beaufort_tab, width=60, height=10, font=("Arial", 16))
        self.beaufort_output_text.pack()

        # Create input field for Homophonic cipher
        self.homophonic_input_label = tk.Label(self.homophonic_tab, text="Enter text:", font=("Arial", 16))
        self.homophonic_input_label.pack()

        self.homophonic_input_entry = tk.Entry(self.homophonic_tab, width=50, font=("Arial", 16))
        self.homophonic_input_entry.pack()

        # Create key entry for Homophonic cipher
        self.homophonic_key_label = tk.Label(self.homophonic_tab, text="Homophonic key (dictionary):", font=("Arial", 16))
        self.homophonic_key_label.pack()

        self.homophonic_key_entry = tk.Entry(self.homophonic_tab, width=20, font=("Arial", 16))
        self.homophonic_key_entry.pack()

        # Create encrypt/decrypt buttons for Homophonic cipher
        self.homophonic_encrypt_button = tk.Button(self.homophonic_tab, text="Encrypt", command=self.homophonic_encrypt, font=("Arial", 16))
        self.homophonic_encrypt_button.pack()

        self.homophonic_decrypt_button = tk.Button(self.homophonic_tab, text="Decrypt", command=self.homophonic_decrypt, font=("Arial", 16))
        self.homophonic_decrypt_button.pack()

        # Create output field for Homophonic cipher
        self.homophonic_output_label = tk.Label(self.homophonic_tab, text="Output:", font=("Arial", 16))
        self.homophonic_output_label.pack()

        self.homophonic_output_text = tk.Text(self.homophonic_tab, width=60, height=10, font=("Arial", 16))
        self.homophonic_output_text.pack()

        # Create input field for Polygram cipher
        self.polygram_input_label = tk.Label(self.polygram_tab, text="Enter text:", font=("Arial", 16))
        self.polygram_input_label.pack()

        self.polygram_input_entry = tk.Entry(self.polygram_tab, width=50, font=("Arial", 16))
        self.polygram_input_entry.pack()

        # Create key entry for Polygram cipher
        self.polygram_key_label = tk.Label(self.polygram_tab, text="Polygram key (matrix):", font=("Arial", 16))
        self.polygram_key_label.pack()

        self.polygram_key_entry = tk.Entry(self.polygram_tab, width=20, font=("Arial", 16))
        self.polygram_key_entry.pack()

        # Create encrypt/decrypt buttons for Polygram cipher
        self.polygram_encrypt_button = tk.Button(self.polygram_tab, text="Encrypt", command=self.polygram_encrypt, font=("Arial", 16))
        self.polygram_encrypt_button.pack()

        self.polygram_decrypt_button = tk.Button(self.polygram_tab, text="Decrypt", command=self.polygram_decrypt, font=("Arial", 16))
        self.polygram_decrypt_button.pack()

        # Create output field for Polygram cipher
        self.polygram_output_label = tk.Label(self.polygram_tab, text="Output:", font=("Arial", 16))
        self.polygram_output_label.pack()

        self.polygram_output_text = tk.Text(self.polygram_tab, width=60, height=10, font=("Arial", 16))
        self.polygram_output_text.pack()

        # Create input field for Pigpen cipher
        self.pigpen_input_label = tk.Label(self.pigpen_tab, text="Enter text:", font=("Arial", 16))
        self.pigpen_input_label.pack()

        self.pigpen_input_entry = tk.Entry(self.pigpen_tab, width=50, font=("Arial", 16))
        self.pigpen_input_entry.pack()

        # Create encrypt/decrypt buttons for Pigpen cipher
        self.pigpen_encrypt_button = tk.Button(self.pigpen_tab, text="Encrypt", command=self.pigpen_encrypt, font=("Arial", 16))
        self.pigpen_encrypt_button.pack()

        self.pigpen_decrypt_button = tk.Button(self.pigpen_tab, text="Decrypt", command=self.pigpen_decrypt, font=("Arial", 16))
        self.pigpen_decrypt_button.pack()

        # Create output field for Pigpen cipher
        self.pigpen_output_label = tk.Label(self.pigpen_tab, text="Output:", font=("Arial", 16))
        self.pigpen_output_label.pack()

        self.pigpen_output_text = tk.Text(self.pigpen_tab, width=60, height=10, font=("Arial", 16))
        self.pigpen_output_text.pack()

    def caesar_encrypt(self):
        text = self.input_entry.get()
        key = int(self.caesar_key_entry.get())
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            else:
                result += char
        self.caesar_output_text.delete(1.0, tk.END)
        self.caesar_output_text.insert(tk.END, result)

    def caesar_decrypt(self):
        text = self.input_entry.get()
        key = int(self.caesar_key_entry.get())
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            else:
                result += char
        self.caesar_output_text.delete(1.0, tk.END)
        self.caesar_output_text.insert(tk.END, result)

    def affine_encrypt(self):
        text = self.affine_input_entry.get()
        key = self.affine_key_entry.get().split(',')
        a = int(key[0])
        b = int(key[1])
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((a * (ord(char) - ascii_offset) + b) % 26 + ascii_offset)
            else:
                result += char
        self.affine_output_text.delete(1.0, tk.END)
        self.affine_output_text.insert(tk.END, result)

    def affine_decrypt(self):
        text = self.affine_input_entry.get()
        key = self.affine_key_entry.get().split(',')
        a = int(key[0])
        b = int(key[1])
        a_inv = pow(a, -1, 26)
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((a_inv * (ord(char) - ascii_offset - b)) % 26 + ascii_offset)
            else:
                result += char
        self.affine_output_text.delete(1.0, tk.END)
        self.affine_output_text.insert(tk.END, result)

    def atbash_encrypt(self):
        text = self.atbash_input_entry.get()
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr(ascii_offset + (25 - (ord(char) - ascii_offset)))
            else:
                result += char
        self.atbash_output_text.delete(1.0, tk.END)
        self.atbash_output_text.insert(tk.END, result)

    def atbash_decrypt(self):
        text = self.atbash_input_entry.get()
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr(ascii_offset + (25 - (ord(char) - ascii_offset)))
            else:
                result += char
        self.atbash_output_text.delete(1.0, tk.END)
        self.atbash_output_text.insert(tk.END, result)


    def rail_fence_encrypt(self):
        text = self.rail_fence_input_entry.get()
        key = int(self.rail_fence_key_entry.get())
        rails = [''] * key
        dir = 0
        rail = 0
        for i in range(len(text)):
            rails[rail] += text[i]
            if rail == 0:
                dir = 1
            elif rail == key - 1:
                dir = -1
            rail += dir
        result = ''
        for rail in rails:
            result += rail
        self.rail_fence_output_text.delete(1.0, tk.END)
        self.rail_fence_output_text.insert(tk.END, result)

    def rail_fence_decrypt(self):
        text = self.rail_fence_input_entry.get()
        key = int(self.rail_fence_key_entry.get())
        length = len(text)
        rail_lengths = [0] * key
        dir = 0
        rail = 0
        for i in range(length):
            rail_lengths[rail] += 1
            if rail ==  0:
                dir = 1
            elif rail == key - 1:
                dir = -1
            rail += dir
        rails = [''] * key
        index = 0
        for i in range(key):
            rails[i] = text[index:index + rail_lengths[i]]
            index += rail_lengths[i]
        result = [''] * length
        index = 0
        for i in range(length):
            for j in range(key):
                if len(rails[j]) > 0:
                    result[i] = rails[j][0]
                    rails[j] = rails[j][1:]
                    break
        self.rail_fence_output_text.delete(1.0, tk.END)
        self.rail_fence_output_text.insert(tk.END, ''.join(result))     
    
    def vigenere_encrypt(self):
        text = self.vigenere_input_entry.get()
        key = self.vigenere_key_entry.get()
        result = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                shift = ord(key[key_index % len(key)].upper()) - 65
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                key_index += 1
            else:
                result += char
        self.vigenere_output_text.delete(1.0, tk.END)
        self.vigenere_output_text.insert(tk.END, result)

    def vigenere_decrypt(self):
        text = self.vigenere_input_entry.get()
        key = self.vigenere_key_entry.get()
        result = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                shift = ord(key[key_index % len(key)].upper()) - 65
                result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                key_index += 1
            else:
                result += char
        self.vigenere_output_text.delete(1.0, tk.END)
        self.vigenere_output_text.insert(tk.END, result)

    def beaufort_encrypt(self):
        text = self.beaufort_input_entry.get()
        key = self.beaufort_key_entry.get()
        result = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                shift = ord(key[key_index % len(key)].upper()) - 65
                result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                key_index += 1
            else:
                result += char
        self.beaufort_output_text.delete(1.0, tk.END)
        self.beaufort_output_text.insert(tk.END, result)

    def beaufort_decrypt(self):
        text = self.beaufort_input_entry.get()
        key = self.beaufort_key_entry.get()
        result = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                shift = ord(key[key_index % len(key)].upper()) - 65
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                key_index += 1
            else:
                result += char
        self.beaufort_output_text.delete(1.0, tk.END)
        self.beaufort_output_text.insert(tk.END, result)

    def homophonic_encrypt(self):
        text = self.homophonic_input_entry.get()
        key = self.homophonic_key_entry.get()
        key_dict = {}
        for pair in key.split(','):
            key_dict[pair.split(':')[0]] = pair.split(':')[1]
        result = ""
        for char in text:
            if char.isalpha():
                result += key_dict[char]
            else:
                result += char
        self.homophonic_output_text.delete(1.0, tk.END)
        self.homophonic_output_text.insert(tk.END, result)

    def homophonic_decrypt(self):
        text = self.homophonic_input_entry.get()
        key = self.homophonic_key_entry.get()
        key_dict = {}
        for pair in key.split(','):
            result = ""
        for char in text:
            if char.isalpha():
                result += key_dict[char]
            else:
                result += char
        self.homophonic_output_text.delete(1.0, tk.END)
        self.homophonic_output_text.insert(tk.END, result)

    def polygram_encrypt(self):
        text = self.polygram_input_entry.get()
        key = self.polygram_key_entry.get()
        key_matrix = []
        for row in key.split(';'):
            key_matrix.append([int(x) for x in row.split(',')])
        result = ""
        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            if len(pair) == 2:
                x = ord(pair[0]) - 65
                y = ord(pair[1]) - 65
                x_new = (key_matrix[0][0] * x + key_matrix[0][1] * y) % 26
                y_new = (key_matrix[1][0] * x + key_matrix[1][1] * y) % 26
                result += chr(x_new + 65) + chr(y_new + 65)
            else:
                result += pair
        self.polygram_output_text.delete(1.0, tk.END)
        self.polygram_output_text.insert(tk.END, result)

    def polygram_decrypt(self):
        text = self.polygram_input_entry.get()
        key = self.polygram_key_entry.get()
        key_matrix = []
        for row in key.split(';'):
            key_matrix.append([int(x) for x in row.split(',')])
        det = key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]
        det_inv = pow(det, -1, 26)
        key_matrix_inv = [[det_inv * key_matrix[1][1] % 26, -det_inv * key_matrix[0][1] % 26],
                          [-det_inv * key_matrix[1][0] % 26, det_inv * key_matrix[0][0] % 26]]
        result = ""
        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            if len(pair) == 2:
                x = ord(pair[0]) - 65
                y = ord(pair[1]) - 65
                x_new = (key_matrix_inv[0][0] * x + key_matrix_inv[0][1] * y) % 26
                y_new = (key_matrix_inv[1][0] * x + key_matrix_inv[1][1] * y) % 26
                result += chr(x_new + 65) + chr(y_new + 65)
            else:
                result += pair
        self.polygram_output_text.delete(1.0, tk.END)
        self.polygram_output_text.insert(tk.END, result)

    def pigpen_encrypt(self):
        text = self.pigpen_input_entry.get()
        pigpen_dict = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10', 'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26'}
        result = ""
        for char in text:
            if char.isalpha():
                result += pigpen_dict[char.upper()]
            else:
                result += char
        self.pigpen_output_text.delete(1.0, tk.END)
        self.pigpen_output_text.insert(tk.END, result)

    def pigpen_decrypt(self):
        text = self.pigpen_input_entry.get()
        pigpen_dict = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J', '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': ' R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'}
        result = ""
        for char in text:
            if char.isdigit():
                result += pigpen_dict[char]
            else:
                result += char
        self.pigpen_output_text.delete(1.0, tk.END)
        self.pigpen_output_text.insert(tk.END, result)

root = tk.Tk()
app = CipherApp(root)
root.mainloop()