from typing import Union, List, Dict
from src.insights.jobs import read


def validate_salary_parameter(job: Dict) -> None:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Salary is not valid")

    min_salary, max_salary = job["min_salary"], job["max_salary"]

    if (not type(min_salary) == int and not str(min_salary).isnumeric()) or (
        not type(max_salary) == int and not str(max_salary).isnumeric()
    ):
        raise ValueError("Salary is not valid")

    if int(min_salary) > int(max_salary):
        raise ValueError("min_salary must be less than max_salary")


def validate_job_salary_parameter(salary: Dict) -> None:
    if type(salary) is not int and type(salary) is not str:
        raise ValueError("Salary is not valid")
    if type(salary) is str and not salary.isnumeric():
        raise ValueError("Salary is not valid")


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary = []
    for row in data:
        if row["max_salary"] and row["max_salary"].isdigit():
            max_salary.append(int(row["max_salary"]))
    return max(max_salary)


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salary = []
    for row in data:
        if row["min_salary"] and row["min_salary"].isdigit():
            min_salary.append(int(row["min_salary"]))
    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    validate_salary_parameter(job)
    validate_job_salary_parameter(salary)
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError


