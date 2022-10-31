from flask import Flask, request, render_template, send_from_directory
from thread2txt import gettxt
app = Flask(__name__)

@app.route('/')
@app.route('/app.py')
def hello_world():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def result():
   if request.method == 'POST':
      posturl = request.form["text"]
      if not(posturl):
         return render_template("index.html", error="Error: no url provided.")
      if not(posturl.startswith("https://twitter.com/")):
         return render_template("index.html", error="Error: invalid twitter url.")
      result = gettxt(posturl)
      return render_template("index.html", result=result)

@app.route('/download', methods=['POST'])
def get_file():
    try:
        return send_from_directory(".", "results.txt", as_attachment=True)
    except FileNotFoundError:
        return render_template("index.html", error="Error: no file found.")

if __name__ == '__main__':
    app.run(debug=True)