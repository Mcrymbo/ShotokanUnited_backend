from .knowledge_base.karate_knowledge import TECHNIQUES, KATA, ORGANIZATION_INFO

def check_knowledge_base(query: str) -> str | None:
    query = query.lower()
    
    # Technique lookup
    for tech, data in TECHNIQUES.items():
        if tech.replace("_", " ") in query:
            response = f"{tech.replace('_', ' ').title()}:\n"
            response += f"- Purpose: {data['description']}\n"
            response += f"- Key Points: {', '.join(data['key_points'])}\n"
            response += f"- Avoid: {data['common_mistakes'][0]}"
            return response
    
    # Kata lookup
    for kata, data in KATA.items():
        if kata.replace("_", " ") in query:
            return f"{kata.replace('_', ' ').title()} has {data['movements']} movements focusing on {data['purpose']}"
    
    # Organization info
    if "schedule" in query:
        loc = next((loc for loc in ORGANIZATION_INFO['schedule'] if loc in query), None)
        if loc: return f"{loc.title()} schedule: {ORGANIZATION_INFO['schedule'][loc]}"
    
    return None