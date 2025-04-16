from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)
app.secret_key = "admin"

# Configuração do banco de dados (SQLite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Modelo de Post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Post {self.title}>"

    def formatted_date(self):
        br_tz = pytz.timezone("America/Sao_Paulo")
        local_date = self.date.replace(tzinfo=pytz.utc).astimezone(br_tz)
        return local_date.strftime("%d/%m/%Y - %H:%M")


# Página inicial
@app.route("/")
def home():
    posts = Post.query.all()  # Buscar todos os posts do banco de dados
    return render_template("index.html", posts=posts)


@app.route("/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        flash("Post created successfully!", "success")
        return redirect(url_for("home"))
    return render_template("new_post.html")


# Rota para remover um post
@app.route("/confirm_delete/<int:id>", methods=["GET", "POST"])
def confirm_delete(id):
    post = Post.query.get_or_404(id)  # Buscar post pelo ID

    if request.method == "POST":
        # Verificar se o usuário digitou "DELETE"
        if request.form["confirmation"].upper() == "DELETE":
            db.session.delete(post)
            db.session.commit()
            flash("Post excluído com sucesso!", "success")
            return redirect(url_for("home"))
        else:
            flash("Por favor, digite 'DELETE' para confirmar.", "danger")

    return render_template("confirm_delete.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
