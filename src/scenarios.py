def scenario(base_headcount, growth_rate, months=12):
    hc = base_headcount
    for _ in range(months):
        hc *= (1 + growth_rate)
    return int(hc)

def build_scenarios(base_headcount):
    return {
        "conservative": scenario(base_headcount, 0.005),
        "base": scenario(base_headcount, 0.015),
        "aggressive": scenario(base_headcount, 0.03),
    }
