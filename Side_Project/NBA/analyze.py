"""
pip install mysql-connector-python pandas matplotlib
"""
import mysql.connector
from mysql.connector import Error
import pandas as pd
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO,
# logging.basicConfig(level=logging.CRITICAL,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='open',
            database='NBA'
        )
        logging.info("資料庫連接成功")
        return connection
    except Error as e:
        logging.error(f"資料庫連接錯誤: {e}")
        return None

def fetch_player_data(cursor, player_name):
    query = f"SELECT * FROM Regular_Season WHERE Player_Name = '{player_name}';"
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return pd.DataFrame(result, columns=columns)

def analyze_and_plot(jordan_df, lebron_df):
    players = ['Michael Jordan', 'LeBron James']

    # 計算數據
    total_points = [jordan_df['PTS'].sum(), lebron_df['PTS'].sum()]
    avg_points = [jordan_df['PTS'].mean(), lebron_df['PTS'].mean()]
    fg_percentage = [jordan_df['FG_Percentage'].mean(), lebron_df['FG_Percentage'].mean()]
    tp_percentage = [jordan_df['3P_Percentage'].mean(), lebron_df['3P_Percentage'].mean()]
    twop_percentage = [jordan_df['2P_Percentage'].mean(), lebron_df['2P_Percentage'].mean()]
    total_assists = [jordan_df['AST'].sum(), lebron_df['AST'].sum()]
    total_rebounds = [jordan_df['TRB'].sum(), lebron_df['TRB'].sum()]
    total_steals = [jordan_df['STL'].sum(), lebron_df['STL'].sum()]
    total_blocks = [jordan_df['BLK'].sum(), lebron_df['BLK'].sum()]

    # 繪圖
    plt.rcParams['font.family'] = 'Microsoft JhengHei'  # 設置中文字體
    fig, ax = plt.subplots(3, 3, figsize=(18, 18))
    fig.suptitle("Michael Jordan 和 LeBron James 的數據比較")

    colors = ['#CE0000', '#FFD700']  # 設置顏色，紅色和深黃色

    # 總得分
    ax[0, 0].bar(players, total_points, color=colors)
    ax[0, 0].set_title('總得分')

    # 平均得分
    ax[0, 1].bar(players, avg_points, color=colors)
    ax[0, 1].set_title('平均得分')

    # 投籃命中率
    ax[0, 2].bar(players, fg_percentage, color=colors)
    ax[0, 2].set_title('投籃命中率')

    # 三分球命中率
    ax[1, 0].bar(players, tp_percentage, color=colors)
    ax[1, 0].set_title('三分球命中率')

    # 兩分球命中率
    ax[1, 1].bar(players, twop_percentage, color=colors)
    ax[1, 1].set_title('兩分球命中率')

    # 總助攻
    ax[1, 2].bar(players, total_assists, color=colors)
    ax[1, 2].set_title('總助攻')

    # 總籃板
    ax[2, 0].bar(players, total_rebounds, color=colors)
    ax[2, 0].set_title('總籃板')

    # 總抄截
    ax[2, 1].bar(players, total_steals, color=colors)
    ax[2, 1].set_title('總抄截')

    # 總封蓋
    ax[2, 2].bar(players, total_blocks, color=colors)
    ax[2, 2].set_title('總封蓋')

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def main():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        jordan_df = fetch_player_data(cursor, 'Michael Jordan')
        lebron_df = fetch_player_data(cursor, 'LeBron James')

        analyze_and_plot(jordan_df, lebron_df)

        cursor.close()
        connection.close()
    else:
        logging.error("無法建立資料庫連接")

if __name__ == "__main__":
    main()

