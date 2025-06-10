from conexao_orm import Base, newEngine, session
from User import User
from Post import Post

#OBS: Lembrando que é necessário criar os modelos ou entidades antes de iniciar a criação das tabelas, pois a configuração de como será a tabela estão nas nossas entidades User e Post

#Criando a tabela
Base.metadata.create_all(newEngine)

#Função para exibir o menu de opções
def show_menu():
    print("Menu de opções:")
    print("1 - Adicionar Usuário")
    print("2 - Adicionar Post")
    print("3 - Consultar Usuários e Seus Posts")
    print("4 - Sair")

# Função para adicionar usuário
def add_user():
    print("Adicionar novo usuario:\n")
    name = input("Nome:\n")
    email = input("Email:\n")
    user = User(name, email) #Criando uma instância da classe User.
    session.add(user) #Criando uma sessão para simplificação dos dados passados em user, que será persistido no banco de dados
    session.commit() #Salvando as alterações no banco de dados
    print("Usuário adicionado com sucesso!")

#Função para adicionar novo Post
def add_post():
    print("Adicionar novo Post:\n")
    title = input("Digite o título do post:\n")
    content = input("Digite o conteúdo do post\n")
    author_id = int(input("Id do author:\n"))
    user = session.query(User).filter_by(id=author_id).first()
    if user:
        post = Post(title, content, user) #Instancia de Post
        session.add(post) #Persistindo as informações no banco de dados
        session.commit() #Salvando as informações no banco de dados
        print("Post adicionado com sucesso!")
    else:
        print("Usuário não encontrado!")

#Função para consultar usuários e posts
def query_users_posts():
    users = session.query(User).join(User.posts).order_by(User.name).all() #Utilizando o join para buscar os dados do usuário, e seus posts relacionados a esse usuário
    for user in users: #Iteragindo dados com o usuário
        print(f"\nUser: {user.name}, Email: {user.email}")
        for post in user.posts: #Iterando dados do Post com o usuário
            print(f"Post: {post.title}, Conteúdo: {post.content}")
