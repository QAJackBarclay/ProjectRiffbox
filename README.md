# ProjectRiffbox

Welcome to Project Riffbox, my first ever project created using the training I have learned over the past four weeks.

In this project, my intention is to create a website that a user can visit to find new music, the final product should take the users requested genre and display a list of five songs for them to listen to.

## Project Planning and Managment

The original project had planned to have multiple features, from selecting three genres of music and displaying the youtube links embedded into the html
but with time constraints and scheduling issues, along with a lack of experience resulted in me also having to cut features and replan accordingly.

To deal with this, the functionality was stripped back further to a basic concept so that I could complete the Project in the alloted timeframe whilst also
attempting to complete as much work as possible.

I created a Trello board to help keep track of my ongoing work.
<img src="https://github.com/QAJackBarclay/ProjectRiffbox/blob/4104427fa4154732d32730bb05e036be386bee28/application/Images/Trello%201.PNG" alt="Alt text" title="Optional title">


## Risk Assesment 

The biggest risk for Project Riffbox was being unable to deliver anything for the user to see or interact with, which was the priority heading into the Project extension week as the delay of a week in between starting the Project and then having to pick up where I left off forced me to make some major decisions to avoid this risk. 

The second biggest risk was delivering an application that didn't fit the parameters or reach the deployment phase due to this, although some features are not yet implemented the foundation work has been done to add these features at a later time.

The risk of hackers or unwarranted users in the database by accessing the network past the firewall. 

There is a risk that the youtube links lead to no video as they could have been taken down. 

The least important risk is that the user did not enjoy the music provided by Riffbox.


## The Application

I was able to create all the desirable html pages, along with the main function of the website complete with hyperlinks and 
navbar that all lead to their respective pages. 

I uploaded images to github to host them so that they could be displayed on the webpages for the user to see, along with this I managed to create a database of music that the user can see by selecting the appropriate genre.

There was initially meant to be a random playlist generator feature that would take three genres selected by the user and display five links selected from the database at random but due to time constraints this was cut.

<img src="https://github.com/QAJackBarclay/ProjectRiffbox/blob/4104427fa4154732d32730bb05e036be386bee28/application/Images/Riffbox.PNG" alt="Alt text" title="Optional title">
<img src="https://github.com/QAJackBarclay/ProjectRiffbox/blob/4104427fa4154732d32730bb05e036be386bee28/application/Images/Riffbox.PNG" alt="Alt text" title="Optional title">
<img src="https://github.com/QAJackBarclay/ProjectRiffbox/blob/4104427fa4154732d32730bb05e036be386bee28/application/Images/Riffbox%20Results.PNG" alt="Alt text" title="Optional title">

## Testing
Covered 91% of testing after deploying through Jenkins.
<img src="https://github.com/QAJackBarclay/ProjectRiffbox/blob/347e523d41db1dad3be26703cde4f928db628a39/application/Images/Jenkins%20test.PNG" alt="Alt text" title="Optional title">

## User Story
The user should be able to go onto the website, submit any name they want into the submit box. Once they have done so it will redirect them to the input page
where they can select which genre of music they would like to hear some music from, after they select the genre and submit, it will then take them to the results page, where it will display the names and youtube links of five songs from that style of music.
<img src="https://github.com/QAJackBarclay/ProjectRiffbox/blob/4104427fa4154732d32730bb05e036be386bee28/application/Images/Riffbox%20Index.PNG" alt="Alt text" title="Optional title">

## Known Issues 

Due to my lack of experience with coding other than this training course I had to scale back some of my larger ambitions such as selecting three genres and having a random selection of five songs be delivered to the user.

After Project weeks time was cut short and then restarted two weeks later, the project is now focussed primarly of getting to a working state so that it can be improved upon in time and after I learn more from the course.

## Final Notes

I am happy with how the Project turned out considering all the issues that where faced over the past three weeks, as someone with no prior experience to coding 
other than this training course I think it shows potential if I was given proper time and attention to learn and practice correctly. 

With an entire week gap in between coding and soft skills development, my information retention has been put properly to the test and I also have to thank my amazing cohort for their support and dedication to keeping everyone working together.


## Developer Diary and notes
Welcome to the readme of Project Riffbox! 

This will be my first ever project to display as much as I have learned over the past four weeks in training.

My intention is to create a website that users can find music to listen to from a variety of genres that they choose! 

I created 5 html pages to create the webpage that will host my project, currently the only webpage with user input functions is input.html,
also I am also in the process of creating hyperlinks which connect all of the pages together for easy viewing.

Set up all of the app.routes for each html and some basic text and titles on the pages to provide the website something to load, the home button that redirects
to the instructions page currently doesn't work and the jpg is not loading.

Managed to get all hyperlinks working and redirecting to the appropraite pages, along with this, all select fields and buttons also now work and redirect to the correct pages. 

Built the database of youtube links each seperated into their respective genre databases.

Now I need to build a function that takes the three selected genres, and displays the links requested.

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

16.06.2022
Tried to refactor code to add the users name in the result page so that it would display their name and the playlist but I was advised this would take too long
and I should also cut this feature for now.

Exported coverage to a .xml

Refined html and code as best as I could before pushing to main. 

Set up Jenkins and a systemctl file for deployment

Set up firewall and parameters 

got test coverage up to 91% out of 95% target

Jenkins fully deploys

Final push now going to GitHub for presentation.
