# Bambu Lab A1 mini 学校LANモード運用ガイド

このリポジトリは、学校・FabLab向けに Bambu Lab A1 / A1 mini のLANモード運用を整理する公開用GitHub Pagesサイトです。

## 公開記事

- `docs/index.md`
  - 学校でBambu Lab A1 miniを複数台運用するための導入設計―LANモードと多数ユーザー設定の初年度記録
- `docs/classroom-practice-2025.md`
  - 中学校3年生160人規模で卒業記念プレートを3Dプリントした初年度実践
- `docs/3d-modeling-environment-selection.md`
  - 学校の3Dモデリング環境をどう選ぶか―作成・保存・確認・救出・卒業後まで見据える

## GitHub Pages

GitHub Pagesの公開元は、`main` ブランチの `/docs` を想定しています。リポジトリ設定で Pages の Source を `Deploy from a branch`、Branch を `main`、Folder を `/docs` に設定してください。

## 公開情報の方針

このリポジトリには、学校固有の設定、内部マニュアル、個人情報、ネットワーク構成の具体値を含めません。ネットワークは模式的・一般的な表現に限定します。

## 検査

文書変更時は、少なくとも次を実行します。

```bash
git diff --check
python scripts/check_public_content.py
python scripts/check_internal_links.py
```

## ライセンス

Copyright (c) 2026 Yuichiroh Kobayashi。記事・文書は、特記がない限り [CC BY-SA 4.0](LICENSE) で公開します。第三者資料の長文転載は行わず、公式資料は要約と参考リンクで示します。商標、製品名、公式資料、その他の第三者資料は、各権利者が明示しない限りCC BY-SA 4.0の対象外です。
