
# AI Usage Documentation

## 1. AI Tools Used

I used ChatGPT to help me understand parts of the Python and Django project and to troubleshoot issues during development.

## 2. How AI Was Used

AI assistance was used for:
- Understanding the Django project structure.
- Learning how to create Django models and register them in the admin panel.
- Understanding how to build a JSON API endpoint.
- Discussing the shipping box selection and packing logic.
- Writing and improving automated test cases.
- Troubleshooting errors and understanding test results.
- Preparing project documentation.

## 3. Code Review and Verification

I ran the Django system check and automated tests locally.

Command used:

```bash
python manage.py check
python manage.py test boxes
```

The test run reported five passing tests.

I reviewed the output to check whether the implemented functionality behaved as expected. Passing tests do not guarantee that the packing algorithm works correctly for every possible product arrangement.

## 4. Limitations and Improvements

The current packing algorithm uses a heuristic. It may fail to find some valid packing arrangements.

Further improvements could include testing more product combinations, checking different product orientations, and comparing the results against a more complete packing algorithm.

## 5. My Responsibility

I am responsible for reviewing, understanding, testing, and maintaining the code submitted in this project.

AI-generated suggestions should be checked against the actual implementation before being accepted.
