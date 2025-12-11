# modules/ai_summ.py
from transformers import pipeline

# 모델 로딩은 시간이 걸리므로 모듈이 import 될 때 전역 변수로 한 번만 로드
print(">> [System] AI 모델을 메모리에 올리는 중... (10~20초 소요)")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    """
    긴 영어 텍스트를 받아 요약문을 반환
    """
    if not text or len(text) < 50:
        return "요약할 본문 내용이 너무 짧습니다."

    try:
        # 텍스트가 너무 길면 모델 제한(1024 토큰)에 걸리므로 앞부분만 자름
        input_text = text[:3000]
        
        # AI 요약 수행
        summary_result = summarizer(input_text, max_length=100, min_length=30, do_sample=False)
        return summary_result[0]['summary_text']
        
    except Exception as e:
        return f"AI 요약 중 오류 발생: {e}"

if __name__ == "__main__":
    # 테스트
    test_text = "Python is an interpreted, high-level and general-purpose programming language. " * 10
    print(summarize_text(test_text))