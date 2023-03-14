"""
entradas:
-usuario;
-senha;

condições: 
- usuario != senha

saída:
-certo: "cadastro feito"
-errado: "o usuario e a senha não podem ser iguais"
"""
while True:
    nomeUsuario = input("digite seu nome de usuario:")
    senha = input("digite a senha:")
    if nomeUsuario != senha:
        print("cadastro efetuado com sucesso!")
        break
    else:
        print("o usuario e a senha não podem ser iguais.")