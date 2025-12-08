# Pettit
## Overview
<img src="README_assets/pettit_icon.png" alt="pettit logo" width="250"/>

Pettit is a full stack web application made for my final capstone project at Code Institute. It was built using all the skills I learned during Code Institute, primarily with the Django web framework. The main objective of Pettit is to provide users with a way to share images and questions about their pets for other users to see and leave comments on.

## Table of contents
- [Overview](#overview)
- [User Stories](#user-stories)
  - [Must Have](#must-have)
  - [Should Have](#should-have)
  - [Could Have](#could-have)
- [Product Planning](#product-planning)
  - [Wireframes](#wireframes)
  - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram)
- [UX Design](#ux-design)
  - [Colours](#colours)
  - [Fonts](#fonts)
- [Features](#features)
- [AI Implementation](#ai-implementation) 
- [Testing](#testing)
- [Validation](#validation)
  - [HTML](#html)
  - [CSS](#css)
  - [Python](#python)
  - [JavaScript](#javascript)
- [Deployment](#deployment)
- [Credits](#credits)

## User Stories

[Project board](https://github.com/users/SParb/projects/10)

### Must Have
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

### Should Have
----

<details><summary>Confirmation messages:</summary>

As a **registered user** I can **see that my comment or post was submitted successfully** so that **I am sure my comment or post was submitted**.
<br/><br/>
Acceptance criteria
- If the registered user submits a comment or post, there should be some kind of confirmation message for the user.

- If the registered user deletes or edits a comment or post, there should be some kind of confirmation message for the user.
----
</details>

### Could Have

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
### Entity Relationship Diagram
## UX Design
### Colours
Chosen color palette using [Coolor:](https://coolors.co/)
### Fonts

## Features

## AI Implementation
GitHub Copilot helped with some suggested user stories and grammatical errors.

## Testing

## Validation

### HTML

### CSS

CSS validation was checked using [W3C CSS Validation Service.](https://jigsaw.w3.org/css-validator/)

<details><summary>style.css</summary>

![css validation](README_assets/CSS_Validation.jpg)
</details>

### Python

### JavaScript

JavaScript validation was checked using [JSHint](https://jshint.com/)

<details><summary>comments.js</summary>

![comments.js validation](README_assets/Comments.js_Validation.jpg)
</details>

<details><summary>posts.js</summary>

![posts.js validation](README_assets/Posts.js_Validation.jpg)
</details>

## Deployment

## Credits

[Back to table of contents](#table-of-contents)
