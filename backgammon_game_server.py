from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app,async_code='eventlet')

# 初始化遊戲狀態
board_state = [[0] * 15 for _ in range(15)]
player_score = 0
ai_score = 0

# 在這裡添加你的五子棋遊戲邏輯
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/move', methods=['POST'])
def move():
    x = int(request.form.get('x'))
    y = int(request.form.get('y'))
    board[y][x] = 1
    if check_winner(1):
        return {'winner': 'player'}
    ai_move()
    if check_winner(2):
        return {'winner': 'ai'}
    return {}
@socketio.on('player_move')
def handle_player_move(data):
    x = data['x']
    y = data['y']
    # 在這裡處理玩家的移動，並更新遊戲狀態
    # 如果玩家贏了，則發送一個消息
    # emit('player_wins', {'message': '玩家獲勝！'})

@socketio.on('ai_move')

# 電腦下棋
def ai_move():
    while True:
        x = random.randint(0, 14)
        y = random.randint(0, 14)
        if board[y][x] == 0:
            board[y][x] = 2
            break
 # 檢查玩家獲勝
def check_winner(player):
    for y in range(15):
        for x in range(15):
            if check_direction(x, y, 1, 0, player) or check_direction(x, y, 0, 1, player) or check_direction(x, y, 1, 1, player) or check_direction(x, y, 1, -1, player):
                return True
    return False

 # 檢查棋盤狀態
def check_direction(x, y, dx, dy, player):
    for i in range(5):
        if x + i * dx < 0 or x + i * dx >= 15 or y + i * dy < 0 or y + i * dy >= 15 or board[y + i * dy][x + i * dx] != player:
            return False
    return True

if __name__ == '__main__':
    socketio.run(app, host='120.11399.47', port=5001, debug=True)
