from flask import Flask, request, render_template
from flask_cors import CORS
from pydub import AudioSegment
from time import sleep
import os

app = Flask(__name__, static_url_path="/static", static_folder='./static')
CORS(app)

# preprocessing audio
def preprocessing(folder, path):
    audios = set()
    # CONVERT MP3 -> WAV
    type_file = path.split(".")[-1]
    sound = AudioSegment.from_file(path, type_file)

    # SPLIT AUDIO
    time_audio = int(sound.duration_seconds / 30) + 1
    for i in range(time_audio):
        t1 = i * 30 * 1000
        t2 = (i+1) * 30 * 1000
        newAudio = sound[t1:t2]

        newAudio.set_channels(1)   # single channel --> mono channel
        newAudio = newAudio.set_frame_rate(16000)    # convert frequency : mọi freq --> 16000kHz
        # print(newAudio.frame_rate)
        # print(newAudio.split_to_mono())

        audio_path = os.path.join(folder,  str(i) + '.wav')
        newAudio.export(audio_path, format="wav") 
        audios.add(audio_path)

    return audios


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def predic_upload():
    print('upload file')
    if request.method == 'POST':
        # Lấy dữ liệu âm thanh người dùng vừa tải lên
        _file = request.files['file']
        if _file.filename == '':
            return render_template('index.html', predict="", error="File không hợp lệ")
        
        # Lưu file vừa tải lên
        print('\n\nfile uploaded:',_file.filename)
        _file.save('./static/upload/' + _file.filename)
        print('Write file success!')

        # Audio preprocessing
        audio_path='./static/upload/' + _file.filename
        # Hàm preprocessing trả về một set(danh sách các đường dẫn file được tách file/30s)
        audios = preprocessing("./static/upload/", audio_path)
        print(audios)

        # model dự đoán
        predict = "dạ mobifone xin nghe em là minh anh có thể giúp được gì cho anh chị ạ chị kiểm tra giùm em cái số điện thoại này gọi lên đó em mới cài ba g d mười á mà không hoạt động nó không chạy được luôn á chị dạ vâng rất xin lỗi về sự bất tiện này cho em xin anh tên gì để em tiện xưng hô được không ạ dạ em tên minh dạ em chào anh minh số anh minh đây em kiểm tra là đúng là có đăng ký gói cước d mười cho mở thiết bị di động máy hiện ba g bốn g hay kiểu gì vậy anh minh dạ chữ h chị dạ vâng mình sẽ hỗ trợ đóng nối mở nối lại đường truyền truy cập mạng cho sim của anh minh lại kết thúc cuộc gọi này anh thông cảm tắt nguồn máy hai phút sau anh mở nguồn nên bật lại dùng lại thử xem được chưa nha được rồi ok em cám ơn dạ mình cần hỗ trợ thông tin"
        
        # delete log audio 
        path = r"./static/upload/"
        for file_name in os.listdir(path):
            # construct full file path
            file = path + file_name
            if os.path.isfile(file):
                print('Deleting file:', file)
                os.remove(file)

    return render_template('index.html', predict=predict, audio_path=audio_path)


if __name__ == "__main__":
    app.run(debug=True)