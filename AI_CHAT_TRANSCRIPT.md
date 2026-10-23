
# AI-Assisted Development Chat Transcript

**Project:** AI-Assisted Box Selection System  
**AI Tool:** ChatGPT  
**Format:** Reconstructed summary of the development conversation, not a verbatim transcript.

## 1. Project Setup

**User:** I want to build a Python and Django-based box selection system. Please guide me step by step because I want to write the code myself in VS Code.

**AI:** We can build the project in stages: Django setup, database models, box recommendation logic, API development, automated tests, documentation, and GitHub deployment.

**User:** The project is set up, and I can access the Django admin panel.

**AI:** The next step is to create Product and ShippingBox models to store product dimensions, weight, box dimensions, maximum weight capacity, and cost.

## 2. Box Recommendation Logic

**User:** I want the system to recommend a suitable shipping box for an order and choose the lowest-cost option.

**AI:** We can create a recommendation service that checks weight capacity and attempts to determine whether the products fit inside each available box.

**User:** The system should also check whether multiple products can fit together in one box.

**AI:** We can add a placement heuristic that tries different product orientations and placements. However, a heuristic may not find every valid arrangement, so its limitations must be documented and tested.

## 3. API Development

**User:** How can I test the API from PowerShell?

**AI:** You can send a POST request with a JSON body containing the product IDs. The endpoint can return the recommended box details or an appropriate error response.

**User:** I received a CSRF error while sending the request.

**AI:** CSRF handling needs to be configured appropriately for the endpoint. Any CSRF exemption should be considered carefully, especially before using the endpoint in production.

## 4. Automated Testing

**User:** My tests are passing. What should I do next?

**AI:** The tests should cover the cheapest suitable box, weight limits, dimension constraints, empty orders, and cases where multiple products cannot fit together.

**User:** All five tests passed.

**AI:** That is good progress. However, passing these tests does not guarantee that the packing algorithm handles every possible product arrangement correctly.

## 5. Project Documentation

**User:** Where should I create README.md and AI_USAGE.md?

**AI:** Both files should be created in the root project folder, alongside manage.py, rather than inside the boxes application folder.

**User:** I created the documentation files.

**AI:** The README should explain the project, setup instructions, API usage, tests, and limitations. The AI usage documentation should accurately describe how AI assistance was used and how the code was verified.

## 6. Git and GitHub

**User:** I created a GitHub repository. How do I upload the project?

**AI:** First, initialize Git, create a .gitignore file, stage the appropriate project files, commit them, connect the remote repository, and push the main branch.

**User:** The project has been pushed successfully.

**AI:** The next step is to configure GitHub Actions so that the system checks and automated tests can run when changes are pushed.

## 7. GitHub Actions

**User:** Please create the workflow using terminal commands.

**AI:** Create the `.github/workflows/django-tests.yml` file and configure it to check out the repository, set up Python, install Django, run `python manage.py check`, and run `python manage.py test boxes`.

**User:** The GitHub Actions workflow completed successfully.

**AI:** Verify the workflow logs and retain the actual test results for the assignment.

## 8. Verification and Limitations

The project was tested locally with five Django test cases, and a GitHub Actions workflow was added to run automated checks.

The packing algorithm uses a heuristic and may fail to identify some valid packing arrangements. Further testing and improvements are needed before treating it as a complete packing solution.

## Note

This document is a reconstructed summary of the development discussion. It is not the original exported ChatGPT conversation. The original transcript should be included separately if required by the assignment.
