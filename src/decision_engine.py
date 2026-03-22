# src/decision_engine.py

def decide(state, intensity, stress, energy, time_of_day):

    # High stress → immediate calming
    if stress >= 8:
        return "box_breathing", "now"

    # Low energy → rest
    if energy <= 3:
        return "rest", "within_15_min"

    # High energy + low stress → productive work
    if energy >= 7 and stress <= 4:
        return "deep_work", "now"

    # Medium stress → grounding
    if 5 <= stress < 8:
        return "grounding", "within_15_min"

    # Late night logic
    if time_of_day in ["night", "late_night"]:
        return "light_planning", "tomorrow_morning"

    return "light_planning", "later_today"