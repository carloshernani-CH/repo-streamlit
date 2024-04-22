import streamlit as st
from pymongo import MongoClient
from bson import ObjectId

# Establish MongoDB connection
client = MongoClient("mongodb+srv://admin:admin@projagil.pim4mny.mongodb.net/APS5")
db = client['APS5']  # Database name
users_collection = db.usuarios  # Users collection
bikes_collection = db.bikes  # Bikes collection
loans_collection = db.emprestimos  # Loans collection

# Convert MongoDB ObjectId to string for Streamlit display
def stringify_id(item):
    item['_id'] = str(item['_id'])
    return item

# USERS
def all_users():
    users = list(map(stringify_id, users_collection.find()))
    if users:
        st.table(users)
    else:
        st.error("Nenhum usuário encontrado.")

def get_user_by_id(user_id):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        st.table(stringify_id(user))
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

def update_user(user_id):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        updated_user = {
            "nome": st.text_input("Nome", value=user['nome']),
            "cpf": st.text_input("CPF", value=user['cpf']),
            "data": st.text_input("Data de nascimento", value=user['data']),
        }
        if st.button("Atualizar Usuário"):
            result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": updated_user})
            if result.modified_count > 0:
                st.success("Usuário atualizado com sucesso.")
            else:
                st.error("Erro ao atualizar usuário.")
    else:
        st.error("Usuário não encontrado.")

def delete_user(user_id):
    if st.button("Deletar Usuário"):
        result = users_collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count > 0:
            st.success("Usuário deletado com sucesso.")
        else:
            st.error("Erro ao deletar usuário.")

# BICYCLES
def all_bikes():
    bikes = list(map(stringify_id, bikes_collection.find()))
    if bikes:
        st.table(bikes)
    else:
        st.error("Nenhuma bicicleta encontrada.")

def get_bike_by_id(bike_id):
    bike = bikes_collection.find_one({"_id": ObjectId(bike_id)})
    if bike:
        st.table(stringify_id(bike))
    else:
        st.error("Bicicleta não encontrada.")

def update_bike(bike_id):
    bike = bikes_collection.find_one({"_id": ObjectId(bike_id)})
    if bike:
        updated_bike = {
            "marca": st.text_input("Marca", value=bike['marca']),
            "modelo": st.text_input("Modelo", value=bike['modelo']),
            "cidade": st.text_input("Cidade", value=bike['cidade']),
        }
        if st.button("Atualizar Bicicleta"):
            result = bikes_collection.update_one({"_id": ObjectId(bike_id)}, {"$set": updated_bike})
            if result.modified_count > 0:
                st.success("Bicicleta atualizada com sucesso.")
            else:
                st.error("Erro ao atualizar bicicleta.")
    else:
        st.error("Bicicleta não encontrada.")

def delete_bike(bike_id):
    if st.button("Deletar Bicicleta"):
        result = bikes_collection.delete_one({"_id": ObjectId(bike_id)})
        if result.deleted_count > 0:
            st.success("Bicicleta deletada com sucesso.")
        else:
            st.error("Erro ao deletar bicicleta.")

# LOANS
def all_loans():
    loans = list(map(stringify_id, loans_collection.find()))
    if loans:
        st.table(loans)
    else:
        st.error("Nenhum empréstimo encontrado.")

def get_loan_by_id(loan_id):
    loan = loans_collection.find_one({"_id": ObjectId(loan_id)})
    if loan:
        st.table(stringify_id(loan))
    else:
        st.error("Empréstimo não encontrado.")

def delete_loan(loan_id):
    if st.button("Deletar Empréstimo"):
        result = loans_collection.delete_one({"_id": ObjectId(loan_id)})
        if result.deleted_count > 0:
            st.success("Empréstimo deletado com sucesso.")
        else:
            st.error("Erro ao deletar empréstimo.")

# Sidebar Navigation
def sidebar_layout():
    st.sidebar.title("Navegação")
    page = st.sidebar.radio("Escolha a página", ["Todos os Usuários", "Usuário por ID", "Criar Usuário", "Atualizar Usuário", "Deletar Usuário", "Todas as Bicicletas", "Bicicleta por ID", "Atualizar Bicicleta", "Deletar Bicicleta", "Todos os Empréstimos", "Empréstimo por ID", "Deletar Empréstimo"])

    if page == "Todos os Usuários":
        all_users()
    elif page == "Usuário por ID":
        user_id = st.text_input("Insira o ID do usuário", "")
        if st.button("Buscar"):
            get_user_by_id(user_id)
    elif page == "Criar Usuário":
        create_user()
    elif page == "Atualizar Usuário":
        user_id = st.text_input("Insira o ID do usuário para atualizar", "")
        update_user(user_id)
    elif page == "Deletar Usuário":
        user_id = st.text_input("Insira o ID do usuário para deletar", "")
        delete_user(user_id)
    elif page == "Todas as Bicicletas":
        all_bikes()
    elif page == "Bicicleta por ID":
        bike_id = st.text_input("Insira o ID da bicicleta", "")
        if st.button("Buscar"):
            get_bike_by_id(bike_id)
    elif page == "Atualizar Bicicleta":
        bike_id = st.text_input("Insira o ID da bicicleta para atualizar", "")
        update_bike(bike_id)
    elif page == "Deletar Bicicleta":
        bike_id = st.text_input("Insira o ID da bicicleta para deletar", "")
        delete_bike(bike_id)
    elif page == "Todos os Empréstimos":
        all_loans()
    elif page == "Empréstimo por ID":
        loan_id = st.text_input("Insira o ID do empréstimo", "")
        if st.button("Buscar"):
            get_loan_by_id(loan_id)
    elif page == "Deletar Empréstimo":
        loan_id = st.text_input("Insira o ID do empréstimo para deletar", "")
        delete_loan(loan_id)

if __name__ == "__main__":
    sidebar_layout()
