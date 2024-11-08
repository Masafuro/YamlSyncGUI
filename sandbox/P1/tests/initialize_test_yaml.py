import yaml
import os
from datetime import datetime

def initialize_test_yaml(yaml_file):
    """
    指定されたYAMLファイルを読み込み、必要に応じて初期化する。
    初期化では、tests内のresultとnotesをクリアし、test_datetimeを現在の日時に更新する。
    
    Args:
        yaml_file (str): 初期化するYAMLファイルのパス。
    """
    # YAMLファイルの読み込み
    try:
        with open(yaml_file, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        abs_path = os.path.abspath(yaml_file)
        print(f"Error: The file {abs_path} was not found.")
        return
    except yaml.YAMLError as e:
        abs_path = os.path.abspath(yaml_file)
        print(f"Error: Failed to load YAML file at {abs_path} due to a YAML error: {e}")
        return

    # 初期化の確認プロンプト
    user_input = input("Do you want to initialize the test results in this YAML file? (y/n): ")
    if user_input.lower() != 'y':
        print("Initialization canceled.")
        return

    # 現在の日付と時刻をISOフォーマットで取得
    current_datetime = datetime.now().isoformat(timespec='seconds')

    # 日時の更新
    data['test_datetime'] = current_datetime

    # testsセクション内のresultとnotesの内容を削除
    if 'tests' in data:
        for test in data['tests']:
            test['result'] = ""
            test['notes'] = ""

    # 更新した内容をファイルに書き戻す
    try:
        with open(yaml_file, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
        print("Test results have been initialized successfully.")
    except IOError as e:
        print(f"Error: Could not write to file {yaml_file}: {e}")

# 使用例
if __name__ == "__main__":
    yaml_file_path = "../python/core/tests/validate_color_yaml_structure/validate_color_yaml_structure.yaml"  # テスト用YAMLファイルのパスを指定
    initialize_test_yaml(yaml_file_path)
