import streamlit as st
import requests

url = "https://aps-5-rest-mongodb-streamlit-joaodelomo-dmu5.onrender.com/"

##############################################################################################################################################

#USUÁRIOS

def all_users():
    response = requests.get(f'{url}/usuarios')
    if response.status_code == 200:
        st.table(response.json())


def get_user_by_id(user_id):
    response = requests.get(f'{url}/usuarios/{user_id}')
    if response.status_code == 200:
        st.table(response.json())
    else:
        st.error("Usuário não encontrado.")

def create_user():
    user = {
        "nome": st.text_input("Insira o nome do usuário", ""),
        "cpf": st.text_input("Insira o CPF do usuário", ""),
        "data": st.text_input("Insira a data de nasciemto do usuário", ""),
    }

    if st.button("Criar Usuário"):
        response = requests.post(f'{url}/usuarios', json=user)
        if response.status_code == 201:
            st.success("Usuário criado com sucesso.")
        else:
            st.error("Erro ao criar usuário.")

def data_user():
    id = st.text_input("Insira o ID do usuário", "")
    if st.button("Buscar"):
        response = requests.get(f'{url}/usuarios/{id}')
        st.table(response.json())
        st.session_state["Usuario"] = response.json()
    if 'Usuario' in st.session_state:
        usuario = st.session_state["Usuario"]
        nome = st.text_input("Insira o nome do usuário", usuario.get("nome", ""))
        cpf = st.text_input("Insira o CPF do usuário", usuario.get("cpf", ""))
        data = st.text_input("Insira a data de nascimento do usuário", usuario.get("data", ""))
        
        if st.button("Atualizar"):
            update_data = {"nome": nome, "cpf": cpf, "data": data}
            response = requests.put(f'{url}/usuarios/{id}', json=update_data)
            if response.status_code == 201:
                st.success("Usuário atualizado com sucesso.")
            else:
                st.error("Erro ao atualizar usuário.")

        if st.button("Deletar"):
            response = requests.delete(f'{url}/usuarios/{id}')
            if response.status_code == 200:
                del st.session_state["Usuario"]  # Limpa o estado após deletar
                st.success("Usuário deletado com sucesso.")
            else:
                st.error("Erro ao deletar usuário.")


##############################################################################################################################################

#BICICLETAS

def all_bikes():
    response = requests.get(f'{url}/bikes')
    if response.status_code == 200:
        st.table(response.json())

def get_bike_by_id(bike_id):
    response = requests.get(f'{url}/bikes/{bike_id}')
    if response.status_code == 200:
        st.table(response.json())
    else:
        st.error("Bicicleta não encontrada.")

def create_bike():
    bike = {
        "marca": st.text_input("Insira a marca da bicicleta", ""),
        "modelo": st.text_input("Insira o modelo da bicicleta", ""),
        "cidade": st.text_input("Insira a cidade da bicicleta", ""),
        "status": st.text_input("Insira o status da bicicleta", ""),
    }

    if st.button("Criar Bicicleta"):
        response = requests.post(f'{url}/bikes', json=bike)
        if response.status_code == 201:
            st.success("Bicicleta criada com sucesso.")
        else:
            st.error("Erro ao criar bicicleta.")

def data_bike():
    id = st.text_input("Insira o ID da bicicleta", "")
    if st.button("Buscar"):
        response = requests.get(f'{url}/bikes/{id}')
        st.table(response.json())
        st.session_state["Bicicleta"] = response.json()
    if 'Bicicleta' in st.session_state:
        bike = {
            "marca": st.text_input("Insira a marca da bicicleta", ""),
            "modelo": st.text_input("Insira o modelo da bicicleta", ""),
            "cidade": st.text_input("Insira a cidade da bicicleta", ""),
            "status": st.text_input("Insira o status da bicicleta", ""),
        }
        if st.button("Atualizar"):
            response = requests.put(f'{url}/bikes/{id}', json=bike)
            if response.status_code == 201:
                st.success("Bicicleta atualizada com sucesso.")
            else:
                st.error("Erro ao atualizar bicicleta.")
        if st.button("Deletar"):
            response = requests.delete(f'{url}/bikes/{id}')
            if response.status_code == 200:
                st.success("Bicicleta deletada com sucesso.")
            else:
                st.error("Erro ao deletar bicicleta.")

##############################################################################################################################################

#EMPRÉSTIMOS

def all_emps():
    response = requests.get(f'{url}/emprestimos')
    if response.status_code == 200:
        st.table(response.json())

def get_emps_by_id( user_id, bike_id):
    response = requests.get(f'{url}/emprestimos/{user_id}/{bike_id}')
    if response.status_code == 200:
        st.table(response.json())
    else:
        st.error("Empréstimo não encontrado.")

def create_emps():
    emps = {
        "id_usuario": st.text_input("Insira o ID do usuário", ""),
        "id_bike": st.text_input("Insira o ID da bicicleta", ""),
        "data": st.text_input("Insira a data do empréstimo", ""),
    }

    if st.button("Criar Empréstimo"):
        response1 =  requests.get(f'{url}/usuarios/{emps["id_usuario"]}')
        response2 = requests.get(f'{url}/bikes/{emps["id_usuario"]}')
        if response1.status_code != 200 and response2.status_code != 200:
             st.error("Usuario ou bike não localizado.")
        else:
            response = requests.post(f'{url}/emprestimos', json=emps)
            print(response.status_code)
            if response.status_code == 201:
                st.success("Empréstimo criado com sucesso.")




def delete_emps():
    id = st.text_input("Insira o ID do empréstimo", "")
    if st.button("Deletar"):
        response = requests.delete(f'{url}/emprestimos/{id}')
        print(response.status_code)
        if response.status_code == 200:
            st.success("Empréstimo deletado com sucesso.")
        else:
            st.error("Erro ao deletar empréstimo.")
    
##############################################################################################################################################

#SIDEBAR PARA NAVEGAÇÃO

def sidebar_layout():
    st.sidebar.title("Navegação")
    page = st.sidebar.radio("Escolha a página", ["Todos os Usuários", "Usuário por ID", "Criar Usuário", "Atualizar Usuário", "Todas as Bicicletas", "Bicicleta por ID","Criar Bicicleta","Atualizar Bicicleta", "Todos os Empréstimos", "Empréstimo por ID", "Criar Empréstimo",   "Apagar Empréstimo"])

    if page == "Todos os Usuários":
        all_users()
    elif page == "Usuário por ID":
        user_id = st.text_input("Insira o ID do usuário", "")
        if st.button("Buscar"):
            get_user_by_id(user_id)
    elif page == "Criar Usuário":
        create_user()
    elif page == "Todas as Bicicletas":
        all_bikes()
    elif page == "Bicicleta por ID":
        bike_id = st.text_input("Insira o ID da bicicleta", "")
        if st.button("Buscar"):
            get_bike_by_id(bike_id)
    elif page == "Criar Bicicleta":
        create_bike()
    elif page == "Todos os Empréstimos":
        all_emps()
    elif page == "Empréstimo por ID":
        user_id = st.text_input("Insira o ID do usuário", "")
        bike_id = st.text_input("Insira o ID da bicicleta", "")
        if st.button("Buscar"):
            get_emps_by_id(user_id, bike_id)
    elif page == "Criar Empréstimo":
        create_emps()
    elif page == "Atualizar Usuário":
        data_user()
    elif page == "Atualizar Bicicleta":
        data_bike()
    elif page == "Apagar Empréstimo":
        delete_emps()

if __name__ == "__main__":
    sidebar_layout()

