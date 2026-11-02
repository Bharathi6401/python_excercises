def add(a, b):
    return a + b

def check_employee(employee):
    experience = employee.get("experience")

    if experience is None:
        return "Experience missing"

    try:
        experience = int(experience)
    except (ValueError, TypeError):
        return "Invalid experience"

    if experience < 0:
        return "Invalid experience"
    elif experience >= 2:
        return "Eligible for experienced role"
    else:
        return "Junior level"