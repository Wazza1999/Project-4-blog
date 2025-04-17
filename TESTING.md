# Testing

As each section or Function/Model was built during this project, I was testing for functionality and styling issues that may have arisen (see table below), which were corrected or fixed before continuing. I also had friends test the site by signing up, adding and deleting comments using various devices on varying platforms (IOS, Android, Mobile, Tablet etc) and reporting back any issues they encountered with functionality or styling.

# Automatic Testing

- Using the walkthrough I was able to make some automatic testing code for some of the views but there was still some bugs during development causing the tests to fail which were eventually fixed.

- FAIL: There was a bug with testing whether a comment was submitted correctly or not 

![Test1](documentation/tests/test1.JPG)

- FAIL: 404 error for the testing whether a comment was posted correctly

![Test2](documentation/tests/test2.JPG)

- PASS: All tests passing 

![Test3](documentation/tests/test3.png)

## Manual Testing

_For any Fails, there is a more detailed description below the table_

ADMIN
| TEST | OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Create Blog Post | Post successfully created and displayed | Pass |
| Edit Blog Post | Editing post in the website successful | Pass |
| Delete Blog Post | Deleting selected post successfull | Pass |
| Delete User Comments | Comment deleted successfully | Pass |
| Create 4 Test Posts to check Pagination | Next/Previous Page Appears at bottom of screen | Pass |

## User

|                                TEST                                |                                  OUTCOME                                   | PASS/FAIL |
| :----------------------------------------------------------------: | :------------------------------------------------------------------------: | :-------: |
|                           Create Account                           |                            Created successfully                            |   Pass    |
|                               Login                                |                              Login Successful                              |   Pass    |
|                               Logout                               |                             Logout Successful                              |   Pass    |
|                        Read Full Blog Post                         |                    PostDetail page loaded successfully                     |   Pass    |
|                          Add a Blog Post                           |        Add a post page loaded successfully and addition successful         |   Pass    |
|                          Delete Blog Post                          |                  Delete post button working successfully                   |   Pass    |
|                     Add Comment under Blogpost                     |                         Comment Added Successfully                         |   Pass    |
|                           Delete Comment                           |                              Comment Deleted                               |   Pass    |
|                      Filter Posts by category                      |          Posts marked as selected category displayed successfully          |   Pass    |
| Create User Account to check access to restricted pages (add_post) | Page displayed correct error message, with no access to restricted content |   Pass    |

(\*) See Bugs below

## Solved Bugs

![About url error](documentation/tests/about.JPG)

- This error was due to the database and my code not making a url for the about page. Was solved with the help of tutors.

![About image error](documentation/tests/aboutimageerror.png)

- This error was because the image I gave the database was not showing up due to incorrect code in my about.html file which was rectified

![Makemigrations error](documentation/tests/capture.JPG)

- This error was due to the database not accepting migrations in the Post model during early development when my knowledge of django was quite basic. This was fixed in the final product.

![Flake8 error](documentation/tests/capture1.JPG)

- This error was due to poor indentation in my code which is now fixed.

![Delete comment error](documentation/tests/comment-delete-error.png)

- This error was similar to the first in that the proper urls for the comment delete view were not being made.



## Lighthouse

The performance scores appear to be low, and I believe this is due to the images uploaded for each blog post being hosted on cloudinary and the image size is too big but couldn't find a fix for it. 

Mobile

![Lighthouse Mobile Score](documentation/tests/lighthousemobile.png)

Desktop

![Lighthouse Desktop Score](documentation/tests/lighthousedesktop.png)

# Validation Testing

# HTML & CSS

### HTML & CSS testing was completed using [W3 Validator](https://validator.w3.org/)

- Home page

![Home Page](documentation/images/homepagevalidation.png)

- Login page

![Login Page](documentation/images/loginvalidation.png)

- Logout page

![Logout Page](documentation/images/logoutvalidation.png)

- Register page

![Register Page](documentation/images/signupvalidation.png)

- About page

![About Page](documentation/images/aboutvalidation.png)

- Category page

![Category Page](documentation/images/categoryvalidation.png)

- Add a post age

![Add a Post Page](documentation/images/addpostvalidation.png)

# CSS Validation

![CSS Validation](documentation/images/cssvalidation.png)

# JS Validation

![JS Validation](documentation/images/jsvalidation.png)

- A note to bear in mind that I didn't change any of this code from the walkthrough as it wasn't necessary but thought I'd include the validation anyway.

## Python Testing

Python pep8 validation was done via [Code Institute's Python Linter](https://pep8ci.herokuapp.com/)

The only errors recieved here were where some lines of text exceeded the limit of 79 characters, but these have now been rectified using the #noqa comment.

Python Files Tested:

- models
- forms
- views
- urls

# Blog Tests

- Admin

![Blog Admin](documentation/pythontest/blogadminvalidation.png)

- Forms

![Blog Forms](documentation/pythontest/blogformsvalidation.png)

- Migration 0001

![Blog Migration 0001](documentation/pythontest/blogmigration0001validation.png)

- Migration 0002

![Blog Migration 0002](documentation/pythontest/blogmigration0002validation.png)

- Migration 0003

![Blog Migration 0003](documentation/pythontest/blogmigration0003validation.png)

- Migration 0004

![Blog Migration 0004](documentation/pythontest/blogmigration0004validation.png)

- Migration 0005

![Blog Migration 0005](documentation/pythontest/blogmigration0005validation.png)

- Migration 0006

![Blog Migration 00006](documentation/pythontest/blogmigration0006validation.png)

- Models

![Blog Models](documentation/pythontest/blogmodelsvalidation.png)

- URLs

![Blog URLs](documentation/pythontest/blogurlvalidation.png)

- Views

![Blog Views](documentation/pythontest/blogviewvalidation.png)

- Test Forms

![Blog TestForms](documentation/pythontest/blogtestformsvalidation.png)

- Test Views

![Blog TestViews](documentation/pythontest/blogtestviewsvalidation.png)

# About Tests

- Admin

![About Admin](documentation/pythontest/aboutadminvalidation.png)

- Apps

![About Apps](documentation/pythontest/aboutappsvalidation.png)

- Forms

![About Forms](documentation/pythontest/aboutformsvalidation.png)

- Migration 0001

![About Migration 0001](documentation/pythontest/aboutmigration0001validation.png)

- Migration 0002

![About Migration 0002](documentation/pythontest/aboutmigration0002validation.png)

- Migration 0003

![About Migration 0003](documentation/pythontest/aboutmigration0003validation.png)

- Models

![About Models](documentation/pythontest/aboutmodelsvalidation.png)

-TestForms

![About TestForms](documentation/pythontest/abouttestformsvalidation.png)

-TestViews

![About TestViews](documentation/pythontest/abouttestviewsvalidation.png)

-URLs

![About URLs](documentation/pythontest/abouturlsvalidation.png)








