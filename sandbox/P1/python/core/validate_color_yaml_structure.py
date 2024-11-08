import yaml
import re

def validate_color_yaml_structure(data):
    """
    universal_colors.yamlのデータ構造が正しいかを検証する。
    
    Args:
        data (dict): YAMLファイルから読み込んだ辞書形式のデータ。
    
    Raises:
        KeyError: トップレベルのキー 'colors' が存在しない場合。
        TypeError: 'colors' の値が辞書でない場合。
        ValueError: カラーコードの形式が不正な場合、または色名が重複している場合。
    """
    # 1. トップレベルのキーが "colors" であることを確認
    if 'colors' not in data:
        raise KeyError("Top-level key 'colors' is missing.")
    
    # 2. "colors" の値が辞書であることを確認
    colors = data['colors']
    if not isinstance(colors, dict):
        raise TypeError("The 'colors' key should contain a dictionary of color names and hex values.")
    
    # 3. 色名が重複していないことを確認
    color_names = set()
    for color_name in colors.keys():
        if color_name in color_names:
            raise ValueError(f"Duplicate color name found: {color_name}")
        color_names.add(color_name)
    
    # 4. 各カラーコードが正しい形式であることを確認
    hex_pattern = re.compile(r'^#[0-9A-Fa-f]{6}$')
    for color_name, color_code in colors.items():
        if not isinstance(color_code, str) or not hex_pattern.match(color_code):
            raise ValueError(f"Color code for '{color_name}' is invalid: {color_code}")

    # 5. サポート外のトップレベルキーが存在しないことを確認
    supported_keys = {'colors'}
    for key in data.keys():
        if key not in supported_keys:
            raise ValueError(f"Unsupported top-level key found: {key}")

    print("Validation passed: The structure of the color YAML file is correct.")
    return True



# テスト用のmain関数
if __name__ == "__main__":
    file_name = "duplicate_color_name.yaml"
    file_path = f"../../settings/tests/validate_color_yaml_structure/{file_name}"
    try:
        # YAMLファイルを読み込み
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        
        # 構造の検証
        is_valid = validate_color_yaml_structure(data)
        print(f"Validation result: {is_valid}")
    except (KeyError, TypeError, ValueError) as e:
        print(f"Validation error: {e}")
