# YouTube 喜歡影片清理

只保留「喜歡的影片」清單中**最近 N 部**（預設 9 部，對應你截圖中的那九部），其餘全部取消喜歡。

> 此腳本須在**你自己的電腦**執行（需要瀏覽器完成 Google 登入授權）。Cloud Agent 環境無法代你登入 YouTube。

## 安全設計

- **預設 dry-run**：只列出將保留／將取消的影片，不會改動帳號。
- 真正取消喜歡必須加上 `--execute`，並輸入 `YES` 確認（或加 `--yes` 略過確認）。
- OAuth 憑證與 token **不進 Git**（見倉庫 `.gitignore`）。

## 事前準備（一次即可）

1. 開啟 [Google Cloud Console](https://console.cloud.google.com/)
2. 建立（或選用）專案 → 啟用 **YouTube Data API v3**
3. **API 和服務 → 憑證 → 建立憑證 → OAuth 用戶端 ID**
   - 應用程式類型選 **電腦應用程式（Desktop）**
   - 若尚未設定 OAuth 同意畫面：選外部／測試，並把你的 Google 帳號加進測試使用者
4. 下載 JSON，重新命名為 `client_secret.json`，放到本目錄：

```text
D:\文件\260703_Al_Agent\260712_YT_UnLike\client_secret.json
```

5. 安裝相依套件：

```bash
cd /d D:\文件\260703_Al_Agent\260712_YT_UnLike
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 使用方式

### 1. 先預覽（建議一定要先做）

```bash
python cleanup_liked.py --keep 9
```

首次執行會開啟瀏覽器，請登入**你的 YouTube 帳號**並允許存取。授權後會產生 `token.json`。

請核對輸出中「將保留」的前 9 部，是否就是截圖那九部。

### 2. 確認無誤後真正執行

```bash
python cleanup_liked.py --keep 9 --execute
```

出現提示時輸入 `YES`。

略過確認：

```bash
python cleanup_liked.py --keep 9 --execute --yes
```

### 3. 喜歡數量很多時（API 日配額）

`videos.rate`（取消喜歡）每次約消耗 50 quota。預設專案日額約 10,000，大約一天最多取消 ~200 部。

可分批：

```bash
python cleanup_liked.py --keep 9 --execute --yes --max-unlike 180
```

隔天再跑同一指令即可；已取消喜歡的影片不會再出現在清單中。

## 常用參數

| 參數 | 說明 |
|------|------|
| `--keep N` | 保留最近 N 部（預設 9） |
| `--execute` | 真正取消喜歡 |
| `--yes` | 略過互動確認 |
| `--max-unlike N` | 本次最多取消 N 部 |
| `--credentials PATH` | `client_secret.json` 路徑 |
| `--token PATH` | token 快取路徑 |
| `--report PATH` | 執行報告 JSON |

## 輸出檔（本機，勿提交）

- `client_secret.json` — Google OAuth 用戶端
- `token.json` — 登入授權快取
- `last_run_report.json` — 最近一次預覽／執行結果

## 注意

- 「最近」依 YouTube「喜歡的影片」播放清單順序（通常最新喜歡在最前）。
- 取消喜歡無法從本腳本一鍵還原；請務必先 dry-run。
- 若 OAuth 同意畫面仍在測試模式，重新授權可能需要把帳號加進測試使用者。
