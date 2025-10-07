import openai
import os
from dotenv import load_dotenv
import json
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_proposals_from_text(user_text: str):
    """
    ユーザーのテキストに基づいて、OpenAI APIに問い合わせ、
    AIソリューションの提案をJSON形式で生成する関数。
    """
    # 機能仕様書に記載のプロンプト例をテンプレート化
    prompt_template = """
    以下のテキストは、あるビジネス会議の内容です。
    この内容から主要な課題を [What], [Why], [Who]の観点で抽出し、
    その課題解決に有効なAI技術、具体的なSaaS ツール名、そして導
    入のヒントをセットにして3つ提案してください。
    出力は以下のJSON形式フォーマットに厳密に従ってください。
    {
      "proposals": [
        {
          "card_title": "（提案の核となるキーワード）",
          "proposal_category": "（業務効率化、新規事業アイデアなど）",
          "recommended_tool": "（具体的なツール名）",
          "introduction_hint": "（導入を促す一言）"
        }
      ]
    }
    --- テキスト ---
    {user_text}
    ---
    """
    
    prompt = prompt_template.format(user_text=user_text)

    try:
        response = openai.chat.completions.create(
            model="gpt-4-turbo",  # 最新のモデルを推奨
            messages=[
                {"role": "system", "content": "あなたは優秀なビジネスコンサルタントです。"},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"} # JSONモードを有効化
        )
        
        # APIからのレスポンス(JSON文字列)をPythonの辞書型に変換
        result_json = json.loads(response.choices[0].message.content)
        return result_json

    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        # エラーが発生した場合はNoneを返すか、例外を投げる
        return None