# myproject

これは myproject の解説です。

## インストール

## 使用方法

## 開発者向け

### 開発環境の構築

1. **Poetry のインストール**:
    - Poetry は Python の依存関係管理ツールです。以下のコマンドでインストールできます。
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. **プロジェクトのクローン**:
    - プロジェクトをローカルにクローンします。
    ```bash
    # git clone https://your-repo-url.git
    cd myproject
    ```

3. **依存関係のインストール**:
    - Poetry を使用してプロジェクトの依存関係をインストールします。
    ```bash
    poetry install
    ```

4. **pre-commit の設定**:
    - `pre-commit` を使用して、コミットするたびにテストやコードフォーマットが行われるようにします。このため、初回に以下のコマンドを実行して設定します。
    ```bash
    poetry run pre-commit install
    ```

5. **テストの実行**:
    - プロジェクトのテストを実行して、全てが正常に動作しているか確認します。
    ```bash
    poetry run pytest
    ```

### コミット手順

1. **コミット**:
    - `commitzen` を使用して以下のコマンドによりコミットを行ってください。
    ```bash
    poetry run commitzen commit  # または poetry run cz c
    ```
    - コンフリクトを防ぐため、バージョン番号のインクリメントは `main` ブランチでのみ行ってください。

### そのほかのガイド

1. **そのほかの指針**
    - そのほかの開発の指針は `COMMIT_GUIDELINES.md` を参照してください。
