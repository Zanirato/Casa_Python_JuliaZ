# Importa o módulo principal do tkinter para construção de interfaces gráficas
import tkinter as tk
from tkinter import ttk, messagebox
from db import getconnection
from utils import centralizarjanela

def showlogin(app):
    """
    Exibe a tela de login no aplicativo.
    """
    # Limpa a tela atual
    for w in app.winfo_children():
        w.destroy()

    # Centraliza a janela principal
    centralizarjanela(app, 400, 250)

    # Frame principal
    frm = ttk.Frame(app, padding=20)
    frm.pack(expand=True)

    # Título
    ttk.Label(frm, text="Login", font=("TkDefaultFont", 16)).grid(column=0, row=0, columnspan=2, pady=10)

    # Campo Usuário
    ttk.Label(frm, text="Usuário").grid(column=0, row=1, sticky="e")
    userent = ttk.Entry(frm, width=25)
    userent.grid(column=1, row=1)
    userent.focus_set()  # Foco automático no usuário

    # Campo Senha
    ttk.Label(frm, text="Senha").grid(column=0, row=2, sticky="e")
    pwdent = ttk.Entry(frm, show="*", width=25)
    pwdent.grid(column=1, row=2)

    # Função interna de login
    def attempt_login():
        username = userent.get().strip()
        password = pwdent.get().strip()

        if not username or not password:
            messagebox.showwarning("Falha", "Preencha usuário e senha.")
            return

        with getconnection() as conn:
            cur = conn.execute(
                "SELECT * FROM usuarios WHERE usuario=? AND senha=?",
                (username, password)
            )
            row = cur.fetchone()

        if row:
            app.currentuser = dict(row)
            app.showmain()
        else:
            messagebox.showerror("Falha", "Usuário ou senha inválidos.")

    # Botão Entrar
    ttk.Button(frm, text="Entrar", command=attempt_login).grid(column=0, row=3, columnspan=2, pady=10)

    # Permite login ao pressionar Enter
    app.bind("<Return>", lambda event: attempt_login())