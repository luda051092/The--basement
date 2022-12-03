ES5 
/** Write an ES2015 Version */
function createInstructor(firstName, lastName){
    return {
        firstName: firstName,
        lastName: lastName
    }
}
/** ES2015 Version */
function createInstructor(firstName, lastName){
    return {
        firstName, 
        lastName
    }
}

Computed Property Names: 
/** Write an ES2015 Version */
var favoriteNumber = 42;

var instructor = {
    firstName: "Colt"
}

instructor[favoriteNumber] = "That is my favorite!"

ES2015 Version:
let favoriteNumber = 42;

const instructor = {
    firstName: "Colt",
    [favoriteNumber]: "That is my favorite!"
}

Object Methods: 
/** Write an ES2015 version */
var instructor = {
    firstName: "Colt", 
    sayHi: function(){
        return "Hi!";
    },
    sayBye: function(){
        return this.firstName " + "says bye!";

    }
}

/**ES2015 Version */
const instructor = {
    firstName: "Colt", 
    sayHi(){
        return "Hi!";
    },
    sayBye(){
        return this.firstName + " says bye!";
    }
}

createAnimal function:
Write a function which generates an animal object. The function should accepts 3 arguments:

species: the species of animal (‘cat’, ‘dog’)
verb: a string used to name a function (‘bark’, ‘bleet’)
noise: a string to be printed when above function is called (‘woof’, ‘baaa’)
const d = createAnimal("dog", "bark", "Woooof!")
// {species: "dog", bark: f}
d.bark() //"Woooof!"

const s = createAnimal("sheep", "bleet", "BAAAAaaaa")
//{species: "sheep", bleet: f }
s.bleet() //"BAAAAaaaa"

function createAnimal(species, verb, noise){
    return {
        species, 
        [verb](){
            return noise;
        }
    }
}








































