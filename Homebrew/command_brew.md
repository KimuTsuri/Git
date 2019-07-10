# Homebrew の基本的なコマンド

## コマンドの書き方
Homebrew の基本的なコマンドの書き方は次のようになります.
```
brew [command] [options] [formula]
```
以下では, コマンドの例を紹介します. 
例は [formula] git を想定しています.
使用する際は, gitの部分を自分が実行したい [formula] に置き換えて使用ください.

## Homebrew のアップデート
インストールした Homebrew を更新するコマンド
```
brew update
```
定期的に実行し, Homebrew を最新の状態に保ちましょう!

## インストール
Homebrew で formula をインストールするコマンド
```
brew install git
```

## アップグレード
インストールした [formula] のバージョンを更新するコマンド
```
brew upgrade git
```
ちなみに, インストールしてある [formula] と Homebrew を一緒に更新することができます.
```
brew update && brew upgrade
```

## アンインストール
インストールした [formula] をアンインストールするコマンド
```
brew uninstall git
```

## 検索
Homebrew でインストールできる [formula] の検索方法
```
brew search "git"
```
また, 検索文字列をスラッシュで囲むと, Ruby の正規表現で [formula] を検索できます.
```
brew search "/\bgit\b/"
```

## その他
インストールした formula を一覧表示
```
brew list
```
Homebrew のヘルプ表示
```
brew help
```
Homebrew で使えるコマンド一覧表示
```
brew commands
```
