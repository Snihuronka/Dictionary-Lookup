# Dictionary Lookup（辞書検索）

[English](README.md) | [日本語](README.ja.md)

複数のオンライン辞書で英単語を一度に検索できる小さな Tkinter GUI です。単語を入力し、検索したい辞書を選ぶと、選択した各エントリが Web ブラウザで開きます。

## 必要環境

- Python 3（標準ライブラリの tkinter モジュールを含む）
- Web ブラウザ
- Linux の場合: 利用可能なときは xdg-open を使用します（無い場合は webbrowser モジュールにフォールバックします）

多くの Linux ディストリビューションでは、tkinter は Python とは別パッケージで提供されます。必要に応じて、パッケージマネージャでインストールしてください。例:

- Debian/Ubuntu: `sudo apt install python3-tk`
- Fedora/RHEL: `sudo dnf install python3-tkinter`
- Arch: `sudo pacman -S tk`

## 使い方

スクリプトを直接実行します:

```sh
python3 Dicts.py
```

または、実行権限が付与されている場合:

```sh
./Dicts.py
```

その後:

1. 「Word:」フィールドに単語を入力します。
2. 検索したい辞書にチェックを入れます（既定ではすべて選択されています）。「Select all」/「Clear」で素早く切り替えられます。
3. 「Look up」をクリックします（単語フィールドで Enter キーを押しても実行できます）。

選択した各辞書が、単語が入力された状態で新しいブラウザタブに開きます。

## 対応辞書

- Oxford English Dictionary
- Cambridge
- Collins
- Merriam-Webster
- Britannica

## カスタマイズ

辞書を追加・削除・変更するには、`Dicts.py` の先頭付近にある `DICTIONARIES` 辞書（dict）を編集します。各エントリは表示名を URL テンプレートに対応付けており、`{word}` が URL エンコードされた検索語に置き換えられます。例:

```python
"Wiktionary": "https://en.wiktionary.org/wiki/{word}",
```

## 備考

- 検索語は URL エンコードされるため、複数語のフレーズや特殊文字も安全に扱えます。
- Linux では、URL オープナーからの stderr を抑制し、不要な出力（例: KIO の警告）を防いでいます。
