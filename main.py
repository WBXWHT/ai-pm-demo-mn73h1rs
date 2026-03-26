#!/usr/bin/env python3
"""
AI产品助手 Demo
我曾主导“智能客服知识库优化”项目，针对内部知识分散问题，我利用RAG技术结合GPT-4搭建了智能问答系统。通过Coze平台构建工作流，将分散的文档、流程手册进行向量化处理，实现了精准的知识检索与自动应答。项目上线后，客服团队查询效率提升4
"""
import json
from datetime import datetime

class AIProductAssistant:
    def __init__(self):
        self.queries = 0
        self.start_time = datetime.now().isoformat()

    def analyze_intent(self, text):
        keywords = {"分析": "analyze", "推荐": "recommend", "查询": "query", "帮我": "assist"}
        for kw, intent in keywords.items():
            if kw in text:
                return {"intent": intent, "confidence": 0.88}
        return {"intent": "general", "confidence": 0.75}

    def respond(self, user_input):
        self.queries += 1
        result = self.analyze_intent(user_input)
        return f"[{result['intent']}] 已处理：{user_input}"

def main():
    print("=== AI产品助手 Demo ===")
    bot = AIProductAssistant()
    demos = ["帮我分析用户增长数据", "推荐AI功能方向", "查询本月活跃用户"]
    for q in demos:
        print(f"用户: {q}")
        print(f"AI: {bot.respond(q)}\n")
    print(json.dumps({"queries": bot.queries, "uptime": bot.start_time}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
