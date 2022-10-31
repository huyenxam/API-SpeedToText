from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__, static_url_path="/static", static_folder='./static')
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def predic_upload():
    print('upload file')
    if request.method == 'POST':
        _file = request.files['file']
        if _file.filename == '':
            return render_template('index.html', predict="", error="File không hợp lệ")
            
        print('\n\nfile uploaded:',_file.filename)
        _file.save('static/upload/' + _file.filename)
        print('Write file success!')

        # model dự đoán
        audio_path='static/upload/' + _file.filename
        predict = "Nguyen Thi Ngoc Huyen"

    return render_template('index.html', predict=predict, audio_path=audio_path)


if __name__ == "__main__":
    app.run(debug=True)