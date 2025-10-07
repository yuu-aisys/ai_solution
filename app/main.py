from fastapi import FastAPI

# FastAPIのインスタンスを作成
app = FastAPI()

# ルートURL ("/") へのGETリクエストに対する処理
@app.get("/")
def read_root():
    return {"message": "AI Solution Proposal API is running!"}

# --- ここから追記 ---
# 今後の機能（ルーター）をここに追加していく
# from .routers import proposal
# app.include_router(proposal.router)