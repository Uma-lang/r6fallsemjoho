# -*- coding: utf-8 -*-
from socket import *
import sys, csv

def main():
    # ポート番号とサービス名を格納するリスト
    portnumbers = []
    
    # CSVファイルからポート番号とサービス名を読み込む
    with open('port-number.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # ヘッダー行をスキップ
        for row in reader:
            portnumbers.append(row)

    # ポート番号と対応するサービス名を辞書に格納
    port_service_map = {int(row[0]): row[1] for row in portnumbers}

    # コマンドライン引数の確認
    if len(sys.argv[1:]) == 3:
        ip = sys.argv[1]
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
    else:
        sys.exit()

    # ポート範囲の確認
    if start_port < 0 or end_port > 65535 or start_port > end_port:
        print("error")
        sys.exit()

    for port in range(start_port, end_port + 1):
        try:
            # ストリームソケットの作成
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(1)  # タイムアウトを1秒に設定
            result = s.connect_ex((ip, port))  # ポートに接続を試みる

            # 接続成功（ポートが開いている）
            if result == 0:
                # 辞書からポートに対応するサービス名を取得
                service_name = port_service_map.get(port, "不明なサービス") #デフォルトは"不明なサービス"
                print(f"{port}: open (サービス: {service_name})")
            else:
                print(f"{port}: time out")

            s.close()

        except error as msg:
            print(f"{port}: {msg}")
            

if __name__ == "__main__":
    main()