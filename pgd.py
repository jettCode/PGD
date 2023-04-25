import random
import tkinter as tk
from tkinter import filedialog

def generate_passwords(start_year, end_year):
    passwords = []
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            for day in range(1, 32):
                password = "{:02d}{:02d}{:04d}".format(day, month, year)
                passwords.append(password)
    random.shuffle(passwords)
    passwords.sort()
    return passwords

def generate_and_save_passwords():
    start_year = int(start_year_entry.get())
    end_year = int(end_year_entry.get())

    if start_year > end_year:
        message = "O ano de início não pode \n ser maior que o ano final."
        result_label.config(text=message)
        return

    passwords = generate_passwords(start_year, end_year)
    save_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if save_path:
        with open(save_path, "w") as f:
            for password in passwords:
                f.write(password + "\n")
        message = "As senhas foram salvas em {}".format(save_path)
        result_label.config(text=message)
    else:
        result_label.config(text="Nenhum arquivo selecionado para salvar as senhas.")

    # Ajustar largura da janela de exibição da mensagem
    result_label.update_idletasks()
    message_width = result_label.winfo_width()
    if message_width > 249:
        result_label.config(wraplength=249)
    else:
        result_label.config(wraplength=message_width)


def validate_input(new_value):
    if len(new_value) > 4:
        return False
    return True


window = tk.Tk()
window.title("Gerador de Senhas")
window.geometry("280x220")
window.resizable(False, False)

start_year_label = tk.Label(window, text="Ano de início:")
start_year_label.grid(row=0, column=0, padx=10, pady=10)

validate_input_command = window.register(validate_input)
start_year_entry = tk.Entry(window, width=5, validate="key", validatecommand=(validate_input_command, '%S'))
start_year_entry.grid(row=0, column=1, padx=10, pady=10)

end_year_label = tk.Label(window, text="Ano final:")
end_year_label.grid(row=1, column=0, padx=10, pady=10)

end_year_entry = tk.Entry(window, width=5, validate="key", validatecommand=(validate_input_command, '%S'))
end_year_entry.grid(row=1, column=1, padx=10, pady=10)


generate_button = tk.Button(window, text="Gerar e Salvar Senhas", command=generate_and_save_passwords)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

window.bind("<Return>", lambda event: generate_and_save_passwords())
window.bind("<Escape>", lambda event: window.destroy())

window.mainloop()

#   __               _               __          #
#  /  \          o  | |          |  /  \         #
# |    | __   _     | |  __,   __| |    | ,_     #
# |    |/    |/  |  |/  /  |  /  | |    |/  |    #
#  \__/ \___/|__/|_/|__/\_/|_/\_/|_/\__/    |_/  #
#                   |\                           #
#                   |/                           #
