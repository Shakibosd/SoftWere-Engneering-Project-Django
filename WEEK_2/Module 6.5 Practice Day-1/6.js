
var friends = ["rahim", "karim", "abdul", "sadsd", "heroAlommm"];

function longestName(names) {
    return names.reduce((longest, current) => current.length > longest.length ? current : longest, '');
}

console.log(longestName(friends)); 
