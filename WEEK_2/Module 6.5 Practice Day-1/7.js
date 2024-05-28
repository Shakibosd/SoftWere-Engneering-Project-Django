
var duplicateRemove = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 10];

function removeDuplicates(arr) {
    return [...new Set(arr)];
}

console.log(removeDuplicates(duplicateRemove));
