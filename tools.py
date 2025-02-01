from langchain_core.tools import tool
from typing import Dict

student_marks = [{'id': '0001', 'mark':520}, {'id': '0002', 'mark':540},]

@tool
def get_mark(id: str) -> Dict:
    """
    Get mark for students.

    Args:
        id (str): ID of the student

    Return:
        str: The mark that matches with the student ID
    """

    for student in student_marks:
        if student['id'] == id:
            return student
    return "Your ID not found in the database. Who are you?"
