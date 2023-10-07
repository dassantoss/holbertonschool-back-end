# ES6 Promises
## What is a Promise?
A promise is an object that may produce a single value some time in the future: either a resolved value, or a reason that it's not resolved (e.g., a network error occurred). A promise may be in one of 3 possible states: fulfilled, rejected, or pending. Promise users can attach callbacks to handle the fulfilled value or the reason for rejection.

Promises are eager, meaning that a promise will start doing whatever task you give it as soon as the promise constructor is invoked. If you need lazy, check out [observables](

## Why Promises?
Promises are a far cleaner solution to writing asynchronous code than callbacks. They allow you to write code that assumes a value is returned within a success callback, and another value is returned in an error callback. This is much cleaner than having to write a bunch of nested callbacks, and makes it much easier to handle errors.

## Creating a Promise
```javascript
var promise = new Promise(function(resolve, reject) {
  // do a thing, possibly async, then…

  if (/* everything turned out fine */) {
	resolve("Stuff worked!");
  }
  else {
	reject(Error("It broke"));
  }
});
```

## Consuming a Promise
```javascript
promise.then(function(result) {
  console.log(result); // "Stuff worked!"
}, function(err) {
  console.log(err); // Error: "It broke"
});
```

## Chaining Promises
```javascript
var promise = new Promise(function(resolve, reject) {
  resolve(1);
});

promise.then(function(val) {
  console.log(val); // 1
  return val + 2;
}).then(function(val) {
  console.log(val); // 3
});
```

## Catching Errors
```javascript
var promise = new Promise(function(resolve, reject) {
  throw new Error('Uh-oh!');
});

promise.catch(function(err) {
  console.log(err); // Error: Uh-oh!
});
```

## Promise.all
```javascript
var promise1 = Promise.resolve(3);
var promise2 = 42;
var promise3 = new Promise(function(resolve, reject) {
  setTimeout(resolve, 100, 'foo');
});

Promise.all([promise1, promise2, promise3]).then(function(values) {
  console.log(values); // [3, 42, 'foo']
});
```




