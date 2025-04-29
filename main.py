< !DOCTYPE
html >
< html
lang = "en" >
< head >
< meta
charset = "UTF-8" / >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1" / >
< title > Transformers - Physics
Project < / title >
< style >
*{
    margin: 0;
padding: 0;
box - sizing: border - box;
}

body
{
    font - family: 'Poppins', sans - serif;
background - color:  # e3f2fd;
color:  # 333;
display: flex;
}

.sidebar
{
    background - color:  # 2196f3;
        color: white;
width: 220
px;
padding: 30
px
20
px;
display: flex;
flex - direction: column;
gap: 20
px;
position: fixed;
height: 100 %;
}

.sidebar
h2
{
    font - size: 24px;
}

.sidebar
ul
{
    list - style: none;
}

.sidebar
ul
li
{
    margin: 15px 0;
}

.sidebar
ul
li
a
{
    color: white;
text - decoration: none;
font - size: 18
px;
padding: 8
px
12
px;
border - radius: 6
px;
display: block;
transition: background
0.3
s;
}

.sidebar
ul
li
a: hover
{
    background - color:  # 64b5f6;
}

.main - content
{
    margin - left: 240px;
padding: 40
px;
}

.section
{
    scroll - margin - top: 80px;
margin - bottom: 60
px;
}

.section
h1
{
    font - size: 36px;
color:  # 1565c0;
margin - bottom: 20
px;
}

.section
p
{
    font - size: 20px;
line - height: 1.6;
max - width: 800
px;
margin - bottom: 20
px;
}

# audioButton {
background - color:  # 42a5f5;
border: none;
color: white;
padding: 12
px
24
px;
font - size: 18
px;
border - radius: 8
px;
cursor: pointer;
transition: background - color
0.3
s, transform
0.2
s;
}

# audioButton:hover {
background - color:  # 1e88e5;
transform: scale(1.05);
}

.quiz - question
{
    margin - bottom: 20px;
}

.quiz - question
h3
{
    font - size: 22px;
margin - bottom: 10
px;
}

.quiz - option
{
    margin - bottom: 5px;
font - size: 18
px;
}

@media(max - width

: 768
px) {
    body
{
flex - direction: column;
}

.sidebar
{
width: 100 %;
flex - direction: row;
overflow - x: auto;
height: auto;
position: static;
}

.main - content
{
margin - left: 0;
padding: 20
px;
}

.sidebar
h2
{
display: none;
}

.sidebar
ul
{
display: flex;
gap: 15
px;
}
}
< / style >
    < / head >
        < body >
        < nav


class ="sidebar" >

< h2 > Menu < / h2 >
< ul >
< li > < a
href = "#introduction" > Introduction < / a > < / li >
< li > < a
href = "#detailed" > Explanation < / a > < / li >
< li > < a
href = "#quiz" > Quiz < / a > < / li >
< li > < a
href = "#transformer-3d-model" > 3
D
Model < / a > < / li >
< li > < a
href = "#certificate" > Certificate < / a > < / li >

< / ul >
< / nav >

< main


class ="main-content" >

< section
id = "introduction"


class ="section" >

< h1 > Welcome
to
Transformers! < / h1 >
< p > In
this
website, you
will
find
an
explanation
of
transformers
using
images, videos, and quizzes.At
the
end, you
'll earn a certificate for mastering the topic!</p>
< p > A
transformer is a
device
that
transfers
electric
energy
from one alternating

-current
circuit
to
another, either
increasing or decreasing
the
voltage. < / p >

< button
id = "audioButton"
onclick = "document.getElementById('introAudio').play()" >🔊 Play
Audio < / button >
< audio
id = "introAudio" >
< source
src = "audio/transformer-intro.mp3"
type = "audio/mpeg" / >
Your
browser
does
not support
the
audio
element.
< / audio >

< div
style = "text-align: center; margin-top: 30px;" >
< img
src = "http://hyperphysics.phy-astr.gsu.edu/hbase/magnetic/imgmag/transf.png"
alt = "Transformer Diagram"
width = "500" / >
< / div >
< / section >

< section
id = "detailed"


class ="section" >

< h1 > Explanation < / h1 >
< p > Transformers
work
on
the
principle
of < strong > electromagnetic
induction < / strong >.When
AC
passes
through
the
primary
coil, it
generates
a
changing
magnetic
field
that
induces
voltage in the
secondary
coil. < / p >
< div
style = "text-align: center; margin: 30px 0;" >
< iframe
width = "560"
height = "315"
src = "https://www.youtube.com/embed/9K4x3WCvKNI"
title = "How Transformers Work"
frameborder = "0"
allowfullscreen > < / iframe >
< / div >
< p > Transformers
are
essential in our
daily
lives,
from phone chargers

to
power
stations.They
help
make
electricity
safe and efficient
to
use
over
long
distances. < / p >
< / section >

< section
id = "quiz"


class ="section" >

< h1 > Quiz
Time! 🚀 < / h1 >
< p
style = "font-size: 18px;" > Test
your
knowledge
about
transformers
below! < / p >

< form
id = "quizForm"
style = "background-color: #bbdefb; padding: 25px; border-radius: 12px; max-width: 800px; margin: 0 auto;" >
< div


class ="quiz-question" >

< h3 >🔌 1.
What
does
a
transformer
do? < / h3 >
< label


class ="quiz-option" > < input type="radio" name="q1" value="a" / > Generates electricity < / label > < br / >

< label


class ="quiz-option" > < input type="radio" name="q1" value="b" / > Changes voltage levels < / label > < br / >

< label


class ="quiz-option" > < input type="radio" name="q1" value="c" / > Stores electric charge < / label >

< / div >

< div


class ="quiz-question" >

< h3 >🔁 2.
What
principle
do
transformers
work
on? < / h3 >
< label


class ="quiz-option" > < input type="radio" name="q2" value="a" / > Static electricity < / label > < br / >

< label


class ="quiz-option" > < input type="radio" name="q2" value="b" / > Electromagnetic induction < / label > < br / >

< label


class ="quiz-option" > < input type="radio" name="q2" value="c" / > Chemical reaction < / label >

< / div >

< div


class ="quiz-question" >

< h3 >⚡ 3.
What
type of current
do
transformers
use? < / h3 >
< label


class ="quiz-option" > < input type="radio" name="q3" value="a" / > Direct current (DC) < / label > < br / >

< label


class ="quiz-option" > < input type="radio" name="q3" value="b" / > Alternating current (AC) < / label > < br / >

< label


class ="quiz-option" > < input type="radio" name="q3" value="c" / > Both < / label >

< / div >

< div


class ="quiz-question" >

< h3 >🌀 4.
What is the
main
component
that
links
primary and secondary
coils? < / h3 >
< label


class ="quiz-option" > < input type="radio" name="q4" value="a" / > Plastic tube < / label > < br / >

< label


class ="quiz-option" > < input type="radio" name="q4" value="b" / > Magnetic core < / label > < br / >

< label


class ="quiz-option" > < input type="radio" name="q4" value="c" / > Battery < / label >

< / div >

< div


class ="quiz-question" >

< h3 >🔋 5.
Which
type of transformer
increases
voltage? < / h3 >
< label


class ="quiz-option" > < input type="radio" name="q5" value="a" / > Step-down transformer < / label > < br / >

< label


class ="quiz-option" > < input type="radio" name="q5" value="b" / > Step-up transformer < / label > < br / >

< label


class ="quiz-option" > < input type="radio" name="q5" value="c" / > Equalizer < / label >

< / div >

< div
style = "text-align: center; margin-top: 20px;" >
< button
type = "button"
onclick = "checkAnswers()"
id = "audioButton" > Check
My
Score < / button >
< / div >
< / form >

< div
id = "quizResult"
style = "margin-top: 20px; font-size: 22px; font-weight: bold; color: #1565c0; text-align: center;" > < / div >
< / section >

< section
id = "transformer-3d-model"


class ="section" >

< h1 > Explore
the
Transformer in 3
D 🔍 < / h1 >
< p
style = "font-size: 18px;" > Take
a
closer
look
at
a
3
D
model
of
a
transformer and see
how
it
works in action! < / p >

< div
style = "text-align: center;" >
< iframe
width = "800"
height = "600"
src = "https://sketchfab.com/models/9e7076096b0346dfbbc729f75f1b41be/embed"
frameborder = "0"
allowfullscreen > < / iframe >
< / div >

< p
style = "font-size: 18px; margin-top: 20px;" > You
can
interact
with the model, rotate it, and zoom in to explore its components.This will give you a better understanding of how transformers work in real life! < / p >
< / section >

< !DOCTYPE
html >
< html
lang = "en" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > Certificate
Generator < / title >
< script
src = "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.4.1/html2canvas.min.js" > < / script >
< style >
body
{
    font - family: 'Roboto Slab', serif;
background - color:  # f4f6f7;
}
# certificate {
padding: 50
px;
text - align: center;
background - color:  # ffffff;
box - shadow: 0
px
5
px
20
px
rgba(0, 0, 0, 0.1);
border - radius: 12
px;
width: 80 %;
max - width: 800
px;
margin: 30
px
auto;
}

.certificatePreview
{
background - color:  # f9fbe7;
border: 2
px
solid  # 1e88e5;
border - radius: 15
px;
padding: 30
px;
margin - top: 30
px;
}

input
{
font - family: 'Georgia', serif;
padding: 10
px
15
px;
width: 70 %;
max - width: 500
px;
font - size: 20
px;
text - align: center;
border: 2
px
solid  # 1e88e5;
border - radius: 10
px;
background - color:  # f4f6f7;
margin - top: 15
px;
}

button: hover
{
background - color:  # 1e88e5;
transform: scale(1.05);
}

button
{
font - size: 18
px;
padding: 12
px
24
px;
background - color:  # 42a5f5;
border: none;
color: white;
font - family: 'Georgia', serif;
border - radius: 8
px;
cursor: pointer;
transition: background - color
0.3
s;
}
< / style >
    < / head >
        < body >

        < section
id = "certificate"


class ="section" >

< h1
style = "text-align: center; font-family: 'Roboto Slab', serif; font-size: 36px; color: #1e88e5;" >🎓 Congratulations, Master
of
Transformers! 🎓 < / h1 >
< p
style = "text-align: center; font-size: 20px; font-family: 'Georgia', serif; color: #2c3e50;" > You
have
successfully
completed
the
Transformers
Physics
lesson
with outstanding performance! Your knowledge has been tested, and you have excelled.< / p >
< p
style = "text-align: center; font-size: 22px; font-family: 'Georgia', serif; color: #2c3e50;" >🌟 You
're officially a Transformer Expert! 🌟</p>

< div
style = "width: 100%; text-align: center; margin-top: 30px;" >
< h2
style = "font-size: 28px; font-family: 'Georgia', serif; color: #1e88e5;" > Certificate
of
Achievement < / h2 >
< p
style = "font-size: 18px; font-family: 'Georgia', serif; color: #2c3e50;" > This is to
certify
that < / p >

< !-- Input
for Name -->
< input
id = "nameInput"
type = "text"
placeholder = "Enter Your Name"
style = "font-size: 22px; padding: 10px 15px; width: 60%; max-width: 400px; border: 2px solid #1e88e5; border-radius: 8px; margin-top: 15px; text-align: center; color: #2c3e50; font-family: 'Georgia', serif;" / >

< p
style = "font-size: 18px; font-family: 'Georgia', serif; color: #2c3e50; margin-top: 20px;" > Has
completed
the
lesson
on
Transformers
Physics
with mastery. </ p >
< p
style = "font-size: 20px; font-family: 'Georgia', serif; color: #1e88e5;" > Mastery
Level: < span
id = "level"
style = "font-weight: bold; color: #e74c3c;" > Excellent < / span > < / p >

< !-- Current
Date
Display -->
< p
style = "font-size: 18px; font-family: 'Georgia', serif; color: #2c3e50; margin-top: 10px;" > Date: < span
id = "currentDate"
style = "font-weight: bold;" > < / span > < / p >

< !-- Certificate
Preview -->
< div
id = "certificatePreview"


class ="certificatePreview" >

< h2
style = "font-size: 36px; font-family: 'Georgia', serif; color: #1e88e5;" > Certificate
of
Achievement < / h2 >
< p
style = "font-size: 24px; font-family: 'Georgia', serif; color: #2c3e50;" > This
certifies
that < span
id = "studentName"
style = "font-weight: bold; color: #e74c3c;" > [Student Name] < / span > < / p >
< p
style = "font-size: 20px; font-family: 'Georgia', serif; color: #2c3e50;" > Has
successfully
completed
the
lesson
on
Transformers
Physics < / p >
< p
style = "font-size: 22px; font-family: 'Georgia', serif; color: #1e88e5;" > Mastery
Level: Excellent < / p >
< p
style = "font-size: 18px; font-family: 'Georgia', serif; color: #2c3e50;" > Date: < span
id = "certificateDate"
style = "font-weight: bold;" > [Date] < / span > < / p >
< / div >

< div
style = "margin-top: 30px;" >
< button
onclick = "generateCertificate()" > Download
Your
Certificate < / button >
< / div >
< / div >
< / section >

< script >
// Function
to
display
the
current
date
const
currentDate = new
Date().toLocaleDateString();
document.getElementById('currentDate').textContent = currentDate;
document.getElementById('certificateDate').textContent = currentDate;

// Function
to
update
the
certificate
preview
with the entered name
function
updateCertificatePreview()
{
    const
name = document.getElementById('nameInput').value;
document.getElementById('studentName').textContent = name | | "[Student Name]";
}

// Event
listener
for name input to update preview
document.getElementById('nameInput').addEventListener('input', updateCertificatePreview);

// Function
to
generate and download
the
certificate
function
generateCertificate()
{
    html2canvas(document.getElementById('certificatePreview')).then(function(canvas)
{
// Convert
canvas
to
data
URL
const
dataURL = canvas.toDataURL('image/png');

// Create
a
temporary
link
element
to
trigger
the
download
const
link = document.createElement('a');
link.href = dataURL;
link.download = 'certificate_of_achievement.png';
link.click();
});

< / script >

    < / body >
        < / html >

            < script >

            < / script >
                < / body >
                    < / html >
