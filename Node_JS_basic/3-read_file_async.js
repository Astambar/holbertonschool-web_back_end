const fs = require('fs');

async function countStudents(filePath) {
  try {
    // Asynchronously read the file
    const data = await fs.promises.readFile(filePath, 'utf8');

    // Split the data into lines and filter out empty lines
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Initialize counters for each field
    let csStudents = 0;
    let sweStudents = 0;

    // Arrays to store first names for each field
    const csStudentNames = [];
    const sweStudentNames = [];

    // Loop through each line and count students in each field
    lines.forEach((line) => {
      const [firstName, lastName, age, field] = line.split(',');
      if (field === 'CS') {
        csStudents++;
        csStudentNames.push(firstName.trim());
      } else if (field === 'SWE') {
        sweStudents++;
        sweStudentNames.push(firstName.trim());
      }
    });

    // Log the total number of students
    console.log(`Number of students: ${lines.length -1}`);

    // Log the number of students in each field and their first names
    console.log(`Number of students in CS: ${csStudents}. List: ${csStudentNames.join(', ')}`);
    console.log(`Number of students in SWE: ${sweStudents}. List: ${sweStudentNames.join(', ')}`);

  } catch (error) {
    // Throw an error if the database is not available
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
