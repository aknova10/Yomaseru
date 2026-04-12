from fastmcp import FastMCP
from logging import Logger
mcp = FastMCP("Demo 🚀")

@mcp.tool
def list_vocabulary():
    logger = Logger(name="vocab logger")
    logger.info("Retrieving vocab list...")
    # print("Retrieving vocab list...")
    vocab = [
        {"word": "案内", "reading": "あんない", "meaning": "guidance / information"},
        {"word": "腕", "reading": "うで", "meaning": "arm / skill"},
        {"word": "影響", "reading": "えいきょう", "meaning": "influence / effect"},
        {"word": "表", "reading": "おもて", "meaning": "front / surface"},
        {"word": "会話", "reading": "かいわ", "meaning": "conversation"},
        {"word": "確認", "reading": "かくにん", "meaning": "confirmation"},
        {"word": "感情", "reading": "かんじょう", "meaning": "emotion"},
        {"word": "環境", "reading": "かんきょう", "meaning": "environment"},
        {"word": "記録", "reading": "きろく", "meaning": "record / documentation"},
        {"word": "苦労", "reading": "くろう", "meaning": "hardship / trouble"},
        {"word": "原因", "reading": "げんいん", "meaning": "cause / origin"},
        {"word": "効果", "reading": "こうか", "meaning": "effect / result"},
        {"word": "交流", "reading": "こうりゅう", "meaning": "exchange (cultural, social)"},
        {"word": "作業", "reading": "さぎょう", "meaning": "work / operation"},
        {"word": "参加", "reading": "さんか", "meaning": "participation"},
        {"word": "支給", "reading": "しきゅう", "meaning": "provision / supply"},
        {"word": "自然", "reading": "しぜん", "meaning": "nature / natural"},
        {"word": "実験", "reading": "じっけん", "meaning": "experiment"},
        {"word": "状態", "reading": "じょうたい", "meaning": "condition / state"},
        {"word": "責任", "reading": "せきにん", "meaning": "responsibility"},
        {"word": "設備", "reading": "せつび", "meaning": "equipment / facilities"},
        {"word": "速度", "reading": "そくど", "meaning": "speed"},
        {"word": "対象", "reading": "たいしょう", "meaning": "target / subject"},
        {"word": "特徴", "reading": "とくちょう", "meaning": "feature / characteristic"},
        {"word": "内容", "reading": "ないよう", "meaning": "content / details"},
        {"word": "判断", "reading": "はんだん", "meaning": "judgment / decision"},
        {"word": "比較", "reading": "ひかく", "meaning": "comparison"},
        {"word": "表現", "reading": "ひょうげん", "meaning": "expression"},
        {"word": "目的", "reading": "もくてき", "meaning": "purpose / goal"},
        {"word": "要求", "reading": "ようきゅう", "meaning": "demand / requirement"}
    ]
    return vocab

if __name__ == "__main__":
    mcp.run()