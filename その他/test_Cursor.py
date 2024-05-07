import requests
# ドキュメント追加前
def update_user_profile(user_id, profile_data):
    """ReproのユーザプロフィールバスクインポートAPIにリクエストを送り、ユーザプロフィールを更新する

    Args:
        user_id (str): 更新するユーザーのID
        profile_data (dict): 更新するプロフィールデータ

    Returns:
        dict: APIレスポンス
    """
    url = f"https://api.repro.io/v2/user/profile/{user_id}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer あなたのアクセストークン'
    }
    response = requests.post(url, json=profile_data, headers=headers)
    return response.json()

# ドキュメント追加後
def bulk_import_user_profiles(api_token, csv_file_path):
    """ReproのユーザプロフィールバルクインポートAPIにCSVファイルをPOSTして、複数のユーザプロフィールを更新する

    Args:
        api_token (str): Repro API トークン
        csv_file_path (str): アップロードするCSVファイルのパス

    Returns:
        dict: APIレスポンス
    """
    url = "https://api.reproio.com/v3/user_profiles/bulk_import"
    headers = {
        'Content-Type': 'text/csv',
        'X-Repro-Token': api_token
    }
    with open(csv_file_path, 'rb') as csv_file:
        response = requests.post(url, headers=headers, data=csv_file)
    return response.json()


