#!/usr/bin/node
const request = require('request');
const api = process.argv[2];
request(api, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let num_of_counts = 0;
    const movies = JSON.parse(body).results;
    for (let res = 0; res < movies.length; res++) {
      const character = movies[res].character;
      for (let i = 0; i < character.length; i++) {
        if (character[i] === 'https://swapi-api.alx-tools.com/api/people/18' || character[i] === 'https://swapi-api.alx-tools.com/api/people/18/') {
	  num_of_counts += 1;
	}
      }
    }
	  console.log(num_of_counts);
  }
});
