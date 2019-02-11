# ykmc/atcoder

atcoderのコンテスト提出・過去問提出を管理するためのリポジトリ。2019年は2019ACを目標に。

## 言語とバージョン

- Python
  - 3.4.3
- Rust
  - 1.15.1


## ディレクトリ構造と命名規則

### ディレクトリ構造

```
 yyyy / mmdd_contestxxx / problem_yyyymmdd.ext
```

- yyyy
  - コンテスト実施年
- mmdd
  - コンテスト実施月日
- contestxxx
  - コンテスト名の省略表記 + コンテスト番号
- problem
  - 問題番号(A-Z)
- yyyymmdd
  - submit年月日
- ext
  - ファイル拡張子

### 命名規則

#### コンテスト名を利用

| コンテスト略称 | コンテスト正式名称           | 主催     |
|----------|------------------------------------|----------|
| CF       | CODE FESTIVAL                      | Recruit  |
| CTF      | CODE THANKS FESTIVAL               | Recruit  |
| T1PC     | Tenka1 Programmer Contest          | KLab     |
| DDCC     | DISCO presents ディスカバリーチャンネル コードコンテスト         | DISCO |
| DDCP     | DISCO presents ディスカバリーチャンネル プログラミングコンテスト | DISCO |

#### 企業名を利用

| コンテスト略称 | コンテスト正式名称 | 主催 |
|----------|--------------------------------|----------|
| AISing   | AISing Programming Contest     | AISing | 
| BitFlyer | codeFlyer                      | bitFlyer |
| CADDi    | CADDi                          | CADDi   |
| Yahoo    | みんなのプロコン               | Yahoo!    |
| Keyence  | KEYENCE Programming Contest    | キーエンス |
| Nikkei   | 全国統一プログラミング王決定戦 | 日経新聞 |
