// full_server/controllers/StudentsController.js

const { readDatabase } = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    readDatabase('./database.csv')
      .then(databaseObject => {
        res.status(200).send('This is the list of our students\n' + formatDatabaseObject(databaseObject));
      })
      .catch(error => {
        res.status(500).send(error.message);
      });
  }

  static getAllStudentsByMajor(req, res) {
    const major = req.params.major.toUpperCase();

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
    } else {
      readDatabase('./database.csv')
        .then(databaseObject => {
          const studentsList = databaseObject[major] || [];
          res.status(200).send('List: ' + studentsList.join(', '));
        })
        .catch(error => {
          res.status(500).send(error.message);
        });
    }
  }
}

function formatDatabaseObject(databaseObject) {
  let result = '';

  // Add the count and list of students for each field to the result string
  Object.keys(databaseObject).sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' })).forEach(field => {
    const studentsCount = databaseObject[field].length;
    const studentsList = databaseObject[field].join(', ');

    result += `Number of students in ${field}: ${studentsCount}. List: ${studentsList}\n`;
  });

  return result;
}

module.exports = StudentsController;
