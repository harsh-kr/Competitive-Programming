# Angry Professor

A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, he decides to cancel class if fewer than some number of students are present
when class starts. Arrival times go from on time (arrivalTime<=0) to arrived late (arrivalTime>0).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is canceled.

The first line of input contains t, the number of test cases.

Each test case consists of two lines.

The first line has two space-separated integers, n and k, the number of students (size of a) and the cancellation threshold.
The second line contains n space-separated integers (a[1], a[2], ..., a[n]) describing the arrival times for each student.

Note: Non-positive arrival times (a[i]<=0) indicate the student arrived early or on time; positive arrival times (a[i]>0) indicate the student arrived a[i] minutes late.

The function angryProfessor has the following parameter(s):

* k: the threshold number of students
* a: an array of integers representing arrival times

<br/>

![Angry](https://st.depositphotos.com/1007168/3030/i/450/depositphotos_30306303-stock-photo-funny-professor-holding-a-pointer.jpg)
