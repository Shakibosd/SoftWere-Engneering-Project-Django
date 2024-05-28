
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter Any Year : ', (input) => {
    const year = parseInt(input);

    if (year % 400 === 0) {
        console.log('Leap Year');
    }
    else if (year % 4 === 0 && year % 100 !== 0) {
        console.log('Leap Year');
    } 
    else {
        console.log('Not Leap Year');
    }
    rl.close();
});
