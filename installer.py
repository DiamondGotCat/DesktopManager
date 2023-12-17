# installer.py

requiments = ["requests"]

numbersofprogress = 3

def install(progress):
    if progress == 1:
        print("Start download loaddesk command...")
        download_file("https://raw.githubusercontent.com/DiamondGotCat/DesktopManager/main/loaddesk","/Users/Shared/Command/")
        print("Downloaded 'loaddesk' command")
    if progress == 2:
        print("Start download savedesk command...")
        download_file("https://raw.githubusercontent.com/DiamondGotCat/DesktopManager/main/savedesk","/Users/Shared/Command/")
    if progress == 3:
        print("Start installing commands...")
        import os
        os.chdir("/Users/Shared/Command/")
        os.system("chmod 777 loaddesk")
        os.system("chmod 777 savedesk")
        os.system("""echo 'export PATH="/Users/Shared/Command/:$PATH"' >> ~/.zshrc""")
        print("Installed")

def download_file(url, save_directory):

    import os
    import requests
    response = requests.get(url)
    
    # レスポンスが成功（ステータスコードが200）の場合
    if response.status_code == 200:
        # ファイルの保存パスを生成
        file_name = url.split("/")[-1]
        save_path = os.path.join(save_directory, file_name)
        
        # ファイルをバイナリモードで書き込み
        with open(save_path, 'wb') as file:
            file.write(response.content)
        
        print(f'Saved to {save_path} ')
    else:
        print(f'Failed! Error Code: {response.status_code}')
