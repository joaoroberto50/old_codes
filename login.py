LOGIN = 1
CADASTRO = 2

users = {"aluno_demo": {"senha": "aluno_senha", "tipo": "aluno"},
         "prof_demo" : {"senha": "prof_senha",  "tipo": "professor"}
        }

def read_integer(*,m=''):
    i = int(input(m))
    return i
    
def read_string(*,m=''):
    s = input(m)
    return s

def create_user(l,s,t):
    return {"l": { "senha": s, "tipo": t}}

def check_user(l,s):
    res = False
    if l in users:
        if users[l]["senha"] == s:
            res = True
            return res, "Login realizado com sucesso"
        else:
            return res, "Senha errada"
    else:
        return res, "Login não encontrado"

def login():
    l = read_string(m="Digite o login: ")
    s = read_string(m="Digire a senha: ")
    r,m = check_user(l,s)
    print(m)
    return r


def main():
    print(50*"=")
    print(
    """
    1 - Fazer login
    2 - Fazer cadastro
    
    """)
    print(50*"=")
    o = read_integer(m="Digite a opção: ")
    print(50*"=")
    print(50*"=")    
    if o == LOGIN:
    
        login()
        
    
    
if __name__ == "__main__":
    main()
    
