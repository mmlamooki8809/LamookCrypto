# LamookCrypto  
A simple text **encryption and decryption tool** based on a custom numeric algorithm that uses two keys.

---

## ✨ Overview  
LamookCrypto encrypts and decrypts text using a custom classical-style numeric algorithm.  
Each character is assigned a **three-digit base code**, and the program uses **two different keys**:

1. **Key 1:** Fully random  
2. **Key 2:** Random but generated using additional internal computations  

These keys modify the numeric codes to produce an encrypted output, which can be reversed only through the same algorithm.

---

## 🔥 Features
- 🔐 Encrypt text using two keys  
- 🔓 Decrypt encrypted text  
- 🎯 Simple classical numeric cipher  
- 🔑 Two-key system (Random Key + Computed Random Key)  
- ⌨️ Supports English letters, digits, and common symbols  
- 🖥️ Clean GUI built with CustomTkinter  
- 📂 Organized and easy-to-extend structure  

---

## 📁 Project Structure
```
LamookCrypto/
│
├── core/
│   └── cipher_core.py     # Algorithm, keys, tables, and core functions
│
└── gui/
    └── app.py             # GUI (main file to run)
```

---

## 🚀 How to Run
### 1. Install requirements  
```bash
pip install customtkinter
```

### 2. Run the app  
```bash
cd gui
python app.py
```

---

## 🧠 Algorithm Summary
- Each character → predefined three-digit number  
- Key 1 → fully random  
- Key 2 → random + computed  
- Both keys transform the numeric code  
- Decryption performs the reverse process  

---

## 📜 License – MIT License  
This project is open-source under the MIT License.  
You may use, modify, and distribute it freely as long as attribution is included and no liability is placed on the author.

---

## 👤 Author  
**Mahdiyar (mmlamooki8809)**  
