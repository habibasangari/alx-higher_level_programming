#!/usr/bin/node


const request = require('request');


request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) { console.log(error); }
  if (response) { console.log(JSON.parse(body).title); }
});
