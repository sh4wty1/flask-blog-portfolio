from app import app, db

# Iniciar o contexto da aplicação
with app.app_context():
    # Criar o banco de dados e as tabelas
    db.create_all()
    print("Banco de dados criado com sucesso!")
