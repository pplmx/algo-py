import argparse
import re
from pathlib import Path

# --- Templates ---

SOLUTION_TEMPLATE = """class Solution:
    def {method_name}(self, s: str) -> str:
        # TODO: Implement the solution
        print(s)
        return ""
"""

TEST_TEMPLATE = """import pytest

from algo.leetcode.{module_name} import Solution


class TestSolution:
    @pytest.mark.parametrize(
        ("s", "expected"),
        [
            ("test_case_1", "expected_1"),
            ("test_case_2", "expected_2"),
        ],
    )
    def test_solution(self, s, expected):
        solution = Solution()
        assert solution.{method_name}(s) == expected
"""


def main():
    parser = argparse.ArgumentParser(description="Create a new LeetCode problem file and its test file.")
    parser.add_argument("id", type=int, help="The problem ID (e.g., 1).")
    parser.add_argument(
        "title", type=str, help="The problem title in CamelCase or snake_case (e.g., TwoSum or two_sum)."
    )
    args = parser.parse_args()

    problem_id_str = f"{args.id:05d}"

    # --- Normalize title to snake_case --- #
    # 1. Replace spaces and hyphens with underscores
    temp_title = args.title.replace(" ", "_").replace("-", "_")
    # 2. Convert CamelCase to snake_case
    temp_title = re.sub(r"(?!^)(?=[A-Z])", "_", temp_title)
    # 3. Lowercase the whole string and clean up any double underscores
    snake_case_title = re.sub(r"__+", "_", temp_title).lower()
    module_name = f"p{problem_id_str}_{snake_case_title}"

    # Define paths using pathlib
    project_root = Path(__file__).parent.parent
    problem_file_path = project_root / "src" / "algo" / "leetcode" / f"{module_name}.py"
    test_file_path = project_root / "tests" / "leetcode" / f"test_{module_name}.py"

    # Create problem file
    if not problem_file_path.exists():
        problem_file_path.parent.mkdir(parents=True, exist_ok=True)
        content = SOLUTION_TEMPLATE.format(method_name=snake_case_title)
        problem_file_path.write_text(content)
        print(f"✅ Created solution file: {problem_file_path.relative_to(project_root)}")
    else:
        print(f"⚠️ Solution file already exists: {problem_file_path.relative_to(project_root)}")

    # Create test file
    if not test_file_path.exists():
        test_file_path.parent.mkdir(parents=True, exist_ok=True)
        content = TEST_TEMPLATE.format(module_name=module_name, method_name=snake_case_title)
        test_file_path.write_text(content)
        print(f"✅ Created test file: {test_file_path.relative_to(project_root)}")
    else:
        print(f"⚠️ Test file already exists: {test_file_path.relative_to(project_root)}")


if __name__ == "__main__":
    main()
