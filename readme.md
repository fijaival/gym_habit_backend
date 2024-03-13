https://zenn.dev/sh0nk/books/537bb028709ab9/viewer/281ee0

## 起動

### イメージの構築

dockerfile を更新したときなど、キャッシュを使用したくないときは、`--no-cache` オプションを付ける

```
docker-compose build
```

### コンテナ構築・起動

up コマンドでは、キャッシュがある場合はそれを使って一発でイメージの構築から、コンテナの構築・起動までします。<br>
キャッシュがない場合は `--build` オプションをつけることで、イメージの構築から、コンテナの構築・起動までしてくれます。<br>
新しいサービスを初めて立ち上げる場合はもちろんキャッシュはないので` docker-compose up --build` コマンドを使う。

```
docker-compose up
```

`http://localhost:3000/`でアクセス可能になります

### すべて削除

```
docker-compose down --rmi all --volumes --remove-orphans
```

### コンテナ停止・削除、ネットワーク削除

```
docker-compose down

```

### イメージ削除

```
docker-compose down --rmi all

```

### ボリューム削除

```
docker-compose down -v

```

### 安全なクリーンアップ

```
docker-compose down --rmi all -v

```
