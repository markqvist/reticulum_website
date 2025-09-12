# はじめに
Reticulum Network Stackを始める最良の方法は、行いたいことによって異なります。詳細や例については、[Getting Started Fast](manual/gettingstartedfast.html)セクションを[Reticulum Manual](manual/index.html)で確認してください。

## コミュニティとサポート
問題が発生したり、何かがうまく動作しない場合は、助けを求めるための優れた場所がいくつかあります：

- GitHubの[discussion forum](https://github.com/markqvist/Reticulum/discussions)
- [Reticulum Matrix Channel](https://matrix.to/#/#reticulum:matrix.org)の`#reticulum:matrix.org`
- [Reticulum subreddit](https://reddit.com/r/reticulum)

## インストール
システムにReticulumおよび関連ユーティリティをインストールする最も簡単な方法は、pipを使用することです：

```bash
pip install rns
```

その後、Reticulumを使用するプログラムを開始するか、[rnsdユーティリティ](manual/using.html#the-rnsd-utility)を使用してReticulumをシステムサービスとして起動できます。

システムに`pip`が利用できない場合は、まずOS用の`python3`および`python3-pip`パッケージをインストールしてください。

最初に起動すると、Reticulumはデフォルトの設定ファイルを作成し、ローカルに到達可能な他のReticulumピアとの基本的な接続性を提供します。これらのローカルピアがTransport Instancesであれば、これらはより広範なネットワークに接続できるかもしれません。デフォルトの設定ファイルにはいくつかの例と、より複雑な構成を作成するための参照が含まれています。

パケットラジオやLoRa、シリアルポート、UDPおよびTCPインターフェースを使用して高速なIPリンクおよびインターネット経由で通信を拡張する方法についての詳細な例については、[Reticulum Manual](manual/index.html)の[Supported Interfaces](manual/interfaces.html)セクションを参照してください。

## 含まれるユーティリティ
Reticulumには、ネットワークを管理し、ステータスや情報を表示し、その他のタスクを行うためのさまざまな便利なユーティリティが含まれています。これらのプログラムについて詳しくは、[Reticulum Manual](manual/index.html)の[Included Utility Programs](manual/using.html#included-utility-programs)セクションを読んでください。

- 常に利用可能なサービスとしてReticulumを実行するためのシステムデーモン`rnsd`
- インターフェイスのステータス情報を表示する`rnstatus`と呼ばれるユーティリティ
- パステーブルを表示および変更するためのパス検索および管理ツール`rnpath`
- 接続先への接続を確認する診断ツール`rnprobe`
- ファイルをリモートシステムに簡単にコピーできるようにする単純なファイル転送プログラム`rncp`
- リモートシステムからコマンドやプログラムを実行し、出力を取得する`rnx`

これらのツール、`rnx`および`rncp`を含むすべてのツールは、LoRaやパケットラジオなどの非常に低帯域幅のリンクでも信頼性があり、うまく動作します。

## Reticulumを使用したプログラム
Reticulumの機能についてすぐに理解したい場合は、以下のリソースをご覧ください。

- オフグリッド、暗号化された、強固なメッシュ通信プラットフォームについては、[Nomad Network](https://github.com/markqvist/NomadNet) を参照してください。
- Android、Linux、およびmacOSアプリ[Sideband](https://github.com/markqvist/sideband)は、グラフィカルなインターフェースを備えており、使いやすさに焦点を当てています。
- [LXMF](https://github.com/markqvist/lxmf)は、Reticulum上に構築された分散型で遅延および障害対応のメッセージ転送プロトコルです。

## 依存関係
デフォルトの`rns`パッケージのインストールには、以下にリストされた依存関係が必要です。ほとんどのシステムとディストリビューションはこれらの依存関係のために既に利用可能なパッケージを持っており、`pip`で`rns`パッケージをインストールすると、これらもダウンロードおよびインストールされます。

- [PyCA/cryptography](https://github.com/pyca/cryptography)
- [netifaces](https://github.com/al45tair/netifaces)
- [pyserial](https://github.com/pyserial/pyserial)

より一般的でないシステムや一部の稀なケースでは、上記のモジュールの1つ以上をインストールまたはコンパイルすることができないかもしれません。そのような状況では、外部依存関係がインストールに必要ない`rnspure`パッケージを代わりに使用できます。`rns`と`rnspure`パッケージの内容は*同一*です。唯一の違いは、`rnspure`パッケージがインストールに必要な依存関係をリストしていないことです。

どのようにReticulumがインストールおよび起動されても、外部依存関係は*必要*かつ*利用可能*な場合のみ読み込まれます。例えば、[pyserial](https://github.com/pyserial/pyserial)をサポートしないシステムでReticulumを使用したい場合、`rnspure`パッケージを使用しても問題ありませんが、Reticulumはシリアルベースのインターフェースを使用できません。それ以外の利用可能なモジュールは、必要に応じて引き続き読み込まれます。

**注意！** [PyCA/cryptography](https://github.com/pyca/cryptography)をサポートしないシステムで`rnspure`パッケージを使用してReticulumを実行する場合は、このサイトの[暗号プリミティブ](crypto.html)セクションを読み、理解することが重要です。

## パフォーマンス
Reticulumは*非常に*広範なパフォーマンスエンベロープを対象としていますが、低帯域幅のメディアに対する機能性とパフォーマンスを優先します。目標は、通常のハードウェアで250ビット/秒から1ギガビット/秒までの動的なパフォーマンス範囲を提供することです。

現在、使用可能なパフォーマンス範囲は約150ビット/秒から40メガビット/秒であり、それ以上の物理メディアは飽和していません。現在のレベルを超えるパフォーマンスは将来のアップグレードのために意図されていますが、ワイヤフォーマットとAPIが確定するまで高い優先度は付けられていません。

<p align="right"><a href="hardware_jp.html">次のトピック：サポートされているハードウェア</a></p>
