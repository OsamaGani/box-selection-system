
# Test Output

## Environment

- Framework: Django
- Test framework: Django TestCase
- Application: boxes

## Command Executed

```powershell
python manage.py test boxes
```

## Test Results

```text
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.014s

OK
Destroying test database for alias 'default'...
```

## Summary

- Total tests: 5
- Passed: 5
- Failed: 0
- Status: OK

## Notes

These tests cover the cheapest suitable box, weight capacity, dimension constraints, empty orders, and multiple products that cannot fit inside a small box.

Passing these tests does not guarantee that the packing algorithm handles every possible arrangement correctly.
