# Coders Cards
This is a DJango-based e-commerce website for a fictional Trading Card Game (TCG) for programmers and coders.

# Five UX Planes

# Site Presentation
The site adapts to various screen sizes as shown by this image from amiresponsive
![image of site responsiveness]()

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

1. Example.<br>
    Explanation.<br>

2. Example.<br>
    Explanation. <br>

# Testing

|TEST|PROCESS|EXPECTATION|RESULT|
| -- | -- | -- | -- |
| What was tested? | How was it tested? | What was the expected outcome? | Success or Failure? |
| -- | -- | -- | -- |
| -- | -- | -- | -- |
| -- | -- | -- | -- |

# Validating

All functional code has been run through various linters and validators to ensure it is compliant with current web standards.

## Python
The [] file was fully checked in the CI Python Linter and returned no errors.<br>
![python file validation example]()<br>

## HTML
The [] page was fully HTML Valid.<br>
![Example Page Validation]()<br>

## CSS
The CSS file was checked using W3C CSS File Validator.
![CSS Validation]()

## JavaScript
The [] script validation.<br>
![Example Validation]()<br>

# Bugs

Currently no bugs.

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

I felt the best way to promote a TCG card shop would be through the use of organic marketing, utilising social media as the primary draw.
Posting regular content of new products, events, tournaments, and getting influencers to play games or do card pack openings at the store would help boost visibility and draw in new customers.
IN addition, with Dublin ComicCon being a host for Card Game Tournaments creating such content surrounding big events like that would facilitate more exposure and growth as well for an up and coming company who may not have much capital to work with.

## Email Marketing

A signup form for digital marketing was created using mailchimp.
I signed up to their free 2 week trial in order to use their service.
I implemented their version of an embedded form into the profile page.
This will allow the site to keep subscribers up to date on new products, deals, events, and any other enticing information that may be relevant to boosting the shop's community.

# Credits
The project was largely built upon the foundation laid by the Boutique Ado project provided by CodeInstitute.

Homepage image source:
https://www.threeforonetrading.com/en/new-magic-store-vienna - https://h5m3s5t5.delivery.rocketcdn.me/wp-content/uploads/2022/06/341-Store-Impressions-23.jpg