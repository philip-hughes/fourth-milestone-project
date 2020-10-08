# Fourth milestone project — "Pizza Dojo - online pizza ordering application"

This project website is an online pizza ordering website for the Pizza Dojo stores.  The primary purpose of the
application is to allow guest users or registered users to select a store based on their home address and place an order to that store for delivery or collection. 

The site comprises the following web pages: select store, menu, cart, checkout and checkout success screen. Logged in users can also update their home address and contact details via the profiles screen.  In addition to these screens there are also the djagno all auth login and registration screens which have both been customised for the project. The site is fully responsive and can be viewed in desktop, tablet and mobile devices. 


## UX


At the beginning of the project I listed the features that were a must for the site, and features that were nice to have. The core flows and features
I wanted were
 1. Allow a guest user to complete the order flow without having to register and login.
 2. For registered users, have their nearest store automatically added to the session on login. 
 3. Allow users to add items to the cart via the menu, and have the total price updated in the headers cart section.
 4. Display selected items on the cart screen with product image, name, quantity and subtotal
 5. Allow users to increase or decrease the quantity of an item on the cart screen, or delete the item from the cart.
 6. Have a one screen menu with links that will scroll the user to each section.  I find this easier than have different products types on seperate 
    screens.
 7. Have a seperate screen for the cart. I'd considered applying a mini cart to the menu screen (a popup / slide out cart that shows items in the cart). This type of approach is used online restaurant sites, but I personally find mini carts clutter the screen too much, particulary on mobile devices, and dont
make for a good user experience.  I prefer screens with minimal functionality and a specific purpose.


An important note is that when I was originally planning the project I had planned on implementing a pizza customization feature that would allow users to
adjust the toppings on a chosen pizza. Due to time constraints I had to descope this feature, but much of the menu and cart code was designed with this feature in mind, and because of this you will see that products of type pizza are handled differently to the other products.  Specifically on the cart screen if you click the + button for a pizza, rather than increasing the quantity of the pizza, a duplicate pizza will be added to the list instead. This was set up this way for a scenario where a user would select two identical pizzas, and then when viewing the pizzas in the cart screen they could choose to customize each one seperately if they wished. I left this code structure in place as I will be completing the customization feature after the project has been submitted, and will be using this app as my primary portfolio project. I discussed this with my mentor and as it doesnt have any negative impact on the other functionality he agreed that there was no issue with leaving it as just as long as it was explained here.

I will also be adding a product management, and order management app (to be used in a store) to the project at a later date.


## Features

### Existing Features — Select store screen
- ** User types their address in the search input field and the google places JS will present a list of Nearby Stores and Other stores. Nearby stores
     are stores located within 5km of the customer location.  Delivery is only available from nearby stores, and so the delivery button is only displayed
     for these stores.
### Existing Features — Menu
- **Menu items** - Menu items are divided into 4 categories: pizzas, sides, desserts and drinks. Pizza items have 3 sizes, but no quantity option. Again, this was designed this way to accomadate the customization functionality.  Other product types have a quantity option, and some have size options
- **Menu section links** - There are four links below the main header that when clicked will scroll the screen to the chosen section. This scroll position 
  is maintainted after the user adds an item.
  
### Existing Features — Cart screen
- **Adjust cart buttons** - For each pizza item in the cart their is an add and delete link.  Clicking the add button will add another pizza to cart.  The 
    other product types have an increase, decrease and delete button.  For these product types clicking the increase or decrease button will alter the    quantity for the item
  - **Empty cart message** - If all items are removed from the cart a message will be displayed, and the checkout button disabled.

### Existing Features — Checkout screen
- **Customer details form** - The address fields are prepopulated based on the address chosen on the select store screen, and are not editable on the checkout screen. If the user wishes to change the address, this could also mean a change in store, so it must be done via the select store screen.
- **Stripe card input** - A standard stripe payment form that requires credit card number, expiration date, CSV and a 5 digit zip code.

### Existing Features — Checkout success screen
- **Order number and thank you message** - The success screen is displayed after successful payment and order creation.  It displays a thank you message and
   the order number.

### Existing Features — Registration screen
- **Customized address field** - This is a customized django signup page which has an additional address field that is required for registration.  The address search is essentially the same as the select store feature. The feature forces the user to choose an address from the dropdown list, and should they choose the wrong address the can reset it using the Change button.
- **Generic error message** - If the user tries to submit the signup form before completing all fields, or if their passwords dont match, an generic error message will be displayed on the form.
### Existing Features — Login screen
- **Standard django login screen** -  This is a standard django login screen style to match the rest of the application.
### Existing Features — Profile screen
- **Change user details** - The profile screen is only availabe for registered, logged in users. Users can change their contact details and default address.

## Technologies Used

— [Bootstrap](https://getbootstrap.com/)
 — Bootstrap was used for the site layout

— [JQuery](https://jquery.com)
 — Jquery is used throughout the project in conjunction with plain javascript for writing to the DOM and local
   storage.

— [Font Awesome](https://fontawesome.com/)
 — Font Awesome icons were used for the calendar toggle button, and for the modal form fields.

— [Google places](https://developers.google.com/places/web-service/overview)
 — Used for autocompleting address search and calculating the distance between the customers address and the various store locations.



## Testing

The following tests were manually executed and passed in Chrome. The chrome dev tools device emulator was used for responsive breakpoint testing.  These tests cover the core flows and functionality of the application that should be run as sanity test after any updates or deployment to a new environment. 


1. Open the app at the menu screen as new user. i.e. not registered / logged in - https://pizza-dojo.herokuapp.com/menu/ and verify that
you are redirected to the select store screen.
2. Enter an address in the search input e.g. 24 grange abbey road, and select an address from the autocomplete dropdown. Click the Go button
   and verify that a list of Nearby and Other stores are displayed.
3. Verify that the Deliver button is only displayed for Nearby stores
4. Select delivery or collect and verify that you are directed to the main menu.
5. On the main menu click each of the menu section buttons: Pizzas, Sides, Desserts, Drinks and verify that the screen scrolls to the correct section.
6. Click on the Add button for one or more items and verify that the scroll position is maintained.
7. Check the cart total in the header section and verify that the total is updated correctly for each item added.
8. Click on the cart button in the header and verify that the cart screen is displayed.
9. Verify that all items that you added to the cart are displayed in the cart with their respective images, name, quantities and subtotals.
10. Verify that Pizza items have a + and delete button. Click the + button and verify that another pizza is added on a new line with a quantity of 1.
11. Click the delete button for one of the pizzas and verify only one of the pizzas is removed from the cart.
12. Click the + and - buttons for one of the other products types and verify that quantity is adjusted accordingly.
13. Verify that if the item quantity is 1 that the - button is no longer displayed for that item.
14. Increase the quantity for the item and verify that the - button is displayed again.
15. Verify that the cart total is adjusted correctly for the increase, decrease and removal of any item.
16. Delete all items in the cart and verify that a message is displayed stating that the cart is empty, and that the checkout button is disabled.
17. Return to the menu using the link in the header.  Add some more items and return to the cart screen.
18. Verify that the items are displayed as expected, and that the Checkout button has been reenabled.
19. Click the Checkout button and verify that the Checkout screen is displayed.
20. For guest users, verify that the Name, email and contact fields are empty, and editable. The address fields should be prepopulated and disabled.
21. Add an name,email and contact number, and then enter 4242424242424242 in the stripe payment form.  Enter any future expiration date, and any number for CSV and zip code.
22. Click the confirm button and verify that the checkout success screen is displayed, and the order number is presented along with the Thank you message.
23. Verify that the cart total in the header is now empty.
24. Refresh the checkout screen and verify that you are directed back to the menu.
25. Go to the cart screen and verify that cart is empty.
26. Verify that the selected store is still displayed in the header.
27. Click the Register button and verify the signup screen is displayed.
28. Enter and name, email, contact number, and select a valid address from the dropdown.  e.g.search for airside retail park, swords
29. Submit the sign up form and verify that you are directed to the menu screen.
30. If you entered the suggested address, then the default selected store should be Swords.
31. Verify that the register and login links are no longer displayed in the header, and in their place is the customer name and a logout link.
32. Click the customer name and verify that the profile screen is displayed and that it the your detail form is prepopulated with the same details
    you entered in the signup form.
33. Change one or more of the fields and click the Apply Changes button.  Exit the profile screen and then open it again, and verify that your updated
    details have been persisted.
34. Return to the main menu, add some items and continue to the checkout screen. Verify that for logged in users all details fields in the checkout form are prepopulated, including Name, email and phone number which arent prepopulated for guest users.
35. Complete the stripe payment input and complete the order flow.
36. Click the Logout link and verify that you are directed to the select store screen.
37. Verify that the Login and register links are again displayed in the header.
38. Click the login link and verify the login screen is displayed as expected.
39. Enter the email address and password you used during sign up and click submit.
40. Verify that you are logged in and directed to the menu screen.  The customer name and logout links should again be displayed in the header.
      

## Deployment

This website was deployed an Heroku server with the following steps.  The version deployed on Heroku is the final version.
1. Go to https://www.heroku.com/ where you'll be presented with a page where you can log in or sign up.
2. Click sign up and complete the form and sign up for the free account
3. Complete the email verification and password steps
4. Login to Heroku and choose the option to create a new app.
5. Give the app a name, select a region and create.
6. If you dont already have Heroku installed locally, you can install using the steps here - https://devcenter.heroku.com/articles/heroku-cli#download-and-install
7. Once Heroku is installed, open your IDE terminal and run 'heroku login', and fill out the required fields.
8. Go back to the Heroku dashboard in your browser, and click on the Settings link for your app. From here
   you can get the Heroku git URL. e.g. https://git.heroku.com/pizza-dojo.git
9. Go back to the IDE terminal and run 'git add remote heroku https://git.heroku.com/pizza-dojo.git'.
10. Next, install Gunicorn which will be used to as part of the deployment. You can install with the
    following command 'pip3 install gunicorn' 
11. Next create a requirements.txt file with the following command 'pip3 freeze --local > requirements.txt'
12. Commit the requirements.txt file to your local git repository.
13. Add a Procfile with the following command 'echo web: gunicorn app:app > Procfile'
14. Push the application to Heroku with 'push -u origin master' 
15. Run the application with heroku ps:scale web=1
16. Check the application is running at https://pizza-dojo.herokuapp.com/
16. If there are any issues with the deployment you can check files and logs with following commands:
    heroku run bash -a doctor-docs
    heroku logs -n 200
    heroku logs --tail   

Note that the static and media files are hosted on AWS. The steps for AWS setup are quite extensive, and it would be best to follow their online guide 
at https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html

If you want to run the site locally you need to download the site files from Github and host it on a Python server with django installed.
1. To download the site files, go to https://philiph80.github.io/fourth-milestone-project/, then click the Clone or Download button and select Download Zip.
2. Extract the downloaded zip and install the project dependencies in the requirements.txt file.  


## Credits

### Content
— The logo image was found through a google search. The menu items images were taken from the dominos website.

### Acknowledgments

— The webhook failover code was implemented using steps outlined in a code institute project and is very similar in structure to webhook handlers in the demo project.  This seemed the optimal approach, so i saw no reason to do it any differently.
— The solution to maintain scroll position between screens was implemented using a solution i found in an online tutorial.
- All other work is my own.