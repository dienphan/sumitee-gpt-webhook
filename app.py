from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    user_message = data.get("text", "")

    reply = gpt_reply(user_message)

    return jsonify({
        "messages": [
            {"text": reply}
        ]
    })

def gpt_reply(text):
    prompt = f"Bạn là nhân viên bán áo thun của thương hiệu Sumitee. Trả lời ngắn gọn, thân thiện, chuyên nghiệp cho khách sau đây: '{text}'"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    app.run(port=5000)
