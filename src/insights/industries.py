from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    list_of_industry = set()
    for row in data:
        if row["industry"]:
            list_of_industry.add(row["industry"])
    return list_of_industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job["industry"] == industry]
    
