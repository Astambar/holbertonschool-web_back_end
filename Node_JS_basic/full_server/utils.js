// full_server/utils.js

const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        // Parse the data from the database file and return the object of arrays of first names per fields
        const databaseObject = parseDataFromDatabase(data);
        resolve(databaseObject);
      }
    });
  });
}

function parseDataFromDatabase(data) {
  const lines = data.trim().split('\n');
  const headers = lines[0].split(',');
  const databaseObject = {};

  // Initialize the databaseObject with an array for each field
  headers.forEach(header => {
    databaseObject[header.trim()] = [];
  });

  // Skip the first line (headers) and start from index 1
  for (let i = 1; i < lines.length; i++) {
    const values = lines[i].split(',');

    // Iterate through each value and push it to the corresponding field's array
    values.forEach((value, index) => {
      const header = headers[index].trim();
      databaseObject[header].push(value.trim());
    });
  }

  return databaseObject;
}

module.exports = {
  readDatabase,
};
