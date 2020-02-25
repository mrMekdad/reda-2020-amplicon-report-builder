"""Core workflow for Amplicon Report Builder by Red@."""

PROJECT_NAME = "Amplicon Report Builder"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
