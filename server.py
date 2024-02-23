from flask import Flask
from flask import url_for
from assitant.assitant import assitant 
from flask import request

app = Flask(__name__, static_folder='static', static_url_path="/")
assitant = assitant()

@app.route('/control_api', methods=['POST'])
def control_api():
    if request.json['content'] == 'begin_recording':
        print('begin_recording_begin_')
        assitant.begin_recording()
        print('begin_recording_end_')
        return ' '
    
    elif request.json['content'] == 'end_recording':
        print('end_recording_begin_')
        assitant.end_recording()
        assitant.processing()
        print('end_recording_end_')
        return ' '

    elif request.json['content'] == 'begin_playing':
        print('begin_playing__begin_')
        assitant.play()
        print('begin_playing_end_')
        return ' '

if __name__ == '__main__':
    app.run()