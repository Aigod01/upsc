async def final_score(c: int, d: int, l: int) -> dict:
    avg = (c + d + l) / 3
    if avg >= 7:
        return {"score": avg, "status": "pass"}
    else:
        return {"score": avg, "status": "fail", "message": "Your score is below average. Please review the suggestions."}
