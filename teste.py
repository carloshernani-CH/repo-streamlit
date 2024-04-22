import streamlit as st
from pymongo import MongoClient

# Establish MongoDB connection
client = MongoClient("mongodb+srv://admin:admin@projagil.pim4mny.mongodb.net/APS5")
db = client['APS5']  # Database name
users_collection = db.usuarios  # Users collection
bikes_collection = db.bikes  # Bikes collection
loans_collection = db.emprestimos  # Loans collection

# USERS

def all_users():
    users = list(users_collection.find())
    if users:
        st.table(users)
    else:
        st.error("Nenhum usuário encontrado.")

def get_user_by_id(user_id):
    user = users_collection.find_one({"_id": user_id})
    if user:
        st.table(user)
    else:
        st.error("Usuário não encontrado.")

def create_user():
    user = {
        "nome": st.text_input("Insira o nome do usuário", ""),
        "cpf": st.text_input("Insira o CPF do usuário", ""),
        "data": st.text_input("Insira a data de nascimento do usuário", ""),
    }

    if st.button("Criar Usuário"):
        result = users_collection.insert_one(user)
        if result.acknowledged:
            st.success("Usuário criado com sucesso.")
        else:
            st.error("Erro ao criar usuário.")

# BICYCLES

def all_bikes():
    bikes = list(bikes_collection.find())
    if bikes:
        st.table(bikes)
    else:
        st.error("Nenhuma bicicleta encontrada.")

def get_bike_by_id(bike_id):
    bike = bikes_collection.find_one({"_id": bike_id})
    if bike:
        st.table(bike)
    else:
        st.error("Bicicleta não encontrada.")

# LOANS

def all_loans():
    loans = list(loans_collection.find())
    if loans:
        st.table(loans)
    else:
        st.error("Nenhum empréstimo encontrado.")

def get_loan_by_id(user_id, bike_id):
    loan = loans_collection.find_one({"user_id": user_id, "bike_id": bike_id})
    if loan:
        st.table(loan)
    else:
        st.error("Empréstimo não encontrado.")

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
        get_bike_by_id(bike_id)
    elif page == "Todos os Empréstimos":
        all_loans()

if __name__ == "__main__":
    sidebar_layout()
