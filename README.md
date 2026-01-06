# 🏥 Medical-RAG
> 🚧 **尚在開發中（Work in Progress）**
Medical-RAG 是一個以 **本地大型語言模型（LLM）** 為核心的  
**醫療問答檢索增強生成（RAG）系統**，  
結合 **LangChain + Chroma + FastAPI + Streamlit**，  
實現「**先檢索，再生成**」的醫療問答流程。
---
## 🔧 目前已完成
1. **本地模型部署**
   - 使用本地 LLM（GGUF）
   - 無需外部 API，即可完成推理
   - 能夠根據檢索結果生成回答（RAG）
2. **完整 RAG Pipeline**
   - CSV 文件載入（MedQuad）
   - 文件切分
   - 向量化（Embedding）
   - Chroma 向量資料庫
   - Retriever + LLM 問答整合
3. **API 與 UI 整合**
   - 使用 **FastAPI** 提供對外 API（`/ask`）
   - 使用 **Streamlit** 作為前端 UI
   - 使用者可透過 UI 輸入問題並獲得回覆
---
## 🧩 系統架構
UI(Stremlitt) -> API(FastAPI) -> Retriever(Chroma) -> Answer
---
## 🚀 即將開發
1. **UI 改善**
   - 支援檔案上傳（PDF / CSV）
   - 問答歷史紀錄
   - 更友善的互動介面
2. **功能擴充（規劃中）**
   - 多文件來源 RAG
   - Prompt 管理與版本控制
   - 回答來源文件顯示（Source Citation）
---
## 🛠️ 技術棧
- Python
- LangChain
- Chroma
- HuggingFace Embeddings
- FastAPI
- Streamlit
- Local LLM (GGUF)
---
## 📌 備註
- 向量資料庫與模型檔案未納入版本控制
- 本專案為學習與實作用途，持續優化中
