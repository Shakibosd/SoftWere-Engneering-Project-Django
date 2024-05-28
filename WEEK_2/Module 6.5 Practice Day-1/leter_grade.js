
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter Student Mark : ", function (marks) {
    marks = parseInt(marks);

    if (marks < 0 || marks > 100 || isNaN(marks)) {
        console.log("Invalid Marks");
        rl.close();
        return;
    }

    let grade;

    if (marks >= 80 && marks <= 100) {
        grade = 'A+';
    }
    else if (marks >= 70 && marks < 80) {
        grade = 'A';
    }
    else if (marks >= 60 && marks < 70) {
        grade = 'A-';
    }
    else if (marks >= 50 && marks < 60) {
        grade = 'B';
    }
    else if (marks >= 40 && marks < 50) {
        grade = 'C';
    }
    else if (marks >= 33 && marks < 40) {
        grade = 'D';
    }
    else {
        grade = 'F';
    }

    console.log("Student Grade = " + grade);
    rl.close();
});
