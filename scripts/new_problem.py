import os
import sys

if len(sys.argv) != 3:
    print("Usage: python new_problem.py <id> <title>")
    sys.exit(1)

# 将输入的题号转成 5 位字符串
id_input = int(sys.argv[1])
id_str = f"{id_input:05d}"  # 自动补零, 2 -> 00002
title = sys.argv[2].lower().replace(" ", "_")
func_name = f"p{id_str}_{title}"

problems_dir = "src/algo/leetcode"
tests_dir = "tests/leetcode"
os.makedirs(problems_dir, exist_ok=True)
os.makedirs(tests_dir, exist_ok=True)

# Problem file
problem_file = os.path.join(problems_dir, f"{func_name}.py")
if not os.path.exists(problem_file):
    with open(problem_file, "w") as f:
        f.write(f"""class Solution:
    def {title}(*args, **kwargs) -> None:
        # TODO: implement
        pass
""")

# Test file
test_file = os.path.join(tests_dir, f"test_{func_name}.py")
if not os.path.exists(test_file):
    with open(test_file, "w") as f:
        f.write(f"""from algo.leetcode.{func_name} import Solution

def test_{title}():
    # TODO: add test cases
    pass
""")

print(f"✅ Created problem {func_name}")
