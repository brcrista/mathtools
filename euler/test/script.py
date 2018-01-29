"""
Automatically regression test all solved problems.
Solved problems should have a script called 'test.py' that runs tests for that problem,
at minimum verifying the correct answer.
"""

import os

def main():
    os.chdir('../problems') # TODO use absolute path with $PROJECT_ROOT
    problems_dir = os.getcwd()

    for problem in os.listdir():
        os.chdir(problem)
        print(f'Testing Problem {problem} ...')
        if 'test.py' in os.listdir():
            os.system('python test.py')
        print()
        os.chdir(problems_dir)

if __name__ == '__main__':
    main()
