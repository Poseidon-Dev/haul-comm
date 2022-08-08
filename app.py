from flask import Flask
import api

app = Flask(__name__)

app.add_url_rule('/', view_func=api.index)
app.add_url_rule('/queue/get/', view_func=api.get_queue)
app.add_url_rule('/queue/post/', view_func=api.post_queue)
app.add_url_rule('/equip/get/', view_func=api.get_equipment)

if __name__ == "__main__":
    app.run(debug=True, port=5001)