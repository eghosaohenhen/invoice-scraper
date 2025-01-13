import re

def regex_tester(regex, testcases):
    """
    Test a regex against a list of testcases and print the results.
    """
    for testcase, expected in testcases:
        match = re.search(regex, testcase)
        print(f"Testing {testcase} against {regex}")
        if match and expected:
            print(f"Matched: {match.group(0)} ... OK")
        elif not match and not expected:
            print("No match ... OK")
        else:
            print("Mismatch ... FAIL")

# Test the regex against some testcases
cur_regex = r'\(?(\d{3})\)?-?(\d{3})(-?)(\d{4})'

new_regex = r'\(?(\d{3})\)?(-|\s|\.)?(\d{3})(-|\s|\.)?(\d{4})'
testcases = [
    ("123-456-7890", True),
    ("1234567890", True),
    ("(123)456-7890", True),
    ("123-4567890", True),
    ("123456-7890", True),
    ("123-456-789", False),
    ("123 456 7890", True),
    ("123.456.7890", True),
    ("123 456-7890", True),
    ("(123) 456-7890", True)
    
    
]
if __name__ == '__main__':
    print("Testing current regex")
    regex_tester(cur_regex, testcases)
    print("Testing new regex") 
    regex_tester(new_regex, testcases)
