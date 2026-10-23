# AI Usage Documentation
## 1. AI Tools Used
I used ChatGPT for guidance while developing this Python and Django project.
## 2. Prompts and Assistance
I asked ChatGPT for help with:
- Setting up the Django project and understanding its folder structure.
- Creating Product and ShippingBox models.
- Implementing box recommendation logic based on product dimensions, weight capacity, and cost.
- Creating a JSON API endpoint.
- Writing Django automated tests.
- Understanding Git commands and pushing the project to GitHub.
- Setting up a GitHub Actions workflow.
- Preparing project documentation.
These are summaries of the prompts used, not verbatim copies of every prompt.
## 3. Outputs Accepted or Modified
I used AI suggestions as a starting point for models, the recommendation service, API implementation, tests, and GitHub Actions configuration.
I also adjusted the project files and commands during development when errors or incorrect file locations were encountered.
The packing logic uses a heuristic, so its results need further validation. Passing the current tests does not prove that every possible product arrangement will be handled correctly.
## 4. Mistakes and Issues Encountered
During development:
- Some documentation files were initially created inside the `boxes` folder instead of the project root. They were moved to the correct location.
- A CSRF error occurred while testing the API locally, requiring changes to the endpoint's CSRF handling.
- The packing heuristic has limitations and may fail to find some valid arrangements.
- File locations and Git status were checked before committing and pushing the project.
## 5. Verification
I ran the following commands locally:
```powershell
python manage.py check
python manage.py test boxes
```
The local test run reported five passing tests.
I also configured a GitHub Actions workflow to run the Django system check and test suite. The workflow completed successfully during development.
These checks provide basic verification but do not guarantee that the packing algorithm handles all possible cases.
## 6. Limitations and Future Improvements
Potential improvements include:
- Adding more edge-case tests.
- Improving and validating the 3D packing algorithm.
- Testing additional product orientations and combinations.
- Reviewing API security before production use.
## 7. Responsibility
I am responsible for understanding, reviewing, and maintaining the submitted code. AI-generated suggestions must be checked against the actual implementation before they are accepted.
