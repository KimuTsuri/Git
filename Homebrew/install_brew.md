# Homebrew のインストール

Homebrew 公式サイトを参考にし, Homebrew を導入します.
https://docs.brew.sh/Installation

## Xcode のインストール

Homebrew を使うには, Xcode の Command Line Tools が必要になります.
ターミナルで次のコマンドを実行し, Xcode をインストールします. 

```
$ xcode-select --install
```

コマンドを実行すると,  インストーラーが表示されます.
インストーラーに従ってインストールを完了させます.

```
$ xcode-select -v
```

を実行する.
これで Xcode のバージョンが表示されれば, インストールが出来ています.

## Homebrew のインストール

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install
```

このスクリプトをターミナルに貼り付け実行して下さい.スクリプトは, Homebrew 公式サイトにあります.

```
Press RETURN to continue or any other key to abort
```

と言われるので, リターンキー[Entern]を押します.

```
Password:
```
パスワードを要求されるため, PCを起動するときのパスワードを入力します.

```
==> This script will install:
 /usr/local/bin/brew
 /usr/local/share/doc/homebrew
 /usr/local/share/man/man1/brew.1
...
 (中略)
...
==> Installation successful!
==> Homebrew has enabled anonymous aggregate formulae and cask analytics.
Read the analytics documentation (and how to opt-out) here:
https://docs.brew.sh/Analytics
==> Homebrew is run entirely by unpaid volunteers. Please consider donating:
https://github.com/Homebrew/brew#donations
==> Next steps:
- Run `brew help` to get started
- Further documentation:
https://docs.brew.sh
```
と表示されたら, インストール完了です!
Homebrew 自体は, `/usr/local/Homebrew`にインストールされます.
