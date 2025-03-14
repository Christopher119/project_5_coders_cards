# Coders Cards
This is a DJango-based e-commerce website for a fictional Trading Card Game (TCG) for programmers and coders.

# Five UX Planes

## Strategy

Users will want a clean presentation of information.<br>
Users will want an easy navigation.<br>
Users will want to be able to create a profile.<br>
Users will want a clean presentation of information.<br>
Users will want to see all products.<br>
Users will want to filter products.<br>
Users will want to search prodcuts.<br>
Users will want to view specific products.<br>
Users will want to be able to add products to their cart.<br>
Users will want their cart to remain updated.<br>
Users will want to be able to checkout and purchase items.<br>
Users will want to view order history.<br>
Users will want to be able to review products.<br>
Users will want to be able to update or delete their reviews.<br>
Users will want the ability to stay updated on events and deals.<br>
Users will want to be able to view blog posts.<br>
Users will want to see all blog posts.<br>
Users will want to view specific blog posts.<br>
Users will want to leave their thoughts on a blog post.<br>
Users will want to be able to update or delete their comments.<br>

Admins will want to be able to manage products.<br>
Admins will want to be able to update products.<br>
Admins will want to be able to delete products.<br>
Admins will want to be able to add new products.<br>
Admins will want to be able to view user reviews of products.<br>
Admins will want to be able to approve user reviews.<br>
Admins will want to be able to delete user reviews.<br>
Admins will want to be able to create blog posts.<br>
Admins will want to be able to update and delete blog posts.<br>
Admins will want to be able to view user comments on blog posts.<br>
Admins will want to be able to approve or delete user comments on blog posts.<br>

## Scope

The site should be cleanly presented, with all information clearly presented.<br>
The site should allow users to signup, login, and logout.<br>
The site should easily present a list of all available products, including filtering and search options.<br>
The site should easily present a list of all blog posts.<br>
The site should create dynamic views for each blog post to view in full.<br>
The site should have a form to allow an admin to easily create a new product.<br>
The site should have a form to allow an admin to easily create a new blog post.<br>
The site should have a form to allow a user to leave a comment on a blog post.<br>
The site should create dynamic views for each product to present more detailed information.<br>
The site should easily allow users to add products to their cart.<br>
The site should clearly communicate when a user's cart is updated.<br>
The site should have a form to allow users to submit reviews.<br>
The site should display approved reviews to users.<br>
The site should use Stripe to handle checkout.<br>
The site should clearly present order history in a user's profile.<br>
The site should allow user's to update their profile details.<br>
The site should clearly communicate when a user's cart is updated.<br>

## Structure

In order to fulfill the users wants from the Strategy plane and the plans from the Scope plane I created a flowchart to understand the site's flow.<br>
![Image of flowchart for the site](README-images\PP5-FLOWCHART.PNG)

I also created a Entity-Relationship Diagram to get a better idea of what I would need to construct to make the site function as required.<br>
![Image of an ERD for the site](README-images\PP5-ERD.PNG)

## Skeleton

A wireframe was drawn up before any code was written to understand how to present information on the home page.<br>
![Image of a wireframe for the home page](README-images\PP5-HOME-PAGE-WIREFRAME.PNG)

A wireframe was drawn up before any code was written to understand how to present information on the profile page.<br>
![Image of a wireframe for the profile page](README-images\PP5-PROFILE-PAGE-WIREFRAME.PNG)

A wireframe was drawn up before any code was written to understand how to present information on the authentication pages.<br>
![Image of a wireframe for the login/logout/signup page](README-images\PP5-AUTH-PAGES-WIREFRAME.PNG)

A wireframe was drawn up before any code was written to understand how to present information on the product page.<br>
![Image of a wireframe for the product page](README-images\PP5-PRODUCTS-WIREFRAME.PNG)

A wireframe was drawn up before any code was written to understand how to present information on the product details page.<br>
![Image of a wireframe for the product details page](README-images\PP5-PRODUCT-DETAILS-WIREFRAME.PNG)

A wireframe was drawn up before any code was written to understand how to present information on the blog page.<br>
![Image of a wireframe for the blog page](README-images\PP5-BLOG-WIREFRAME.PNG)

A wireframe was drawn up before any code was written to understand how to present information on the blog post page.<br>
![Image of a wireframe for the blog post page](README-images\PP5-BLOG-POST-WIREFRAME.PNG)

## Surface

I wanted everything on the site to be cleanly presented.<br>
I wanted to avoid using too many colours to not distract from the presentation of products.<br>

# Features

## Home
The site initially loads a view of the home page which has links to every other part of the site.<br>
![Image of the  page]()

## Products
The site will display a list of all available products.<br>
![Image of the page]()

### Product Details
The site will display a more detailed view of the specific product and any reviews on it.<br>
![Image of the page]()

## Blog
The site will display a list of all blog posts.<br>
![Image of the page]()

### Blog Post
The site will display a more detailed view of the specific blog post and any comments on it.<br>
![Image of the page]()

## Cart
The site will display a list of all items a user has added to their cart and an option to checkout.<br>
![Image of the page]()

## Profile
The site will display a user's details, the option ot update them, and their order history.<br>
![Image of the page]()

## Signup  Login  Logout
These are simple forms to register, login, and logout of the site.<br>
![Images of the Signup form]()
![Images of the Login forms]()
![Images of the Logout form]()

# Features Left to Implement

1. Edit and Deletion of Comments on Blog Posts.<br>
    Due to trying to streamline the comment functionality rather than using a similar structure to how products and blog posts are edited and delted the comments are currently immutable without access through the Admin panel.<br>
    Will require a way to access the UserProfile successfully or sacrifice ease of use and streamlining for sake of functionality.<br>

2. Edit and Deletion of Reviews on Products.<br>
    Due to trying to streamline the comment functionality rather than using a similar structure to how products and blog posts are edited and delted the reviews are currently immutable without access through the Admin panel.<br>
    Will require a way to access the UserProfile successfully or sacrifice ease of use and streamlining for sake of functionality.<br>. <br>

# Testing

|TEST|PROCESS|EXPECTATION|RESULT|
| -- | -- | -- | -- |
| What was tested? | How was it tested? | What was the expected outcome? | Success or Failure? |
|  |  |  |  |
| Does the site navigation function? | Using the nav links | Successful navigation to the various site pages | SUCCESS |
| Can an Admin add a new product through the UI? | Successful addition of new products | Attempting to use the add product form | SUCCESS |
| Can an Admin edit a product through the UI? | Attempting to access and edit the product form for a specific product | Successful update of product | SUCCESS |
| Can an Admin delete a product through the UI? | Attempting to delete a product with a delete button | Removal of product from the database | SUCCESS |
| Does the site display a list of products? | Accessing the relevant view | Proper display of every product | SUCCESS |
| Does the site allow search functionality? | Using the search bar | Display of relevant products for the search query | SUCCESS |
| Does the site allow product filtering? | Using the filters to filter products | Display of relevant products for the selected filters | SUCCESS |
| Does the site allow a detailed view of a specific product? | Accessing the product_detail view | Successful display of product details | SUCCESS |
| Can a user post a review for a product? | Attempting to use review form for a product | Successful addition of review to database and linked to product | SUCCESS - requires restructure of how it accesses UserProfile |
| Can a user edit a review? | Attempting to use an edit button | Successful access to review form to edit existing content | FAIL - Requires restructure of how it accesses UserProfile or using views similar to product and blog |
| Can a user edit other user reviews? | Attempting to use an edit button | Unable to access review content without auth | FAIL - Requires restructure of how it accesses UserProfile or using views similar to product and blog |
| Can a user delete a review? | Attempting to use a delete button | Successful deletion of review | FAIL - Requires restructure of how it accesses UserProfile or using views similar to product and blog |
| Can a user delete other user reviews? | Attempting to use a delete button | Unable to delete review without auth | FAIL - Requires restructure of how it accesses UserProfile or using views similar to product and blog |
| Does the site display a list of blog posts? | Accessing the relevant view to see blog posts | Successful display of all blog posts | SUCCESS |
| Does the user allow a view of a specific blog post? | Accessing the relevant view for a specific blog post | Successful display of a specific blog post | SUCCESS |
| Can an Admin create a new Blog Post through the UI? | Attempting to use the UI to add a new Blog Post | Successful addition of blog post to database and site | SUCCESS |
| Can an Admin edit a Blog Post through the UI? | Attempting to use the UI to edit a new Blog Post | Successful update of blog post on database and site | SUCCESS |
| Can an Admin delete a Blog Post through the UI? | Attempting to use the UI to delete a new Blog Post | Successful removal of blog post from database and site | SUCCESS |
| Can a user post a comment to a Blog Post? | Using the provided form to add a comment | Successful addition of a comment to the database and blog post | SUCCESS  - requires restructure of how it accesses UserProfile |
| Can a user edit a comment? | Attempting to use an edit button | Successful access to comment form to edit existing content | FAIL - Requires restructure of how it accesses UserProfile or using views similar to product and blog |
| Can a user delete a comment? | Attempting to use a delete button | Successful deletion of comment | FAIL - Requires restructure of how it accesses UserProfile or using views similar to product and blog |
| Can a user edit another user's comment? | Attempting to use an edit button | Unable to edit comment without auth | FAIL - Requires restructure of how it accesses UserProfile or using views similar to product and blog |
| Can a user delete another user's comment? | Attempting to use a delete button | Unable to delete comment without auth | FAIL - Requires restructure of how it accesses UserProfile or using views similar to product and blog |
| Does the cart display correctly? | Accessing the Cart view | Cart details will correctly display | SUCCESS |
| Can products be successfully added to the cart? | Using a product detail view to add to the cart | Successfully adding products to the cart | SUCCESS |
| Can incorrect values be added to the cart? | Testing if 0, negative, or over 99 items can be added to cart | Unable to add such values to cart | SUCCESS |
| Do prices correctly update in the cart? | Adding multiple items to cart | Total for checkout will update correctly | SUCCESS |
| Do product amounts correctly display in the cart? | Adding multiple of same item to cart | Quantity will update successfully | SUCCESS |
| Can the cart be altered in the cart view? | Using the cart to change quantity of items | Quantity and total will successfully update | SUCCESS |
| Does shipping correctly calculate? | Adding multiple items and observing change of shipping cost | Shipping cost will be 10% of overall total | SUCCESS |
| Does the shipping threshold get assigned correctly? | Adding over the required total to test shipping threshold discount | Shipping will be 0 if total is over 50 | SUCCESS |
| Can users create profiles? | Using the requisite form to create a new profile | Successful creation of new profiles | SUCCESS |
| Can users update their profiles? | Accessing the profile form on the profile page | Successful update of profile details | SUCCESS |
| Can users successfully checkout? | Going through the checkout process | Successful completion of checkout | SUCCESS |
| Does the site display alerts correctly? | Performing various tasks to proc messages | Successful display of messages | SUCCESS |
| Does the profile show order history? | Checking the profile page after making an order | Successful display of order details | SUCCESS |
| Do Stripe Webhooks function correctly? | Checking the stripe account to view webhooks | Successful | SUCCESS |
| Does Stripe correctly process transactions? | Checking the stripe account to view completed transactions | Successful completion of transactions | SUCCESS |
| Can a user subscribe with their email? | Using form to subscribe to the site | Successful subscribe after providing email | SUCCESS |
| Can a user subscribe with a fake email? | Using form to subscribe to the site | Unable to subscribe | SUCCESS |
| Do user emails get added to mailchimp list? | Checking mailchimp after subscriptions | Users added to mailchimp list | SUCCESS |

## Bugs

1. Unable to edit or delete comments on blog posts through the UI due to incorrect accessing of UserProfile.
2. Display of names on comments defaults to None due to above issue.
3. Unable to edit or delete reviews on products through the UI due to incorrect accessing of UserProfile.
4. Display of names on reviews defaults to None due to above issue.

# Deployment

This app will be deployed through Heroku by being linked to the Github repository.
In order to deploy the site:

1. I created the app in the Heroku Dashboard.
2. I modified the Config Vars of the app to restrict the collection of static data.
3. I installed gunicorn.
4. I created a procfile to instruct heroku on which file to run.
5. I added heroku as an allowed host in settings.py.
6. I disabled DEBUG unless the environment is seen as Developer.
7. I linked the heroku app to my GitHub repo.
8. I clicked Deploy Branch.

The live link can be found here - https://pp5-coders-cards-5ec2dbb6a777.herokuapp.com/

# AWS Bucket

I had errors with my Aws Account and lost access to it before being able to upload the media folder.

# Stripe Webhook Successes

![Initial trigger of stripe webhook succeeding](README-images\stripe-webhook-trigger-success.PNG)<br>

![Stripe developer console webhook successes](README-images\stripe-webhook-success.PNG)<br>

# SEO

A sitemap.xml file and robots.txt file were created for this project.

## Web marketing

A fake facebook page was mocked up using the templates provided by CodeInstitute.
The faked site can be accessed using the main navigation bar on the site.
![Faked Facebook Page](media\coders_cards_facebook_page.png)<br>

A rel link to Dublin ComicCon (https://dublincomiccon.com/wcs-type/gaming-tcg-gaming-dd/) was created to establish a relationship between this website and them as they host TCG tournaments.

# E-Commerce Business Model

## Keywords:
### Short-Tail
-----------
Coder Gifts<br>
Coder Games<br>
Developer Collectibles<br>
Developer TCG<br>
Dublin Card Shops<br>
Developer Hangout Dublin<br>

### Long-Tail
-----------
Trading Card Games for Coding<br>
Board Games for Coders<br>
Tapletop Games for Coders<br>
Buy games for coders<br>
Gifts for web developers<br>
Where can developers play cards in Ireland<br>
Developer games in Ireland<br>
Where to order developer gifts<br>
Coding TCG Tournaments in Dublin<br>

## Organic Social Media Marketing

I felt the best way to promote a TCG card shop would be through the use of organic marketing, utilising social media as the primary draw.<br>
Posting regular content of new products, events, tournaments, and getting influencers to play games or do card pack openings at the store would help boost visibility and draw in new customers.<br>
In addition, with Dublin ComicCon being a host for Card Game Tournaments creating such content surrounding big events like that would facilitate more exposure and growth as well for an up and coming company who may not have much capital to work with.

## Email Marketing

A signup form for digital marketing was created using mailchimp.<br>
I signed up to their free 2 week trial in order to use their service.<br>
I implemented their version of an embedded form into the profile page.<br>
This will allow the site to keep subscribers up to date on new products, deals, events, and any other enticing information that may be relevant to boosting the shop's community.<br>
![Mailchimp Subscriber Email List](README-images\mailchimp-subscribe-success.PNG)<br>

# Credits
The project was largely built upon the foundation laid by the Boutique Ado project provided by CodeInstitute.

Homepage image source:
https://www.threeforonetrading.com/en/new-magic-store-vienna - https://h5m3s5t5.delivery.rocketcdn.me/wp-content/uploads/2022/06/341-Store-Impressions-23.jpg

Slugify fields in forms:
https://stackoverflow.com/questions/70601191/how-to-auto-populate-slug-field-in-django-forms