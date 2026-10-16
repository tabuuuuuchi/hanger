# Hanger

Hangerは、持っている服や小物を登録し、アイテムを組み合わせたコーディネートを管理するWebアプリケーションです。ユーザーごとにアイテムとコーディネートを整理できます。

## 主な機能

- アイテムの登録・詳細表示・編集・削除
- アイテムのカテゴリ、ブランド、サムネイル画像の管理
- アイテム名・ブランド名での検索
- コーディネートの登録・詳細表示・編集・削除
- コーディネートへのアイテム追加と、春・夏・秋・冬の季節設定
- ユーザー登録、ログイン、ログアウト

## 使用技術

- Python / Django
- SQLite
- Pillow（画像アップロード）
- django-cleanup（不要になった画像ファイルの削除）

## セットアップ

Pythonが利用できる環境で、プロジェクトのルート（`manage.py`があるディレクトリ）から実行してください。

1. 仮想環境を作成して有効化します。

	```bash
	python -m venv .venv
	source .venv/bin/activate
	```

	Windowsでは仮想環境を次のコマンドで有効化します。

	```powershell
	.venv\Scripts\Activate.ps1
	```

2. 必要なパッケージをインストールします。

	```bash
	python -m pip install Django Pillow django-cleanup
	```

3. データベースを準備します。

	```bash
	python manage.py migrate
	```

## 起動方法

```bash
python manage.py runserver
```

ブラウザーで <http://127.0.0.1:8000/> を開いてください。アカウント登録は `/accounts/signup/`、ログインは `/accounts/login/` から行えます。アイテムやコーディネートの管理にはログインが必要です。

## 画像とデータベース

データベースにはSQLiteを使用し、初期設定ではプロジェクト直下の `db.sqlite3` に保存します。アップロードした画像は `media/` に保存されます。ローカル開発用の設定では、開発サーバーからメディアファイルを配信します。

## 開発用管理画面

管理者アカウントを作成すると、Django管理画面を利用できます。

```bash
python manage.py createsuperuser
```

サーバー起動後、<http://127.0.0.1:8000/admin/> にアクセスしてください。
