import os

# サンプルのEMLファイルの内容を生成
eml_content_list = [
    """From: someone@example.com
To: recipient@example.com
Subject: Test Email 1
Date: Mon, 1 Jan 2023 12:34:56 +0000
Content-Type: text/plain; charset="utf-8"

Hello, this is the content of test email 1.
""",
    """From: someone@example.com
To: recipient@example.com
Subject: Test Email 2
Date: Tue, 2 Jan 2023 12:34:56 +0000
Content-Type: text/plain; charset="utf-8"

Hello, this is the content of test email 2.
""",
    """From: someone@example.com
To: recipient@example.com
Subject: Test Email 3
Date: Wed, 3 Jan 2023 12:34:56 +0000
Content-Type: text/plain; charset="utf-8"

Hello, this is the content of test email 3.
""",
    """From: someone@example.com
To: recipient@example.com
Subject: Test Email 4
Date: Thu, 4 Jan 2023 12:34:56 +0000
Content-Type: text/plain; charset="utf-8"

Hello, this is the content of test email 4.
""",
    """From: someone@example.com
To: recipient@example.com
Subject: Test Email 5
Date: Fri, 5 Jan 2023 12:34:56 +0000
Content-Type: text/plain; charset="utf-8"

Hello, this is the content of test email 5.
"""
]

# trainフォルダが存在しない場合は作成
os.makedirs('train', exist_ok=True)

# 5つのEMLファイルを生成
for i, content in enumerate(eml_content_list):
    with open(f'train/TEST_EMAIL_{i+1:04d}.eml', 'w') as f:
        f.write(content)

print("5つのEMLファイルを生成しました。")