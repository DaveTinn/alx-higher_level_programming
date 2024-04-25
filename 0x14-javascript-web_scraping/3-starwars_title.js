#!/usr/bin/node
const request = require('request');
const filepath = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/films/' + filepath;
request(api, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(body && JSON.parse(body).title);
  }
});
