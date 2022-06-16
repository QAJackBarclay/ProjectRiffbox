# ProjectRiffbox

Welcome to Project Riffbox, my first ever project created using the training I have learned over the past four weeks.

In this project, my intention is to create a website that a user can visit to find new music, the final product should take the users requested genre and display a list of five songs for them to listen to.

## Project Planning and Managment

The original project had been planned to have multiple features, from selected three genres of music and it displaying the youtube links embedded into the html
but with time constraints and scheduling issues within the business, the Project week was cut short and had to be restarted at a later date.

To deal with this, the functionality was stripped back further to a basic concept so that I could complete the Project in the alloted timeframe whilst also
attempting to complete as much work as possible.

<img src="https://github.com/QAJackBarclay/ProjectRiffbox/blob/4104427fa4154732d32730bb05e036be386bee28/application/Images/Trello%201.PNG" alt="Alt text" title="Optional title">


I created a Trello board to help keep track of my ongoing work.

## Risk Assesment 
The biggest risks: 
Unable to complete Project on time 
Unable to deliver a functioning website
Website does not load
Functions do not work
Links do not work

The smaller risks:
Extra features not added


## The Application

I was able to create all the desirable html pages, along with the main function of the website complete with hyperlinks and 
a working navbar.

## Testing
Managed to keep testing above 75% as I tested the core function and response times of each webpage.

## User Story
The user should be able to go onto the website, submit any name they want into the submit box. Once they have done so it will redirect them to another page
where they can select which genre of music they would like to see some music from, after they select the genre and submit the field it will then take them to the final page, where it will display the names and youtube links to the songs.

## Known Issues 

Due to my lack of experience with coding other than this training course I had to scale back some of my larger ambitions such as selecting three genres and having a random selection of five songs be delivered to the user.

After Project weeks time was cut short and then restarted two weeks later, the project is now focussed primarly of getting to a working state so that it can be improved upon in time and after I learn more from the course.

## Final Notes

I am unhappy with how the project turned out, I believe I can do much better in the future.


## Developer Diary and notes
Welcome to the readme of Project Riffbox! 

This will be my first ever project to display as much as I have learned over the past four weeks in training.

My intention is to create a website that users can find music to listen to from a variety of genres that they choose! 

I created 5 html pages to create the webpage that will host my project, currently the only webpage with user input functions is input.html,
also I am also in the process of creating hyperlinks which connect all of the pages together for easy viewing.

Set up all of the app.routes for each html and some basic text and titles on the pages to provide the website something to load, the home button that redirects
to the instructions page currently doesn't work and the jpg is not loading.

Created a navbar with three functioning links to other html pages.

The navbar is now working but when I run app.py, it does not load up the home.html or any others and I need to manually add /home to enter the website etc.

I resolved the issue and now the website opens as expected, I will now tidy up the files and ensure that everything still links.


Created  routes.py, create.py, license.md files in main directory.

Created Application folder, Images and Templates folders where moved into this directory.

Cleaned up app.py and moved code into their proper files, and linked everything together. 

Testing the website resulted in everything currently added functioning as expected minus the JPG image for the home page. 

Hyperlink 2 in instructions currently does not work as the function for Input has not yet been created.

Created dev branch to push everything to GitHub, then once I am happy push everything to the main branch.

Updated the Index to describe the available genres, inputted a quote for myself along with some html practice on seperating information.

Created the forms.py file and managed to get the Input webpage working with some stringfields although they do not register anything yet.

Managed to get all hyperlinks working and redirecting to the appropraite pages, along with this, all select fields and buttons also now work and redirect to the correct pages. 

Built the database of youtube links each seperated into their respective genre databases.

Now I need to build a function that takes the three selected genres, and displays the music requested.

Also need to build a delete function which I am think of creating two buttons, one thumbs up and one thumbs down for easy save/delete.




14.06.2022
After our Project faced an unavoidable delay when we had our Project week cut short by two days, followed by an entire week in London where we met the team in person.

Did not have SQL Workbench set up properly 
Was working onn a VM and not local to see what tables look like in SQL due to VM

15.06.2022
The forms on input.html did not have any functionality behind them and I spent the majority of the morning and afternoon setting up the relationships between 
html pages, databases and forms and troubleshooting form queries.

After discussing with others and the trainer, I have decided to scale back the project to meet the deadline by changing it to be a single dropdown box that you can
select a genre, it will then display from that genre some songs! 

I may add an update and delete function if I have enough time.
