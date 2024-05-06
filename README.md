# Shopping List App

[-> Link to live site here <-](https://shopping-list-app-bd52d42b5faa.herokuapp.com/)

Shopping List App is a simple lightweight application which allows users to create a shopping list. This will help the user to note down items as they realise they need them, and not forget them when they are in the supermarket.

The app is built mainly utilising Django Python web framework and primarily makes use of CRUD (create, read, update & delete) functions.

The user is able to add items to a list, edit these items by changing their name or marking as complete (bought), and delete items off the list. Users must register an account to use the app and can access their list if logged in. Each user can only see their own lists and entered items. The data is stored on a cloud database meaning that a user can log in anywhere and on any device. A one-to-many relationship is adopted on this project for simplicity.

[-> Link to live site here <-](https://shopping-list-app-bd52d42b5faa.herokuapp.com/)

![Responsive Mockup Of Site](readme_files/images/responsive_site.PNG)

## User Stories

In the development of this project, an agile approach was utilised. This helped initially to break down the project into more manageable chunks by mapping out steps to achieve the final goal. User stories are a big part of the agile approach and help to specify goals based on the user/client requests. 

I used github boards for my user stories. It allows you to input user stories as an 'issue' into a to-do list. They were then moved to in progress as the acceptance criteria were worked on. Once the acceptance criteria were met, the user story is complete and moved to the 'done' column of the board. When working in a team it is a great way of keeping track of who is doing what, espically as you can comment on the issues.

![User Stories](readme_files/images/user_stories.PNG)

Here are the user stories for this project:

- Register Account - As a site user I can register an account so that I am able to see personally created lists.
    - Acceptance criteria 1 - User able to register account using username(maybe email) and password.
    - Acceptance criteria 2 - User able to login/logout securely using these credentials.

- Create a list – As a user I am able to create a shopping list that is my own.
    - Acceptance criteria 1 - User not able to see other user's items.
    - Acceptance criteria 2 - Lists created by user are only viewable by that specific user.

- Add items to list – As a user I am able to add custom items to my shopping list.
    - Acceptance criteria 1 - Able to add custom items to a list.
    - Acceptance criteria 2 - The item must be simple to input.

- Save list – As a user I am able to view a created list at a later date.
    - Acceptance criteria 1 - The list is saved to the database so that the user is able to view again at a later date.
    - Acceptance criteria 2 - The saved list is accessible when the user logs back on.

- Check items – As a user I am able to click on an item on the list in order to show that it is obtained. This will be shown clearly with strikethrough text.
    - Acceptance criteria 1 - Clicking/tapping on item in list checks it off list.
    - Acceptance criteria 2 - Item shows with strikethrough text and different colour to make it obviously checked.

- Modify or delete items in list – As a user I am able to modify or delete items on my list.
    - Acceptance criteria 1 - User able to delete items off list by clicking a button.
    - Acceptance criteria 2 - User able to modify text of item by clicking a button.

- Clean UX – As a user I expect a straight forward user interface so that I have a good experience while using the app.
    - Acceptance criteria 1 – Interface easy to navigate.
    - Acceptance criteria 2 – No clashing colors so that text is easy to read.
    - Acceptance criteria 3 – Responsive to different devices and screen sizes.


## Features

### Existing Features

- __Register__

    - The register view allows the user to create an account.
    - The user inputs a chosen username and password which they must enter twice to avoid a mistake in the password.
    - This information is stored on the database with the password being encripted.
    ![Register](readme_files/images/register.PNG)



- __Login__

    - The login view acts as the landing page for the app if not already logged in.
    - If already registered, a user can enter their username and password to take them to their personalised list view page.
    ![Login](readme_files/images/login.PNG)



- __List__

    - The list page is the main view of the app.
    - The user can only see it if logged in.
    - The header on the list page states "Hello -Username-" with the first letter of the name always being capitalized by the {{request.user|title}} function.
    - The header also says how many items the user has left to buy. The word 'items' utilizes a pluralize function in order to remove the 's' to say 'item' when the number is 1.
    - At the top right of the page there is a 'Logout' button. This will log out the user and direct them back to the login page.
    ![List](readme_files/images/list_view.PNG)
     - The main area of the list view is populated by the list itself.
     - The add item button takes the user to the create list view where they can create a list item.
     - When an item is added, it is listed with a grey circle next to it. This shows that it has not yet been obtained.
     - When an item is clicked the user is taken to the edit view where they can rename it or mark as complete(checked).
     - When an item is marked as complete, the grey circle becomes green and the text becomes italic and strikethrough. The item also then goes to the bottom of the list. This makes it extremely clear that the item has been marked as complete.


