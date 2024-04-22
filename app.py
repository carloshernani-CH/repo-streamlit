import streamlit as st
import requests

url = "mongodb+srv://admin:admin@projagil.pim4mny.mongodb.net/APS5"

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
    }

    if st.button("Criar Bicicleta"):
        response = requests.post(f'{url}/bikes', json=bike)
        if response.status_code == 201:
            st.success("Bicicleta criada com sucesso.")
        else:
            st.error("Erro ao criar bicicleta.")

#EMPRÉSTIMOS

def all_loans():
    response = requests.get(f'{url}/emprestimos')
    if response.status_code == 200:
        st.table(response.json())

def get_loan_by_id( user_id, bike_id):
    response = requests.get(f'{url}/emprestimos/usuarios/{user_id}/bikes/{bike_id}')
    if response.status_code == 200:
        st.table(response.json())
    else:
        st.error("Empréstimo não encontrado.")

def create_loan():
    loan = {
        "user_id": st.text_input("Insira o ID do usuário", ""),
        "bike_id": st.text_input("Insira o ID da bicicleta", ""),
        "data": st.text_input("Insira a data do aluguel", ""),
    }

    if st.button("Criar Empréstimo"):
        response1 =  requests.get(f'{url}/usuarios/{loan["user_id"]}')
        response2 = requests.get(f'{url}/bikes/{loan["bike_id"]}')
        if response1.status_code != 200 and response2.status_code != 200:
            st.error("Erro ao criar empréstimo.")
        else:
            response = requests.post(f'{url}/emprestimos/usuarios/{loan["user_id"]}/bikes/{loan["bike_id"]}', json=loan)
            if response.status_code == 201:
                st.success("Empréstimo criado com sucesso.")
            else:
                st.error("Erro ao criar empréstimo.")
    

def sidebar_layout():
    st.sidebar.title("Navegação")
    page = st.sidebar.radio("Escolha a página", ["Todos os Usuários", "Usuário por ID", "Criar Usuário", "Todas as Bicicletas", "Bicicleta por ID", "Todos os Empréstimos"])

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
    elif page == "Todos os Empréstimos":
        all_loans()
    elif page == "Empréstimo por ID":
        user_id = st.text_input("Insira o ID do usuário", "")
        bike_id = st.text_input("Insira o ID da bicicleta", "")
        if st.button("Buscar"):
            get_loan_by_id(user_id, bike_id)
    elif page == "Criar Empréstimo":
        create_loan()


if __name__ == "__main__":
    sidebar_layout()

