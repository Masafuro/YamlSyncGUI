import yaml
import os

def load_yaml(file_path):
    """
    指定されたパスからYAMLファイルを読み込み、辞書形式で返す。
    ファイルが存在しない、空のファイル、不正な構文のファイルでは標準の例外を発生させる。
    
    Args:
        file_path (str): 読み込むYAMLファイルのパス。
    
    Returns:
        dict: YAMLファイルの内容を辞書形式で返す。
    
    Raises:
        FileNotFoundError: ファイルが存在しない場合。
        ValueError: ファイルが空の場合や、不正なYAML構文がある場合。
    """
    abs_path = os.path.abspath(file_path)
    
    # ファイルが存在しない場合のエラーハンドリング
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {abs_path} was not found.")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            
            # ファイルが空の場合のエラーハンドリング
            if data is None:
                raise ValueError(f"The file at {abs_path} is empty or contains only comments.")
            
            return data
    except yaml.YAMLError as e:
        raise ValueError(f"Failed to load YAML file at {abs_path} due to a YAML error: {e}")

# テスト用のmain関数
if __name__ == "__main__":
    file_path = "../../settings/tests/empty.yaml"  # テスト用YAMLファイルのパスを指定
    try:
        data = load_yaml(file_path)
        print("YAML data loaded successfully:")
        print(data)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
    
