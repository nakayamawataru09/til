## そもそもVertex AI Experimentsとは

> さまざまなモデル アーキテクチャ、ハイパーパラメータ、トレーニング環境を追跡および分析し、テストの実行の手順、入力、出力を追跡する際に役立つツール
公式では上記らしい(https://cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments?hl=ja)
databricksのmlflowみたいなものだと思う。extureだとgcpが多いし、自分も使い慣れている(課金体系とかGCS,BQとかが何を表すか知っている)という点でいいなと思った。
MLFLOWとの差としてはGCPのサービスとのシームレスな連携ができる点
Vertex AI Experimentsの機能の一つで、機械学習の実験パラメータ、スコア等を記録し、GCPのコンソールから確認できる。