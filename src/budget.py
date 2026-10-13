def personnel_budget(headcount, avg_salary, benefits_rate=0.3, tax_rate=0.3):
    base = headcount * avg_salary
    with_benefits = base * (1 + benefits_rate)
    total = with_benefits * (1 + tax_rate)
    return {
        "base_salaries": base,
        "with_benefits": with_benefits,
        "total_with_tax": total,
    }

def recruitment_cost(hires, cost_per_hire=15000):
    return hires * cost_per_hire

def onboarding_cost(hires, onboarding_cost=5000):
    return hires * onboarding_cost
