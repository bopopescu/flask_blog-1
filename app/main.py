from app import app
from posts.blueprint import posts
import view # не удалять, для того, чтобы фласк видел начальную вьюху

app.register_blueprint(posts, url_prefix='/blog')


if __name__ == '__main__':
    app.run()
