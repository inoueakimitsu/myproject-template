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
    poetry run pre-commit
    ```

### コミット手順

1. **初回のみタグを手動作成**
    - 最初のコミットを作成し、バージョンのタグを作成します。(tag は pyproject.toml に記載の内容と合わせてください)
      ```bash
      git commit --allow-empty -m "first commit"
      git tag -a "0.1.0" -m "first version"
      ```

2. **コミット**:
    - `commitizen` を使用して以下のコマンドによりコミットを行ってください。
    ```bash
    git add <該当ファイル>
    poetry run pre-commit  # この結果により、修正や re-staging が必要なファイルが生じたら修正し git add し直してください。
    poetry run cz commit
    ```

3. **バージョンアップ**
   - バージョンアップは、手動で行うように設定されています。以下のコマンドを実行してください。
     ```bash
     poetry run cz bump
     ```
   - コンフリクトを防ぐため、バージョン番号のインクリメントは `main` ブランチでのみ行ってください。

### そのほかのガイド

1. **そのほかの指針**
    - そのほかの開発の指針は `COMMIT_GUIDELINES.md` を参照してください。
