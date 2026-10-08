from smolagents import CodeAgent, InferenceClientModel, tool

PARTY_FAQ = {
    "와이파이": "네트워크명 WayneGuest, 비밀번호 batcave2026",
    "주차": "정문 왼쪽 잔디밭에 발레파킹",
    "드레스코드": "블랙 타이",
    # 항목 3개 이상 더 추가해보세요
}

@tool
def party_faq(question: str) -> str:
    """
    (여기 설명을 쓰는 게 이번 과제의 핵심입니다)

    Args:
        question: (이 값에 무엇을 넣어야 하는지 설명)
    """
    # 질문에 포함된 키워드로 PARTY_FAQ에서 답을 찾아 반환
    # 못 찾으면 어떤 메시지를 돌려줄지도 직접 정해보세요
    pass

agent = CodeAgent(tools=[party_faq], model=InferenceClientModel())
agent.run("와이파이 비밀번호가 뭐예요?")