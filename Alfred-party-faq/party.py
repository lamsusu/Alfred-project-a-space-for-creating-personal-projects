from smolagents import CodeAgent, InferenceClientModel, tool

# 딕셔너리 
PARTY_FAQ = {
    "와이파이": "네트워크명 WayneGuest, 비밀번호 batcave2026",
    "주차": "정문 왼쪽 잔디밭에 발레파킹",
    "드레스코드": "블랙 타이",
    # 항목 3개 이상 더 추가해보세요
    "준비물": "파티에서 먹을 수 있는 음식, 음료",
    "파티 시작시간": "오후 6시 부터 시작",
    "파티 끝나는 시간":"오후 10시에 끝",
    "알레르기":"음식과 음료마다 사용된 재료를 메모로 적어 그릇에 붙여둘 예정입니다.",
}

@tool
def party_faq(question: str) -> str:
    """
        (docstring은 그대로)
    Args:
        question:
    """
    # 질문에 포함된 키워드로 PARTY_FAQ에서 답을 찾아 반환
    # 못 찾으면 어떤 메시지를 돌려줄지도 직접 정해보세요
    for key, answer in PARTY_FAQ.items():
        if key in question:
            return f"[{key}] {answer}"
    return "FAQ에 없는 정보입니다. 추측하지 말고 손님에게 확인 후 알려드리겠다고 안내하세요."
    pass

agent = CodeAgent(tools=[party_faq], model=InferenceClientModel())
agent.run("와이파이 비밀번호가 뭐예요?")