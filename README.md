# Pettit
## Overview
<img src="README_assets/pettit_icon.png" alt="pettit logo" width="250"/>

Pettit is a full stack web application created for my final capstone project at Code Institute. It was built using all the skills I learned during the course, primarily with the Django web framework (which uses Python), but also including HTML, CSS, and JavaScript. The main objective of Pettit is to provide users with a way to share images and questions about their pets, allowing other users to view and comment on them.

[View Pettit here.](https://pettit-003b91eeeaeb.herokuapp.com/)

## Table of contents
- [Overview](#overview)
- [UX Design](#ux-design)
  - [Colours](#colours)
  - [Fonts](#fonts)
  - [Agile and User Stories](#agile-and-user-stories)
    - [Must Have](#must-have)
    - [Should Have](#should-have)
    - [Could Have](#could-have)
- [Product Planning](#product-planning)
  - [Wireframes](#wireframes)
  - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram)
- [Features](#features)
  - [Navigation](#navigation)
  - [Home Page](#home-page)
  - [About Page](#about-page)
  - [Authentication](#authentication)
  - [User Posts](#user-posts)
  - [User Comments](#user-comments)
  - [Post Filter](#post-filter)
  - [Confirmation](#confirmation)
  - [Error Pages](#error-pages)
- [AI Implementation](#ai-implementation) 
  - [Coding](#coding)
  - [Debugging](#debugging)
  - [Asset Creation](#asset-creation)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Performance and Accessibility](#performance-and-accessibility)
- [Validation](#validation)
  - [HTML](#html)
  - [CSS](#css)
  - [Python](#python)
  - [JavaScript](#javascript)
- [Deployment](#deployment)
- [Credits](#credits)

## UX Design

### Colours

Chosen color palette using [Coolor.](https://coolors.co/) I chose a very simple and non flashy colour palette for simplicity. This can always be changed in the future easily if enough feedback suggests we should.

<details><summary>Coolor Colour Palette</summary>

![coolor colour palette](README_assets/coolor.png)
</details>

### Fonts

I wanted to use simplistic fonts so I decided to use Verdana as a primary font followed by [Roboto](https://fonts.google.com/specimen/Roboto?query=roboto) and [Lato](https://fonts.google.com/?query=lato) as backup fonts which were imported using [Google Fonts.](https://fonts.google.com/) These fonts can be easily changed in the future if needed.

### Agile and User Stories

This project was created using the agile methodology with MoSCoW prioritisation, where user stories were split into "must have," "should have," and "could have" groups. All user stories in the "must have" group should be fulfilled to ensure the project meets minimum viability. 

The project board containing the user stories can be viewed
[here.](https://github.com/users/SParb/projects/10) The user stories are also shown below this section.

#### Must Have
----
<details><summary>Responsive web design:</summary>

As a **user** I can **user the site easily on any screen size** so that **I can have a good user experience**.
<br/><br/>
Acceptance criteria
- Site must be responsive on most Desktop, Laptop and phone screen sizes.
- Site layout and navigation are user friendly, allowing easy access to different sections.
----
</details>

<details><summary>Open a post:</summary>

As a **user** I can **open a post by clicking on it** so that **I can read the post content**.
<br/><br/>
Acceptance criteria
- When a post title or image is clicked, it will show the full details of the post.
----
</details>

<details><summary>Account registration:</summary>

As a **user** I can **register for an account** so that **I can comment on posts or create my own posts**.
<br/><br/>
Acceptance criteria
- The user must provide an email address to register for an account.
- The user must then provide a unique username and a password for their account.
- The user must be logged into their account to comment on posts
----
</details>

<details><summary>Comment on a post:</summary>

As a **registered user** I can **leave a comment on a post** so that **other users can see my comment on that post**.
<br/><br/>
Acceptance criteria
- If the registered user is logged in they can leave a comment on a post.
- The comment must be approved by a site admin before being seen by other users.
- The user can edit their comment, but it will require reapproving by a site admin or they can delete the comment entirely.
----
</details>

<details><summary>Approve or delete comments on a post:</summary>

As a **site admin** I can **approve or delete comments** so that **nothing hateful or objectionable is visible**.
<br/><br/>
Acceptance criteria
- If the site admin is logged in as an admin, they can approve comments to be seen by users.
- If the site admin is logged in as an admin, they can delete users accounts if they are constantly attempting to be harmful to the website and its users.
----
</details>

<details><summary>Read about the site:</summary>

As a **user** I can **click the about link** so that **I can read about the sites purpose, frequently asked questions and its rules**.
<br/><br/>
Acceptance criteria
- When the about link in the navigation bar is clicked, the about text will display.
----
</details>

<details><summary>Create a post:</summary>

As a **registered user** I can **make my own posts** so that **other users can see and comment on my post**.
<br/><br/>
Acceptance criteria
- If the registered user is logged in, they can create a post for others to see.
- The user can leave an image and a block of text describing their post.
- The post must be approved by a site admin before being seen by other users.
- The user can edit their post, but it will require reapproving by a site admin or they can delete the post entirely.
----
</details>

<details><summary>Approve or delete user created posts:</summary>

As a **site admin** I can **approve or delete posts** so that **nothing hateful or objectionable is on the post**.
<br/><br/>
Acceptance criteria
- If the site admin is logged in as an admin, they can approve posts to be seen by users or delete them.
- If the site admin is logged in as an admin, they can delete users accounts if they are constantly attempting to be harmful to the website and its users.
----
</details>

#### Should Have
----

<details><summary>Confirmation messages:</summary>

As a **registered user** I can **see that my comment or post was submitted successfully** so that **I am sure my comment or post was submitted**.
<br/><br/>
Acceptance criteria
- If the registered user submits a comment or post, there should be some kind of confirmation message for the user.

- If the registered user deletes or edits a comment or post, there should be some kind of confirmation message for the user.
----
</details>

#### Could Have

----

<details><summary>Like or dislike a post:</summary>

As a **registered user** I can **click a button to like or dislike a post** so that **other users can see if more people like or dislike a post**.
<br/><br/>
Acceptance criteria
- If the registered user is logged in, they can click a like or dislike button, increasing the posts like or dislike counter.
- Other users can see the like to dislike ratio on a post before clicking on it
----
</details>

<details><summary>Filter posts by pet:</summary>

As a **user** I can **add a post filter** so that **I can only see posts of a specific pet**.
<br/><br/>
Acceptance criteria
- The user can interact with a dropdown filter, so that only posts which show a specific kind of pet are shown (e.g dog, cat, bird etc)
----
</details>

## Product Planning

### Wireframes

Wireframes on both large screens and smaller screens were created using the [Balsamiq program.](https://balsamiq.com/)

<details><summary>Home Page</summary>

![Home Page Wireframe](README_assets/Homepage_Wireframe.jpg)
</details>

<details><summary>About Page</summary>

![About Page Wireframe](README_assets/About_Wireframe.jpg)
</details>

<details><summary>Post Detail Page</summary>

![Post Detail Page Wireframe](README_assets/PostDetail_Wireframe.jpg)
</details>

<details><summary>Create Post Page</summary>

![Create Post Page Wireframe](README_assets/CreatePost_Wireframe.jpg)
</details>

### Entity Relationship Diagram

Below is the entity relationship diagram (ERD) which showcases the relationships between the modals. This was created using [LucidChart](https://www.lucidchart.com/pages).

<details><summary>Entity Relationship Diagram</summary>

![Entity Relationship Diagram](README_assets/ERD.jpg)
</details>

## Features

### Navigation
A responsive navigation bar is always stuck at the top of a webpage for site navigation.

<details><summary>Logged In</summary>
Navigation bar when a user is logged in. They can create a post and log out, but cannot log in or sign up as they are already logged in.

![Navbar when logged in](README_assets/features/NavigationLoggedIn.jpg)
</details>

<details><summary>Logged Out</summary>
Navigation bar when a user is not logged in. They can sign up or log in, but cannot create a post or log out because they are not logged in.

![Navbar when not logged in](README_assets/features/NavigationLoggedOut.jpg)
</details>

<details><summary>Mobile View</summary>
On smaller screens the Navigation bar becomes a burger format.

![Navbar on smaller screens](README_assets/features/NavigationMobile.jpg)
</details>

### Home page

<details><summary>Home Page</summary>
The home page will show the user a collection of uploaded posts. They show the post title, the author, an image to go along with the post, time created and the number of comments on that post. If no image is provided with a post it will use the pettit logo as a placeholder.

Users can click on a post to view them in more detail. There are six posts per page with pagination at the bottom of the page to look at more posts.

![Home Page](README_assets/features/HomePage.jpg)
</details>

### About page

<details><summary>About Page</summary>
An about page which will tell the user the purpose of the website and rules. A user can also send feedback to the developers on ways to improve the website. A confirmation message will appear if a user submits feedback.

![About Page](README_assets/features/AboutPage.jpg)
</details>

### Authentication

<details><summary>Sign Up</summary>
The sign up page will ask the user to create an account so that they can create their own posts and leave comments on posts.

![Sign Up](README_assets/features/SignUp.jpg)
</details>

<details><summary>Log In</summary>
The log in page will ask the user for their credentials to log in. If they do not have an account they can be redirected to the sign up page to create an account.

![Log In](README_assets/features/LogIn.jpg)
</details>

<details><summary>Log Out</summary>
When a user wants to log out they are sent to the log out page to confirm they do want to log out.

![Log Out](README_assets/features/LogOut.jpg)
</details>

### User Posts

<details><summary>Create Post</summary>
The page a logged in user is sent to when they want to create their own post. A post must have a title and pet type and some description. Users can upload an image, if no image is uploaded then a default placeholder image will be used instead. Posts must be approved by an admin before other users can see the post on the homepage.

![Create Post](README_assets/features/CreatePost.jpg)
</details>

<details><summary>Edit Post</summary>
On a post a logged in user owns, a button will appear giving them the option to edit their post in a similar fashion as creating a post. Edited posts must be reapproved by an admin before other users can see the post on the homepage.

![Edit Post](README_assets/features/EditPost.jpg)
</details>

<details><summary>Delete Post</summary>
On a post a logged in user owns, a button will appear giving them the option to delete their post. A confirmation modal appears asking if they are sure they want to delete their post.

![Delete Post](README_assets/features/DeletePost.jpg)
</details>

### User Comments

<details><summary>Post Comment</summary>
A logged in user can post a comment on a post. The posted comment will be greyed out and invisible to other users until it has been approved by an admin.

![Post Comment](README_assets/features/CreateComment.jpg)
</details>

<details><summary>Edit Comment</summary>
A logged in user can edit a comment they previously posted on a post. The edited comment will be greyed out and invisible to other users until it has been reapproved by an admin.

![Edit Comment](README_assets/features/EditComment.jpg)
</details>

<details><summary>Delete Comment</summary>
A logged in user can delete a comment they previously posted on a post. A confirmation modal appears asking if they are sure they want to delete their comment.

![Delete Comment](README_assets/features/DeleteComment.jpg)
</details>

### Post Filter

<details><summary>Post Filter</summary>
A user can use the filter to only show posts of a certain pet type (All, Cat, Dog, Bird Rabbit, Other). A logged in user can also filter posts by posts they created (All, My Posts). Both filters can be used at the same time.

![Post Filter](README_assets/features/PostFilter.jpg)
</details>

### Confirmation

<details><summary>Confirmation</summary>
Whenever a user logs in or out, create/edit/delete a post or comment a message at the top of the page will show up confirmation the action they did has be acknowledged. Below is an example when a user logs in.

![Confirmation](README_assets/features/Confirmation.jpg)
</details>

### Error Pages

<details><summary>404</summary>
When the user submits an invalid URL it will send the user to a custom 404 error page.

![Confirmation](README_assets/features/404.jpg)
</details>

<details><summary>Other Errors</summary>
If a user tries to create, edit, or delete a post or comment using the URL but is not the owner of that post or comment, they will be sent to an error page stating that they must be the owner or logged in. Below is an example of trying to edit a post the user does not own.

![Error Example](README_assets/features/ErrorExample.jpg)
</details>

## AI Implementation

### Coding

Reflection: AI was efficient at saving time by quickly producing repetitive code. It also helped by creating simple foundations for functions and classes that could be expanded upon. However, any code produced by AI that I did not immediately understand was diregarded, as relying on such code can lead to not fully understanding your own project.

Example: AI assisted in creating basic view functions and writing repetitive code in the HTML files.

### Debugging

Reflection: AI was a helpful tool in speeding up the fixing of bugs and errors that humans will inevitably make.

Example: Most simple bugs were resolved manually. However, more complex bugs typically those spanning multiple files were resolved by asking AI for help, using any error messages provided by the local server when DEBUG = True in the settings.py file or by the terminal.

### Asset Creation

Reflection: AI was able to produce images appropriate for the websites function and aesthetic.

Example: AI was used to generate the Pettit logo and icon when the user encounters a 404 error.

## Testing

### Manual Testing

<details><summary>Try to create post while not logged in</summary>
If a user tries to create a post while not logged in they will be redirected to this page.

![Try to create post while not logged in](README_assets/testing/CreatePostLoggedOut.jpg)
</details>

<details><summary>Try to edit post while not logged in</summary>
If a user tries to edit a post while not logged in they will be redirected to this page.

![Try to edit post while not logged in](README_assets/testing/EditPostLoggedOut.jpg)
</details>

<details><summary>Try to delete post while not logged in</summary>
If a user tries to delete a post while not logged in they will be redirected to this page.

![Try to delete post while not logged in](README_assets/testing/DeletePostLoggedOut.jpg)
</details>

<details><summary>Try to access an unapproved post</summary>
If a user tries to access a post that has not been yet approved they will be redirected to this page.

![Try to access an unapproved post](README_assets/testing/UnapprovedPost.jpg)
</details>

<details><summary>Try to comment on a post while not logged in</summary>
If a user tries to comment on a post while not logged in they told they need to log in to comment.

![Try to comment on a post while not logged in](README_assets/testing/CommentLoggedOut.jpg)
</details>

<details><summary>Try to edit post that does not belong to the logged in user</summary>
If a logged in user tries to edit a post they do not own they will be redirected to this page.

![Try to edit post that does not belong to the logged in user](README_assets/testing/EditPostLoggedIn.jpg)
</details>

<details><summary>Try to delete post that does not belong to the logged in user</summary>
If a logged in user tries to delete a post they do not own they will be redirected to this page.

![Try to delete post that does not belong to the logged in user](README_assets/testing/DeletePostLoggedIn.jpg)
</details>

<details><summary>Try to edit or delete comment that does not belong to the logged in user</summary>
If a logged in user cannot edit or delete a comment they did not post.

![Try to edit or delete comment that does not belong to the logged in user](README_assets/testing/CommentLoggedIn.jpg)
</details>

<details><summary>Creating a post requires approval</summary>
If a logged in user creates a post an admin will have to approve the post before anyone can see it.

![Creating a post requires approval](README_assets/testing/CreatePostApproval.jpg)
</details>

<details><summary>Commenting requires approval</summary>
If a logged in user comments on a post an admin will have to approve the comment before anyone can see it but the owner can see it with a message saying waiting for approval.

![Commenting requires approval](README_assets/testing/CommentApproval.jpg)
</details>

<details><summary>Broken URL</summary>
If a user tries to access a page that does not exist they will be redirected to a 404 error page.

![Broken URL](README_assets/testing/404.jpg)
</details>

### Performance and Accessibility

[Google Lighthouse](https://developer.chrome.com/docs/lighthouse) was used to test the performance and accessibility of my webpages.

## Validation

### HTML

HTML validation was checked using [W3C HTML Validation Service.](https://validator.w3.org/) There were no validation errors with the exception of a few validation errors on the sign-up page as this was managed by the Django auth package.

<details><summary>Home Page</summary>

![Home Page HTML Validation](README_assets/Homepage_Validation.jpg)
</details>

<details><summary>About Page</summary>

![About Page HTML Validation](README_assets/About_Validation.jpg)
</details>

<details><summary>Post Detail Page</summary>

![Post Detail Page HTML Validation](README_assets/PostDetail_Validation.jpg)
</details>

<details><summary>Create Post Page</summary>

![Create Post Page HTML Validation](README_assets/CreatePost_Validation.jpg)
</details>

### CSS

CSS validation was checked using [W3C CSS Validation Service.](https://jigsaw.w3.org/css-validator/) No validation errors were present.

<details><summary>style.css</summary>

![css validation](README_assets/CSS_Validation.jpg)
</details>

### Python

Python validation was checked using [Heroku's python linter](https://pep8ci.herokuapp.com/) to ensure the code adheres to PEP8 standards. There are no screenshots included, as there are too many Python files for this README, but every Python file did pass the test.

### JavaScript

JavaScript validation was checked using [JSHint.](https://jshint.com/) No validation errors were present.

<details><summary>comments.js</summary>

![comments.js validation](README_assets/Comments.js_Validation.jpg)
</details>

<details><summary>posts.js</summary>

![posts.js validation](README_assets/Posts.js_Validation.jpg)
</details>

## Deployment

[Link to Github Repository.](https://github.com/SParb/SParb-CodeInstitute-Capstone-Project)

[Website Deployment using Heroku.](https://pettit-003b91eeeaeb.herokuapp.com/)

Using Heroku, I was able to create a Heroku app (Pettit) which was then connected to my GitHub repository. Several config vars were set in the Pettit app settings so that the app could use the database provided by Code Institute (with secret key) and access my Cloudinary account for handling uploaded media.

## Credits

- The step-by-step process used to set up a basic Django project was created by Code Institute. The database was also provided by Code Institute.
- VSCode was the IDE used to create this project
- Copilot AI for creating certain assets and helping with debugging and basic code generation.
- Bootstrap framework for front-end templates.
- Cloudinary for handling all uploaded media.
- Google Lighthouse for checking site optimisation.
- Heroku for hosting the final deployment.
- And all other sites and applications mentioned in this README.

Thank you to the Code Institute team for teaching and supporting me on this course.

----
[Back to table of contents.](#table-of-contents)
