from flask import Flask,request

app =Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return "Index page"
  return "Post"

if __name__=='__main__':
  app.run(debug=True)