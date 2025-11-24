from customtkinter import *
import sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import cryptolamook as cl
import tkinter.messagebox as tkm


set_appearance_mode('dark')


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title('Lamooki Crypto')
        self.geometry('700x400')
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)
        self.config(bg='#121212')
        self.changer = cl.CryptoGraphy()

        # TextBox
        self.textbox_label = CTkLabel(self, text='Text : ', text_color=("#212121", "#FFFFFF"), bg_color=('#F5F5F5' ,'#121212'), font=CTkFont('Digital-7', 30, 'bold'))
        self.textbox_label.grid(row=0, column=0, sticky=EW)

        self.textbox_input = CTkTextbox(self, height=250, fg_color=("#FFFFFF", "#1E1E1E"), text_color='#A0A0A0', corner_radius=10, border_color=("#B0B0B0", "#333333"), font=CTkFont('Comic Sans MS', 20), bg_color=('#F5F5F5' ,'#121212'))
        self.textbox_input.grid(row=0, column=1, columnspan=3, sticky=EW, padx=(0,10))
        self.textbox_input.insert('1.0', 'Text or CryptographText...')
        
        self.textbox_input.bind("<FocusIn>", command=self.on_focus_in)
        self.textbox_input.bind('<FocusOut>', command=self.on_focus_out)

        #Buttons
        # Theme switch
        self.theme_switch = CTkSwitch(self, text='Dark Mode', button_color=("#4CAF50", "#BB86FC"), button_hover_color=("#45A049", "#9B6BFF"), progress_color=("#173918", "#BB86FC"), text_color=("#212121", "#FFFFFF"), command=self.toggle_theme, bg_color=('#F5F5F5' ,'#121212'), font=CTkFont('Digital-7'))
        self.theme_switch.grid(row=2, column=0, sticky=S)

        # buttons
        self.clear_all_btn = CTkButton(self, text='Clear All', fg_color=("#4CAF50", "#BB86FC"), hover_color=("#45A049", "#9B6BFF"), text_color="#FFFFFF", font=CTkFont('Digital-7', 25), command=self.clear_all)
        self.clear_all_btn.grid(row=1, column=1, sticky=NSEW, padx=10, pady=5)

        self.copy_text_btn = CTkButton(self, text='Copy', fg_color=("#4CAF50", "#BB86FC"), hover_color=("#45A049", "#9B6BFF"), text_color="#FFFFFF", font=CTkFont('Digital-7', 25), command=self.copy_text)
        self.copy_text_btn.grid(row=1, column=2, sticky=NSEW, padx=10, pady=5)

        self.paste_crypto_btn = CTkButton(self, text='Paste', fg_color=("#4CAF50", "#BB86FC"), hover_color=("#45A049", "#9B6BFF"), text_color="#FFFFFF", font=CTkFont('Digital-7', 25), command=self.paste_text)
        self.paste_crypto_btn.grid(row=1, column=3, sticky=NSEW, padx=10, pady=5)

        self.backspace_btn = CTkButton(self, text='Del', fg_color=("#4CAF50", "#BB86FC"), hover_color=("#45A049", "#9B6BFF"), text_color="#FFFFFF", font=CTkFont('Digital-7', 25), command=self.delete)
        self.backspace_btn.grid(row=2, column=1, sticky=NSEW, padx=10, pady=5)

        self.convert_crypto_btn = CTkButton(self, text='Convert to Crypto', fg_color=("#4CAF50", "#BB86FC"), hover_color=("#45A049", "#9B6BFF"), text_color="#FFFFFF", font=CTkFont('Digital-7', 22), command=self.convert_to_crypto)
        self.convert_crypto_btn.grid(row=2, column=2, sticky=NSEW, padx=10, pady=5)

        self.convert_text_btn = CTkButton(self, text='Convert to Text', fg_color=("#4CAF50", "#BB86FC"), hover_color=("#45A049", "#9B6BFF"), text_color="#FFFFFF", font=CTkFont('Digital-7', 22), command=self.convert_to_text)
        self.convert_text_btn.grid(row=2, column=3, sticky=NSEW, padx=10, pady=5)

    # Toggle Theme
    def toggle_theme(self):
        if self.theme_switch.get() == 1:
            set_appearance_mode('light')
            self.config(bg='#F5F5F5')
            self.theme_switch.configure(text='Light Mode')
            
        else:
            set_appearance_mode('dark')
            self.config(bg='#121212')
            self.theme_switch.configure(text='Dark Mode')
            
    def on_focus_in(self, event):
        if(self.textbox_input.get('1.0', 'end-1c') == "Text or CryptographText..."):
            self.textbox_input.delete('1.0', 'end')
            self.textbox_input.configure(text_color = ("#212121", "#FFFFFF"))
    
    def on_focus_out(self, event):
        if(self.textbox_input.get('1.0', 'end-1c')==''):
            self.textbox_input.insert('1.0','Text or CryptographText...')
            self.textbox_input.configure(text_color=('#A0A0A0'))
        
    def clear_all(self):
        self.textbox_input.delete('1.0', 'end')
        self.textbox_input.insert('1.0','Text or CryptographText...')
        self.textbox_input.configure(text_color=('#A0A0A0'))
        self.textbox_label.configure(text = 'Text : ')
        self.focus()
        
    def copy_text(self):
        if(self.textbox_input.cget('text_color') == '#A0A0A0'):
            pass
        else:
            text = self.textbox_input.get('1.0', 'end-1c')
            self.clipboard_clear()
            self.clipboard_append(text)
        
    def paste_text(self):
        try:
            if(self.textbox_input.cget('text_color') == '#A0A0A0'):
                self.textbox_input.delete('1.0', 'end')
                self.textbox_input.configure(text_color = ("#212121", "#FFFFFF"))
            text = self.clipboard_get()
            self.textbox_input.insert('1.0', text)
        except:
            pass
        
    def delete(self):
        if(self.textbox_input.cget('text_color') == '#A0A0A0'):
            pass
        else:
            text = self.textbox_input.get('1.0', 'end-1c')
            text = text[:-1] 
            self.textbox_input.delete('1.0', 'end')
            self.textbox_input.insert('1.0', text)
            if(text == ''):
                self.textbox_input.insert('1.0','Text or CryptographText...')
                self.textbox_input.configure(text_color=('#A0A0A0'))
                self.focus()
                       
            
    def convert_to_crypto(self):
        text = self.textbox_input.get('1.0', 'end-1c')
        crypto = self.changer.textTocrypto(text)
        self.textbox_input.delete('1.0', 'end-1c')
        self.textbox_input.insert('1.0', crypto)
        
            
    def convert_to_text(self):
        try:     
            crypto = self.textbox_input.get('1.0', 'end-1c')
            text = self.changer.cryptoTotext(crypto)
            self.textbox_input.delete('1.0', 'end-1c')
            self.textbox_input.insert('1.0', text)
        except:
            tkm.showerror('Error', 'please write crypto text by cryptolamook algorithm')
            


root = App()
root.mainloop()
