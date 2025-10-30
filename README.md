# ReferenceManeger
Elsevierが出しているReference ManegerのMendeleyに論文リストを一括でアップデートするためのプログラムです。  

## Mendeley
Mendeleyはこちらからインストールしてください。  
いずれも必要になります。
Mendeley内のリファレンスはElsevierのアカウントに紐づいているのでElsevierのアカウント登録もしておきましょう。  
（Mendeleyのサイトに行った際に登録を求められるはず。）  
- [Mendeley Reference Maneger](https://www.mendeley.com/reference-management/reference-manager)  
  リファレンス管理用のアプリ  

- [Mendeley Web Importer](https://www.mendeley.com/reference-management/web-importer)  
  webからリファレンスの情報を入手するwebブラウザのアドイン

- [Mendeley Pulg-in](https://www.mendeley.com/reference-management/mendeley-cite)  
  Microsoft wordのアドイン  

## Mendeleyの使い方
基本的にはNCBIなどで論文のサイトに行き、（Google chromeだと右上）にあるMendeley（赤色）をクリックし、web importerを起動させMendeley Reference Manegerにインポートするだけです。  
詳しくは[mendelry web importerでの論文データ取得方法](https://guides.lib.kyushu-u.ac.jp/referencemanagementtool/webimporter)を見てください。  

## PubMeta
これは論文のリンクからMendeleyへ一括でインポートするためのアプリです。  
論文のリンクをテキストファイルにまとめてこのアプリで実行するとHTML形式でメタデータを出力してくれるのでweb上で公開すればMendeleyに一括でインポートできます。  
```python
python3 PubMeta.py 
```
Biopythonが必要になるので必要に応じてインストールしてください。  
```Python
python3 -m pip install biopython
```

作成者はGitHub上にアップロードし、web上に公開することで一括インストールしてます。  

### GitHubからweb上に公開する方法
1. GitHubにログイン
👉 https://github.com にアクセスしてログイン。
まだアカウントがない場合は無料で作成できます。

⸻

2. 新しいリポジトリを作成
	1.	右上の「＋」→ New repository をクリック
	2.	以下を設定：
	    - Repository name：例 mendeley-test
	    - Public（公開）を選択（※GitHub PagesはPublic限定）
	    - 他の設定はそのままでOK
	3.	Create repository をクリック

⸻

3.  HTMLファイルをアップロード
	1.	作成したリポジトリページで「Add file → Upload files」をクリック
	2.	ファイル選択画面が出るので、myref.html をドラッグ＆ドロップ
	3.	ページ下部の「Commit changes」ボタンをクリックして保存

→ これでHTMLがGitHubにアップロードされました。

⸻

4. GitHub Pagesを有効化
	1.	リポジトリの上部メニューから「Settings（設定）」をクリック
	2.	左メニューで「Pages」を選択
	3.	「Source」の設定欄で：
	    - Branch：main
	    - Folder：/(root)
	4.	「Save」をクリック

⸻

5. 公開URLを確認
    1. 数十秒後、画面上部に👇のようなURLが表示されます：
        ```text
        Your site is live at https://<ユーザー名>.github.io/<リポジトリ名>/
        ```
    2. このURLにアクセスすると、myref.html の内容がブラウザに表示されます
