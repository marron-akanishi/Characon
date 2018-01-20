# Characon
このスクリプトはキャラの誕生日に自動的にTwitterのアイコンを変更します。

## 動作環境
Python 3です。  
pipでtweepyをインストールしてください。  

## 使い方
まず、birth.csvに`キャラ名,誕生日,アイコンファイルパス`を記述します。  
リポジトリに元々入ってるものはミリマスのキャラ一覧です。参考にしてください。  
次にoauth_sample.pyを開き、中にTwitterのAPIキーを記述します。その後、oauth.pyとして保存しておきます。  
最後にサーバー等の常時起動しているPCで毎日0時にmain.pyが実行されるようにします。  
以上です。