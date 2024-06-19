from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app,async_code='eventlet')

# 初始化遊戲狀態
board_state = [[0] * 15 for _ in range(15)]
player_score = 0
ai_score = 0

# 在這裡添加你的五子棋遊戲邏輯

# 檢查是否有五子連線
def check_winner(player):
    # 檢查直的、橫的和斜的連線
    # 省略具體實現細節，您可以根據需求自行實現

# 玩家下棋
def player_move(x, y):
    # 更新棋盤狀態
    board_state[y][x] = 1
    # 檢查是否獲勝
    if check_winner(1):
        return '玩家獲勝！'
    # 電腦移動
    ai_move()

# 電腦下棋
def ai_move():
    # 根據您的邏輯實現電腦的移動
    # 更新棋盤狀態
    # 檢查是否獲勝



if __name__ == '__main__':
    socketio.run(app, host='120.11399.47', port=5001, debug=True)
