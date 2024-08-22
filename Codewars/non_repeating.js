function firstNonRepeatingLetter(string) {
    const lowerString = string.toLowerCase();
    for (let index = 0; index < lowerString.length; index++) {
        const char = lowerString[index];
        if (lowerString.split(char).length - 1 === 1) {
            return string[index];
        }
    }
    return '';
}
