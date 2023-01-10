def parseTestContainerUrlForPsycopg(url: str) -> str:
    return url.split("+")[1].replace("psycopg2", "postgresql")
