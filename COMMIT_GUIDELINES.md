# リポジトリの運用指針

## 決定事項と運用指針

1. **依存関係管理**: Poetry を使用します。

2. **テスト**: `pytest` と `pytest-cov` を使用します。

3. **コードスタイル**: ほぼ PEP8 に準拠します。

4. **Git フック**: `pre-commit` を使用します。

5. **APIドキュメント**: pdoc3 を使用します。

6. **データ管理**: `data/` ディレクトリを使用します。

7. **ノートブック**: `notebooks/` ディレクトリを使用します。出力は自動的に削除してコミットされます。

8. **開発者用スクリプト**: `scripts/` ディレクトリを使用します。

9. **ユーザー用 CUI コマンド**: エントリポイントとなるスクリプトは `bin/` ディレクトリに格納します。必要に応じて `pyproject.toml` にも登録してください。

10. **バージョン方針**: セマンティック バージョニングを採用します。

11. **CHANGELOG**: `commitzen` を使用して生成します。コミットも原則 `cz c` コマンドで実行してください。コミットのログは `Conventional Commits` に従ってください。

## ディレクトリ構造

```
myproject/
├─ bin/ ... エントリポイントとなるスクリプトが格納されます
├─ data/ ... データ ファイルが格納されます
├─ myproject/ ... パッケージ本体です
├─ notebooks/ ... Jupyter Notebook が格納されます
├─ scripts/ ... 開発者用スクリプトが格納されます
├─ tests/ ... テストが格納されます
├─ CHANGELOG.md ... 自動生成された更新履歴が格納されます
├─ COMMIT_GUIDELINES.md ... 開発指針です。
├─ LICENSE ... 適宜修正してください。
├─ README.md ... ユーザーおよび開発者向けのガイドラインです。
└─ pyproject.toml ... プロジェクトの設定が格納されています。
```

## 依存関係の管理

Poetry を使用して依存関係を管理します。以下のコマンドでインストールできます。

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## テスト

`pytest` と `pytest-cov` を使用します。テストを実行するには以下のコマンドを実行してください。

```bash
poetry run pytest
```

## コードスタイル

ほぼ PEP8 に準拠します。コードフォーマッタとして `black` を使用します。

```bash
poetry run black .
```

## Git フック

`pre-commit` を使用して、コミットするたびにテストやコードフォーマットが行われるようにします。このため、初回に以下のコマンドを実行して設定します。

```bash
poetry run pre-commit install
```

## APIドキュメント

pdoc3 を使用し、コミットのたびに自動生成します。

## データ管理

`data/` ディレクトリを使用します。

## バージョン方針

セマンティックバージョニングを採用します。

**MAJOR.MINOR.PATCH**

- MAJOR: 削除などの非互換的変更
- MINOR: 下位互換の機能追加
- PATCH: バグ修正など
