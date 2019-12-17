# Zsh のインストール

Homebrew を用いてインストールを行います.
```
$ brew install zsh
```
zsh の補完機能を導入するため `zsh-completion`をインストールしておきます.
```
$ brew install zsh-completion
```

## ログインシェルを変更する

### /etc/shellsの編集

`/etc/shells`には, 使用可能なシェルの一覧が設定されています.
```
$ sudo vi /etc/shells
```
を実行し, `/etc/shells`を開いてみると, 以下のようになっています.

```
# List of acceptable shells for chpass(1).
# Ftpd will not allow users to connect who are not using
# one of these shells.

/bin/bash
/bin/csh
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh
```
ここで Homebrew でいれた Zsh を登録します. Zsh のインストール先は, 
```
$ which zsh
```
で知ることができます.  
ここで取得したパスを, 行の最後に追加します. 標準では, 
```
/usr/local/bin/zsh
```
になっています.

### chsh実行

chshを実行して, ログインシェルを変更します.
```
chsh -s /usr/local/bin/zsh
```

## Bash から Zsh へお引越し

bash の `.bash_profile` を, zsh の `.zprofile` にお引越し, `.bashrc` を `.zshrc` にお引越しします.

```
$ cat .bash_profile >> .zprofile
$ cat .bashrc >> .zshrc
```
ちなみに, macOS Catalina からは, ログインシェルのデフォルトが bash から zsh になるようです.
