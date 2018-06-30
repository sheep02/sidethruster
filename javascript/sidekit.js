DOC = document;
OUT = console.log.bind(console);
GET_ELE = DOC.getElementById.bind(DOC);

const shuffleArray = arr => arr.sort(() => Math.random() - 0.5);

function RandomInt_light(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function RandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
}

Array.prototype.chunk = function(groupsize){
    var sets = [], chunks, i = 0;
    chunks = this.length / groupsize;

    while(i < chunks){
        sets[i] = this.splice(0,groupsize);
    i++;
    }
    
    return sets;
}


function sleep(sec) {
    return new Promise(resolve => setTimeout(resolve, sec*1000));
}


Math.degrees = function(radians) {
  return radians * 180 / Math.PI;
}


function atan360(y, x) {
    if (0 <= y)
        return Math.degrees(Math.atan2(y, x));
    else
        return 360 + Math.degrees(Math.atan2(y, x));
}


String.prototype.as_axes = function() {
    let axes = this.split(',');

    return [parseInt(axes[0]), parseInt(axes[1])];
}

function removeChildAll (parent) {
    while (parent.firstChild) parent.removeChild(parent.firstChild);
}

Object.prototype.len = function () {
    return Object.keys(this).length;
}